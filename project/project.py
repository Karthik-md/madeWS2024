import os
import requests
import configparser
import pandas as pd
import sqlite3

# Function to download a CSV file from a URL
def download_csv(url, folder_name, filename):
    # Create folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # Full path to save the file
    file_path = os.path.join(folder_name, filename)
    
    # Send GET request to download the file
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"CSV file downloaded successfully from {url} as {file_path}")
    else:
        print(f"Failed to download {url}. Status code: {response.status_code}")

# Function to create SQLite database, delete existing data, and write new CSV data to a table
def write_csv_to_db(csv_file_path, db_name):
    # Connect to SQLite database (it will create the DB if it doesn't exist)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Get the table name based on the CSV file name (without extension)
    table_name = os.path.splitext(os.path.basename(csv_file_path))[0]

    # Delete data if the table already exists
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    print(f"Existing table '{table_name}' deleted (if it existed).")

    # Write the entire DataFrame to a new table in SQLite
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    print(f"Data from {csv_file_path} written to '{table_name}' table in SQLite DB.")

    # Commit and close the connection
    conn.commit()
    conn.close()

# Read URLs from app.config file
config = configparser.ConfigParser()
config.read('app.config')

# Folder name to save CSV files
folder_name = 'data'
# SQLite database file name
db_name = 'data.db'

# Iterate over all URLs in the config file, download CSV files, and write them to DB
for key in config['urls']:
    url = config['urls'][key]
    filename = f"{key}.csv"
    
    # Download CSV file
    download_csv(url, folder_name, filename)
    
    # Get the full path of the downloaded CSV file
    csv_file_path = os.path.join(folder_name, filename)
    
    # Write the entire CSV data to a new table in SQLite DB
    write_csv_to_db(csv_file_path, db_name)

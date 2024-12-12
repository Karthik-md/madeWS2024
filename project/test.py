import os
import sqlite3
import pandas as pd
import unittest
from unittest.mock import patch
from project import download_csv, write_csv_to_db
import configparser

class TestProject(unittest.TestCase):

    @patch('project.requests.get')
    def test_download_csv(self, mock_get):
        # Mock the response from requests.get
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = b'Test data'

        # Read from app.config
        config = configparser.ConfigParser()
        config.read('./project/app.config')
        folder_name = 'test_data'
        url = config['urls']['url1']
        filename = 'test.csv'
        download_csv(url, folder_name, filename)

        # Check if the file was created
        file_path = os.path.join(folder_name, filename)
        self.assertTrue(os.path.exists(file_path))

        # Clean up
        os.remove(file_path)
        os.rmdir(folder_name)

    def test_write_csv_to_db(self):
        # Create a sample CSV file
        csv_file_path = 'test.csv'
        df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        df.to_csv(csv_file_path, index=False)

        # Call the function
        db_name = 'test.db'
        write_csv_to_db(csv_file_path, db_name)

        # Check if the table was created in the database
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='test'")
        table_exists = cursor.fetchone()
        self.assertIsNotNone(table_exists)

        # Clean up
        conn.close()
        os.remove(csv_file_path)
        os.remove(db_name)

    @patch('project.requests.get')
    def test_integration(self, mock_get):
        # Mock the response from requests.get
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = b'col1,col2\n1,3\n2,4'

        # Call the functions
        config = configparser.ConfigParser()
        config.read('./project/app.config')
        folder_name = 'test_data'
        filename = 'test.csv'
        url = config['urls']['url1']
        db_name = 'test.db'
        download_csv(url, folder_name, filename)
        csv_file_path = os.path.join(folder_name, filename)
        write_csv_to_db(csv_file_path, db_name)

        # Check if the table was created in the database
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='test'")
        table_exists = cursor.fetchone()
        self.assertIsNotNone(table_exists)

        # Clean up
        conn.close()
        os.remove(csv_file_path)
        os.remove(db_name)
        os.rmdir(folder_name)

if __name__ == '__main__':
    unittest.main()
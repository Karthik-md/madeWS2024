#!/bin/bash

# Run the tests
python3 -m unittest discover -s . -p '*test.py'

# Validate that the output files exist
if [ -f "data/url1.csv" ] && [ -f "data.db" ]; then
    echo "System test passed: Output files exist."
else
    echo "System test failed: Output files do not exist."
    exit 1
fi
#!/bin/bash

# PrimerPal Runner Script

# Set the directory containing the script as the working directory
cd "$(dirname "$0")"

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python 3 could not be found. Please install Python 3 and try again."
    exit 1
fi

# Check if the required Python packages are installed
python3 -c "import pandas, yaml" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Required Python packages are not installed. Installing them now..."
    pip3 install pandas pyyaml
    if [ $? -ne 0 ]; then
        echo "Failed to install required packages. Please install pandas and pyyaml manually."
        exit 1
    fi
fi

# Check if the config file exists
if [ ! -f "config.yaml" ]; then
    echo "config.yaml not found in the current directory."
    exit 1
fi

# Check if the Python script exists
if [ ! -f "PrimerPal.py" ]; then
    echo "PrimerPal.py not found in the current directory."
    exit 1
fi

# Run the Python script
echo "Running PrimerPal..."
python3 PrimerPal.py

# Check if the script ran successfully
if [ $? -eq 0 ]; then
    echo "PrimerPal completed successfully."
else
    echo "PrimerPal encountered an error. Please check the output above for details."
fi

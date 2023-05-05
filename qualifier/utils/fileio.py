# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""

import csv
# imported Path to allow 'save_csv' function to open a path to a new .csv file so UI allows saving loan_qualifier results if desired
from pathlib import Path

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

# defined 'save_csv' function in utils folder so app.py can call it when requested by user running program - maintaining DRY modular coding style
def save_csv(data, loan_list):
    """Creating a new function called save_csv that saves a csv file
    Args:
        data (list of lists): The list of filtered loans that the user qualifies for
    
    Returns:
        A csv file with the saved data
    """   
    
    bank_data = data

    #Creating headers for the csv file
    header = ["Lender", "Max Loan Amount", "Max LTV", "Max DTI", "Max Credit Score", "Interest Rate"]

    #Creating output path of the CSV file
    csvpath = Path(loan_list) 

    # Open csv file in csvpath by using the open() method
    with open(csvpath, "w", newline='') as csvfile:

        csvwriter = csv.writer(csvfile, delimiter = ",")
        csvwriter.writerow(header)
        for row in bank_data:
            csvwriter.writerow(row)

    return data


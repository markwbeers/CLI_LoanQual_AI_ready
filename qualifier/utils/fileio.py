# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
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

# code below needed to define 'save_csv' function used in 'loan_qualifier_app_v2.py'
# def save_csv(filtered_loans, loan_data):
#     with open(filtered_loans, 'w') as app_output:
#         write = csv.writer(app_output)
#         write.writerows(loan_data)

# # def save_csv("pre_qual.csv", newline='') as f:
# #     csvfile = 

# # # def save_csv(csvpath, data, header=None):
# # #     """Saves the CSV file from path provided.

# # #     Args:
# # #         csvpath (Path): The CSV file path.
# # #         data (list of lists): A list of the rows of data for the CSV file.
# # #         header (list): An optional header for the CSV.

# # #     """
# # #     with open(csvpath, "w", newline="") as csvfile:
# # #         csvwriter = csv.writer(csvfile, delimiter=',')
# # #         if header:
# # #             csvwriter.writerow(header)
# # #         csvwriter.writerows()








# # # code to define 'save_csv' function - located here to maintain modular style
# # # def save_csv(filtered_loans, loan_data):
# # #     with open(filtered_loans, 'w') as app_output:
# # #         write = csv.writer(app_output)
# # #         write.writerows(loan_data)

# # # define function(Path, data, header)

# # # def save_csv(qual_loans.csv, loan_data, header=None):

# # #     with open(qual_loans.csv, 'w', newline="") as prequal_csvfile:
# # #         writer = csv.writer(prequal_csvfile, delimiter=',')
# # #         if header:
# # #             writer.writerow(header)
# # #         writer.writerows(loan_data)

# # # def save_csv(csvpath, data, header=None):
# # #     """Saves the CSV file from path provided.

# # #     Args:
# # #         csvpath (Path): The CSV file path.
# # #         data (list of lists): A list of the rows of data for the CSV file.
# # #         header (list): An optional header for the CSV.

# # #     """
# # #     with open(csvpath, "w", newline="") as csvfile:
# # #         csvwriter = csv.writer(csvfile, delimiter=',')
# # #         if header:
# # #             csvwriter.writerow(header)
# # #         csvwriter.writerows(data)

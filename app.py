# -*- coding: utf-8 -*-
"""Loan Qualifier Application.

This is a command line application to match applicants with qualifying loans.

Example:
    $ python app.py
"""
import sys
import fire # imported fire library to enable python object conversion to CLI creation requested by BizOps Team
import questionary as qst # imported questionary as 'qst' library required to write simple CLI's with shortened code
from pathlib import Path # path module creates strings that represent file paths

from qualifier.utils.fileio import load_csv, save_csv
# from qualifier.utils.fileio import save_csv <-- added then replaced line#15 with simpler import code - ie. ...", save_csv" addition to line 14

from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)

from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value

print("\n") # code added to improve UI output appearance/spacing in terminal output

def underline(text):
    print("\u0332".join(text))

underline("Welcome to the UCB FinTech Desktop Underwriter Terminal!\n") # added welcome text for more attractive UI
print("Thank you for using our Home Equity Line of Credit (HELOC) pre-qual screening portal.\n")
print("\t Today's Bank Loan Offerings located here --> 'data/rates.csv' <-- (enter below)\n") # made shortened .csv filename - improves ease of use

def load_bank_data():
    """Ask for the file path to the latest banking data and load the CSV file.

    Returns:
        The bank data from the data rate sheet CSV file.
    """

    csvpath_rates = qst.text("Enter the file path above for today's bank rate-sheet (.csv):").ask() # improved ease of use, clarified instruction wording
    csvpath_rates = Path(csvpath_rates)
    if not csvpath_rates.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath_rates} - please run program again when ready...")

    return load_csv(csvpath_rates)

def get_applicant_info():
    """Prompt dialog to get the applicant's financial information.

    Returns:
        Returns the applicant's financial information.
    """

    credit_score = qst.text("What's your credit score?").ask()
    debt = qst.text("What's your current amount of monthly debt?").ask()
    income = qst.text("What's your total monthly income?").ask()
    loan_amount = qst.text("What's your desired loan amount?").ask()
    home_value = qst.text("What's your home value?").ask()

    credit_score = int(credit_score)
    debt = float(debt)
    income = float(income)
    loan_amount = float(loan_amount)
    home_value = float(home_value)

    return credit_score, debt, income, loan_amount, home_value


def find_qualifying_loans(bank_data, credit_score, debt, income, loan, home_value):
    """Determine which loans the user qualifies for.

    Loan qualification criteria is based on:
        - Credit Score
        - Loan Size
        - Debit to Income ratio (calculated)
        - Loan to Value ratio (calculated)

    Args:
        bank_data (list): A list of bank data.
        credit_score (int): The applicant's current credit score.
        debt (float): The applicant's total monthly debt payments.
        income (float): The applicant's total monthly income.
        loan (float): The total loan amount applied for.
        home_value (float): The estimated home value.

    Returns:
        A list of the banks willing to underwrite the loan.

    """

    # Calculate the monthly debt ratio
    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income) # modified print-f below to show % output for DTI ratio
    print(f"\nYour current monthly 'Debt to Income' ratio is {100 * monthly_debt_ratio:.02f}%\n")
    
    # Calculate loan to value ratio
    loan_to_value_ratio = calculate_loan_to_value_ratio(loan, home_value)
        
    # Run qualification filters
    bank_data_filtered = filter_max_loan_size(loan, bank_data)
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)
        
    if len(bank_data_filtered) == 0: # offered message of hope and encouragement below for failed applicant - and a clean errorless exit from the program below
        sys.exit("Unfortunately you did not pre-qualify for loans today; however, you may schedule a free appointment with our credit counselor.")

    print(f"You have qualified for {len(bank_data_filtered)} loans based on your responses.\n") # modified print-f below with % and CLTV increase comment
    print(f"If fully approved, will increase your 'combined loan to value'(CLTV Ratio) by {100 * loan_to_value_ratio:.02f}%.\n")
    print(f"Ask your loan officer about a rate/term 'cash out' refi of current mortgage, especially if drawing the new loan for debt consolidation.")
    
    return bank_data_filtered

def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    # YOUR CODE HERE!
    user_saves_loans = qst.confirm("Would you like to save the list of your pre-approved loan options as a (.csv) file?\n").ask()
    if user_saves_loans == False:
        sys.exit("Thank you for checking your financing options using the desktop underwriter.  Rates, loan amounts, and borrower requirements are subject to change daily.")

    if user_saves_loans == True:
        prequal_list_path = qst.text("please enter the path to save your list as a (.csv) file:\n").ask()
        prequal_list_path = Path(prequal_list_path)
    
    print (f"Your loans are now saved in {prequal_list_path}.  Thank you for using the UCB FinTech Desktop Underwriter!\n")
    
    return save_csv(qualifying_loans, prequal_list_path)
            
    
def run():
    """The main function for running the script."""

    # Load the latest Bank data
    bank_data = load_bank_data()

    # Get the applicant's information
    credit_score, debt, income, loan_amount, home_value = get_applicant_info()

    # Find qualifying loans
    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )
 
    # Save qualifying loans
    save_qualifying_loans(qualifying_loans)

if __name__ == "__main__":
    fire.Fire(run)

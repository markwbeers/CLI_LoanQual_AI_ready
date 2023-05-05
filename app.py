# -*- coding: utf-8 -*-
"""Loan Qualifier Application.

This is a command line application to match applicants with qualifying loans.

Example:
    $ python app.py
"""
import sys
import fire
import questionary as qst
from pathlib import Path

from qualifier.utils.fileio import load_csv
from qualifier.utils.fileio import save_csv

from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)

from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value

# code added to improve UI appearance
print("\n")

def underline(text):
    print("\u0332".join(text))

underline("Welcome to the UCB FinTech Desktop Underwriter Terminal!\n")
print("Thank you for using our Home Equity Line of Credit (HELOC) pre-qual screening portal.\n")
print("\t Today's Bank Loan Offerings located here --> 'data/rates.csv' <-- (enter below)\n")

def load_bank_data():
    """Ask for the file path to the latest banking data and load the CSV file.

    Returns:
        The bank data from the data rate sheet CSV file.
    """

    csvpath_rates = qst.text("Enter a file path to a rate-sheet (.csv):").ask()
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
    # modified print-f statement to use more descriptive wording for and also to output a % instead of decimal
    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
    print(f"\nYour current monthly 'Debt to Income' ratio is {100 * monthly_debt_ratio:.02f}%\n")
    
    # Calculate loan to value ratio
    # modified print-f statement to use more descriptive wording for and also to output a % instead of decimal
    loan_to_value_ratio = calculate_loan_to_value_ratio(loan, home_value)
    # print(f"If fully approved and accepted, this loan would increase your current 'loan to value' by {100 * loan_to_value_ratio:.02f}%.\n")
    
    # Run qualification filters
    bank_data_filtered = filter_max_loan_size(loan, bank_data)
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)
        
    if len(bank_data_filtered) == 0:
        sys.exit("Unfortunately you did not pre-qualify for loans today; however, you may schedule a free appointment with our credit counselor.")

    # # print(f"Based on your responses, you are pre-qualified for {len(bank_data_filtered)} loans.\n")
    # else: 
    print(f"You have qualified for {len(bank_data_filtered)} loans based on your responses.\n")
    print(f"If fully approved and accepted, this loan would increase your current 'loan to value' by {100 * loan_to_value_ratio:.02f}%.\n")
    
    return bank_data_filtered
    # user_saves_loans = qst.confirm("Would you like to save the list of your pre-approved loan options as a (.csv) file?\n").ask()
    # if user_saves_loans == False:
    #     sys.exit("goodbye")

    # if user_saves_loans == True:
    #     prequal_list_path = qst.text("please enter the path to save your list as a (.csv) file:").ask()
    

def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    # YOUR CODE HERE!
    user_saves_loans = qst.confirm("Would you like to save the list of your pre-approved loan options as a (.csv) file?\n").ask()
    if user_saves_loans == False:
        sys.exit("goodbye")

    if user_saves_loans == True:
        prequal_list_path = qst.text("please enter the path to save your list as a (.csv) file:").ask()
        prequal_list_path = Path(prequal_list_path)
    print(prequal_list_path)
    print("11111111111111")
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
  #  print(qualifying_loans)

    # Save qualifying loans
    save_qualifying_loans(qualifying_loans)

if __name__ == "__main__":
    fire.Fire(run)

#######################################
# LOAN ANALYZER ... Can You Dig it ?
######################################

####  Imports ####
import csv
from csv import writer
from pathlib import Path
import numpy as np
# ---- End of Imports ---- #


def about_this_loan (loan_inquestion=list):
    loan_inquestion_sum = sum(loan_inquestion)
    loan_inquestion_avg = np.mean(loan_inquestion)
    loan_inquestion_num = len(loan_inquestion)

    return loan_inquestion_num, loan_inquestion_sum, loan_inquestion_avg

def present_value(loan=dict, rate=float):

    loan_price = loan.get("loan_price")
    loan_future_val = loan.get("future_value")
    loan_remaining_months =  loan.get("remaining_months")

    present_value = loan_future_val/(1 + (rate/12))**loan_remaining_months

    return loan_price, loan_future_val, loan_remaining_months, present_value

def conditional_calc(present_value, orig_loan_price):

    if present_value >- loan_price:
        print(f"Buy it and grow fat off someone else's debt")
    else:
        print(f"Drop this loan, can't profit enough from another pain")

    return()

def conditional_filter(loans):
    sub500_list = []

    for loan in loans:
        if loan['loan_price'] <= 500:
            sub500_list.append(loan)

    return sub500_list

""""
For the send_to_csv here are some notes:
Here is the deal we need to have two lists:
    1. one list of field names
    2. one list of row values

I doubled down on my for looping to get a list of rows
"""
def send_to_csv(loans_list =list):

    csv_fields = ['loan_price', 'remaining_months', 'repayment_interval','future_value']
    csv_rows = []

    for loan in inexpensive_list:
        new_output = list(loan.values())
        csv_rows.append(new_output)

    
    with open('Loan_list.csv', 'w') as f:

    # using csv.writer method from CSV package
        write = csv.writer(f)  
        write.writerow(csv_fields)
        write.writerows(csv_rows)




###  Variable List ###
#Givens - Variables we are given to work with
#     loans_cost - list of loan prices
loan_costs = [500, 600, 200, 1000, 450]

#loan -  dictionary where the keys are the loan features
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# loans - a list of dictionaries we have to lopp through to show off our loop mastery, ya know spice things up
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]


# Created Variables
# - variables we need to create for the assignment
# - I'm just going to initialize them alll here, because you love to see it 
num_of_loans = ''
sum_of_loans = ''
avg_of_loans = ''
rate = 0.20
inexpensive_list =[]

####################
### MAIN PROGRAM ###
####################

""""PART ONE: GIVE ME INFORMATION ABOUT THE LOAN
1. How many loans
2. Sum of all Loans
3. Average of all loans
4. Note: This  sends information to a defintion to do the dirty work line 104
"""
num_of_loan, sum_of_loans, avg_of_loans = about_this_loan(loan_costs)
print(f"There are: {num_of_loans} loans in this list")
print(f"The sum of all the loans are ${sum_of_loans}")
print(f"The average cost of these {num_of_loans} loans are: {avg_of_loans}")

## PART TWO: THE NEXT EPISODE LOAN CALCULATIONS
"""Part 2: Analyze Loan Data.
Analyze the loan to determine the investment evaluation.
That means using the get function to pull out the following parameters:
1. Original Price
2. Months Remaining
3. Future value of the loan
4. Present value of the loan
 Note: this  sends information to a defintion to do the dirty work line 122
"""

print(f"We have a situation on our hands. We have a loan that we need to calculate the present value of the loan")
print(f"... yeah I know not all heros wear capes !!!")

loan_price,loan_future_val,loan_remaining_months, present_value = present_value(loan,rate)
print("\n\n\n")
print(f"For the loan in our dictionary, the original loan_price is: ${loan_price}, remaining months left: {loan_remaining_months}")
print(f"The present and future values of the loan at a {rate}% is {present_value} and {loan_future_val}")
print("\n\n")

## PART THREE: Should you by this loan?
"""
Using the present value calculation, we want to determine using a conditional
should the company acquire the loan in question. The best way to do so is to do
so as a function. Ideally this should be a loop that iteration through a more 
complex data structure like a dataframe a list of lists, a list of dictionary
but thats the next section
"""
print(f"The question remains: Does it make sense to buy the loan at its current cost?")
print(f"The answer:")

# the conditional compares to values and depending  determines the whether the loand should be purchased.
conditional_calc(present_value,loan_price)

## PART FOUR: Conditionally Filter Lists of Loans
""" Now your task is to loop through a series of loans that 
the company is considering and filter them to find the inexpensive 
ones i.e. less than or equal to $500.
"""

inexpensive_list = conditional_filter(loans)
print(f"With the criteria established( less than or equal to $500, we have found {len(inexpensive_list)} loans")
print(f"First loan: {inexpensive_list[0]}")
print(f"Second loan: {inexpensive_list[1]}")

print(f"ill put this information in a file and export it for you")
send_to_csv(inexpensive_list)
print(f"All Done")
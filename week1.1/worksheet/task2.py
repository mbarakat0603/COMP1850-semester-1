"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Mohammad Barakat
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.

try:
    amount = int(input("Enter an amount you want to save per month: "))

    # Calculate the total amount of money they will have saved by the end of the year
    # print this out for the user with a suitable message.
    yearly = amount * 12
    print(f"By the end of the year you will have saved £{yearly}")

    # Calculate the total amount of money including interest (0.8% of the final annual amount)
    # print this out in the format £X.XX (to two decimal places).
    with_interest = yearly * 1.008
    print(f"With interest you will have £{with_interest:.2f}")
except:
    print("Please enter a whole number.")
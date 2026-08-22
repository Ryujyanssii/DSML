from finance_tools.tax import calculate_tax
from finance_tools.loan import calculate_emi

try:
    # Tax
    income = float(input("Enter your income: "))
    tax_rate = float(input("Enter tax rate (%): "))

    tax = calculate_tax(income, tax_rate)

    print("Tax:", tax)

    # Loan
    amount = float(input("\nEnter loan amount: "))
    rate = float(input("Enter interest rate (%): "))
    years = int(input("Enter loan period (years): "))

    emi = calculate_emi(amount, rate, years)

    print("Monthly EMI:", emi)

except ValueError:
    print("Invalid input! Please enter numbers only.")
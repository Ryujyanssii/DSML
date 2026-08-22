def calculate_emi(principal, rate, years):
    interest = principal * rate * years / 100
    total_amount = principal + interest
    emi = total_amount / (years * 12)

    return emi
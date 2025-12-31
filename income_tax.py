def compute_tax(status, income):
    # Tax brackets: (rate, upper_limit)
    if status == 0:  # Single
        brackets = [
            (0.10, 8350),
            (0.15, 33950),
            (0.25, 82250),
            (0.28, 171550),
            (0.33, 372950),
            (0.35, float('inf'))
        ]
    elif status == 1:  # Married filing jointly
        brackets = [
            (0.10, 16700),
            (0.15, 67900),
            (0.25, 137050),
            (0.28, 208850),
            (0.33, 372950),
            (0.35, float('inf'))
        ]
    elif status == 2:  # Married filing separately
        brackets = [
            (0.10, 8350),
            (0.15, 33950),
            (0.25, 68525),
            (0.28, 104425),
            (0.33, 186475),
            (0.35, float('inf'))
        ]
    elif status == 3:  # Head of household
        brackets = [
            (0.10, 11950),
            (0.15, 45500),
            (0.25, 117450),
            (0.28, 190200),
            (0.33, 372950),
            (0.35, float('inf'))
        ]
    else:
        return None

    tax = 0
    previous_limit = 0

    for rate, limit in brackets:
        if income > limit:
            tax += (limit - previous_limit) * rate
            previous_limit = limit
        else:
            tax += (income - previous_limit) * rate
            break

    return tax


# ---- MAIN PROGRAM ----
status = int(input("Enter filing status (0-single, 1-married jointly, 2-married separately, 3-head of household): "))
income = float(input("Enter taxable income: "))

tax = compute_tax(status, income)

if tax is None:
    print("Invalid filing status.")
else:
    print(f"Your total tax is: ${tax:.2f}")
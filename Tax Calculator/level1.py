def tax_calc():
    age = int(input('Enter Your Age: '))
    income = int(input('Enter Your Total Income: '))

    if age < 60:
        if income <= 20_000:
            tax = 0
        if income > 20_000 and income <= 50_000:
            tax = income * 0.2
        if income > 50_000 and income <= 100_000:
            tax = income * 0.3
        if income > 100_000:
            tax = income * 0.4

    elif age >= 60:
        if income <= 20_000:
            tax = 0
        if income > 20_000 and income <= 50_000:
            tax = income * 0.1
        if income > 50_000 and income <= 100_000:
            tax = income * 0.2
        if income > 100_000:
            tax = income * 0.3

    print(f'Taxes Due: {tax: ,.0f}')


tax_calc()

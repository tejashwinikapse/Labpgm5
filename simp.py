def calculate_simple_interest(principal, rate, time):
    return principal * rate * time / 100


try:
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual rate of interest (%): "))
    time = float(input("Enter time in years: "))

    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Values must be zero or greater.")

    interest = calculate_simple_interest(principal, rate, time)
    print(f"Simple interest: {interest:.2f}")

except ValueError as error:
    print(f"Invalid input: {error}")
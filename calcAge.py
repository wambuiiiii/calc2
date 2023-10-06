from datetime import datetime


def calculate_age(birthdate):
    # Convert the birthdate string to a datetime object/integer
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")


    current_date = datetime.now()
    years = current_date.year - birthdate.year
    months = current_date.month - birthdate.month
    days = current_date.day - birthdate.day

    # Adjust for negative months or days
    if days < 0:
        months -= 1
        days += 30  # Assuming each month has 30 days for simplicity

    if months < 0:
        years -= 1
        months += 12

    return years, months, days



birthdate = input("Enter your birthdate (YYYY-MM-DD): ")

years, months, days = calculate_age(birthdate)

print(f"Your age is {years} years, {months} months, and {days} days.")

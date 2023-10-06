
def calculate_bill(total_bill, tip_percentage, num_people):

    tip = tip_percentage / 100


    tip_amount = total_bill * tip


    total_amount = total_bill + tip_amount


    per_person_amount = total_amount / num_people

    return per_person_amount

# Input
try:
    total_bill = float(input("Enter the total bill amount: $"))
    tip_percentage = float(input("Enter the tip percentage (10, 12, or 15): "))
    num_people = int(input("Enter the number of people splitting the bill: "))
    if tip_percentage not in [10, 12, 15]:

        raise ValueError("Tip percentage must be 10, 12, or 15.")


    per_person_amount = calculate_bill(total_bill, tip_percentage, num_people)

    print(f"Each person should pay: ${per_person_amount:.2f}")

except ValueError as e:
    print("Invalid input. Please enter valid numeric values for bill amount, tip percentage, and number of people.")

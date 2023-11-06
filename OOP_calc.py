class Calculator:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "Division by zero is not allowed."
        return num1 / num2



calc = Calculator()
while True:
    print("Options:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '5':
        break

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = calc.add(num1, num2)
        elif choice == '2':
            result = calc.subtract(num1, num2)
        elif choice == '3':
            result = calc.multiply(num1, num2)
        elif choice == '4':
            result = calc.divide(num1, num2)
        print("Result: ", result)
    else:
        print("Invalid input")








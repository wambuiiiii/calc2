print("Here is a simple calculator")
print("1.Adddition")
print("2.Subtraction")
print("3.Multiplication")
print("4.division")
option = int(input("Pick an option(1-4):"))
num1 = float(input("Enter your first number:"))
num2 = float(input("Enter the second number:"))

if option == 1:

    print("Result is:",num1+num2)

elif option == 2:
    result2 = num1 - num2
    print("Result:", result2)
elif option == 3:
    result3 = num1 * num2
    print("Result:", result3)
elif option == 4:
    if num2 != 0:
        result4 = num1 / num2
        print("Result", result4)
    else:
        print("Divivsion by 0 is not allowed")

else:
    print("invalid choice")

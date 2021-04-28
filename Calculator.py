print('''Select an operation to perform:
Press 1 for Addition
Press 2 for Subtraction
Press 3 for Multiplication
Press 4 for Division
Press 5 for Exponents''')


operation = input()

if operation == "1":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is: " + str(int(num1) + int(num2)))

elif operation == "2":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The difference is: " + str(int(num1) - int(num2)))

elif operation == "3":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The product is: " + str(int(num1) * int(num2)))

elif operation == "4":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The result is: " + str(int(num1) // int(num2)))

elif operation == "5":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The answer is: " + str(int(num1) ** int(num2)))



else:
    print("INVALID ENTRY !!!. Please try again.")

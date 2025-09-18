def simple_calculator():
    print("Welcome to the Simple Calculator!")
    print("You can perform addition, subtraction, multiplication, and division.")

    num1 = float(input("Enter the first number: "))
    op = input ("Enter an operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if op == '+':
        print ('Result:', num1 + num2)
    elif op == '-':
        print ('Result:', num1 - num2)
    elif op == '*':
        print ('Result:', num1 * num2)
    elif op == '/':
        if num2 > 0:
            print ('Result:', num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")


simple_calculator()
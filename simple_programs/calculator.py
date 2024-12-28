# Here I would be making a calculator program that would be able to perform basic arithmetic operations based on the selection that the user does

def calculator():
    print("Welcome to the calculator program")
    print("Select the operation you would like to perform")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    operation = int(input("Enter the operation you would like to perform: "))
    if operation == 1:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print(f"The sum of {num1} and {num2} is {num1 + num2}")
    elif operation == 2:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print(f"The difference of {num1} and {num2} is {num1 - num2}")
    elif operation == 3:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print(f"The product of {num1} and {num2} is {num1 * num2}")
    elif operation == 4:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print(f"The division of {num1} and {num2} is {num1 / num2}")
    elif operation == 5:
        print("Exiting the program")
    else:
        print("Invalid operation selected")
        calculator()

if __name__ == "__main__":
    calculator()
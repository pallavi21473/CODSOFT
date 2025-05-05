def add(x, y):
    """Adds two numbers."""
    return x + y

def subtract(x, y):
    """Subtracts two numbers."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

def divide(x, y):
    """Divides two numbers."""
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y

def main():
    """Main function to run the calculator."""
    print("--- Simple Calculator ---")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            break # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        choice = input("Enter your choice (+/-/*//): ")

        if choice in ['+', '-', '*', '/']:
            break # Exit the loop if choice is valid
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

    if choice == '+':
        result = add(num1, num2)
        operation_symbol = '+'
    elif choice == '-':
        result = subtract(num1, num2)
        operation_symbol = '-'
    elif choice == '*':
        result = multiply(num1, num2)
        operation_symbol = '*'
    elif choice == '/':
        result = divide(num1, num2)
        operation_symbol = '/'

    print("\n--- Calculation Result ---")
    if isinstance(result, str): # Check if it's the error message
        print(result)
    else:
        print(f"{num1} {operation_symbol} {num2} = {result}")
    print("--------------------------")

if __name__ == "__main__":
    main()
# PROJECT: Simple Command-Line Calculator
# ... (all your step-by-step comments are here)

# STEP 1: Welcome the user to the calculator.
print("Welcome to the Simple Command-Line Calculator!")

def get_number(prompt_message):
    """Gets a valid number from the user by repeatedly prompting them."""
    while True:
        try:
            user_input = input(prompt_message)
            number = float(user_input)
            return number
        except ValueError:
            print("Invalid input. Please enter a number.")

# STEP 2: Ask the user for the first number and store it.
num1 = get_number("Enter the first number: ")

# STEP 3: Ask the user for the second number and store it.
num2 = get_number("Enter the second number: ")

# STEP 4: Ask the user for the operation.
operation = input("Enter the operation (+, -, *, /): ")

# STEP 5 & 7: Perform calculation and handle errors.
result = None  # Initialize result to None

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = num1 / num2
else:
    print("Invalid operation. Please use one of the following: +, -, *, /")

# STEP 6: Display the final result.
if result is not None:
    print(f"The result is: {result}")
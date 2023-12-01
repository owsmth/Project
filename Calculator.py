print("Hello! Welcome to The Calculator App!")

result = 0  # Initialize the result variable

while True:
    try:
        # Input for the operator
        operator = input("Enter an operator (+, -, *, /, **) or 'n' to exit: ")

        if operator.lower() == 'n':
            break

        # Input for the next number
        number = float(input("Enter the next number: "))

        # Perform the calculation based on the operator
        if operator == "+":
            result += number
        elif operator == "-":
            result -= number
        elif operator == "*":
            result *= number
        elif operator == "/":
            if number == 0:
                print("Error! Division by zero is not allowed.")
                continue
            result /= number
        elif operator == "**":
            result **= number
        else:
            print("Invalid operator! Please enter a valid operator.")
            continue

        print("Current Result:", result)

    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except Exception as e:
        print("Error:", e)

print("Thank you for using The Calculator App! Final Result:", result)

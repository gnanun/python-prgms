print("\n====== Simple Calculator ======\n")

while True:
    print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit\n")
    choice = int(input("Enter your choice (1-5): "))

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif choice == 2:
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif choice == 3:
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    elif choice == 4:
        if num2 != 0:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
    elif choice == 5:
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid choice! Please select a valid option (1-5).")

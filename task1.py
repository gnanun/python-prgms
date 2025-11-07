print("\n======Simple Calculator======\n")
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))  

print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")
choice=int(input("Enter your choice (1-3): "))

if choice==1:
        print(f"{num1} + {num2} = {num1 + num2}")
elif choice==2:
        print(f"{num1} - {num2} = {num1 - num2}")
elif choice==3:
        print(f"{num1} * {num2} = {num1 * num2}")
elif choice==4:
        if num2!=0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
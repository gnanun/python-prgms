print("Welcome to the Password Strength Checker!")

pwd=str(input("Enter your password: "))

if len(pwd)<8:
    print("Password must be at least 8 characters long.")
elif not any(char.isdigit() for char in pwd):
    print("Password must contain at least one digit.")
elif not any(char.isupper() for char in pwd):
    print("Password must contain at least one uppercase letter.")
elif not any(char.islower() for char in pwd):
    print("Password must contain at least one lowercase letter.")
elif not any(char in "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|" for char in pwd):
    print("Password must contain at least one special character.")
else:
    print("Password is valid.")


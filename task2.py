import random

number = random.randint(1, 100)
counts = 0
print("Welcome to the Number Guessing Game!\n")
print("I've chosen a number between 1 and 100. Can you guess it?\n")

while True:
        guess = int(input("Please enter your guess (between 1 and 100): "))
        counts += 1
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number} in {counts} attempts.")
            break

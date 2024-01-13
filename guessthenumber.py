import random

# Generate a random number between 1 and 10
generatedNumber = random.randrange(1, 10)

# Welcome message
print("Welcome to guess the number! The computer generates a random number, and YOU, the user, have to guess it.")

try:
    # Get user input as an integer
    userInput = int(input("Guess a number between 1-10: "))

    # Check if the user input is greater than 10
    if userInput > 10:
        print("This number is greater than 10!")
    else:
        # Check if the user's guess is correct
        if userInput == generatedNumber:
            print("You guessed correctly! Here's a cookie 🍪")
        else:
            print("Incorrect guess. Try again ☹️")

except ValueError:
    # Handle the case where the user enters a non-integer value
    print("Enter a valid whole number!")
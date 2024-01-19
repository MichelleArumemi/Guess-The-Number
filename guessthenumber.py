import random

userAttempts = 3
# Generate a random number between 1 and 50
generatedNumber = random.randrange(1, 51)

# Welcome message
print("Welcome to Guess The Number! The computer generates a random number, and YOU, the user, has to guess it.")
try:
    while userAttempts > 0:
        # Get user input as an integer
        userInput = int(input("Guess a number between 1 and 50: "))

        # Check if the user's guess is correct
        if userInput == generatedNumber:
            print("You guessed correctly! Here's a cookie 🍪")
            break

        # Check if the user input is greater than the generated number
        elif userInput > generatedNumber:
            userAttempts -= 1
            if userAttempts > 0:
                print("This number is too high. Try again.")
                print(f"You have {userAttempts} attempts left")
            else:
                print("You lose.")
                print(f"The number was {generatedNumber}")
                break

        # Check if the user input is less than the generated number
        elif userInput < generatedNumber:
            userAttempts -= 1
            if userAttempts > 0:
                print("This number is too low. Try again.")
                print(f"You have {userAttempts} attempts left")
            else:
                print("You lose.")
                print(f"The number was {generatedNumber}")
                break

except ValueError:
    # Handle the case where the user enters a non-integer value
    print("Enter a valid whole number!")

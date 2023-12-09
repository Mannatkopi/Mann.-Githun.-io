print('kutta kamina nuber gussin game ha ha ha')

```python
import random

# Generate a random number between 1 and 1
secret_number = random.randint(1, 100)

# Initialize the number of guesses
attempts = 0

print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 100. Can you guess it?")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Try a higher number.")
        elif guess > secret_number:
            print("Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break
    except ValueError:
        print("Please enter a valid number.")

print("Thanks for playing!")
```

Copy and paste this code into a Python environment to play the game. It's a simple guessing game where you try to guess a random number between 1 and 100. You can expand and customize this game as you like to make it more interesting and challenging.

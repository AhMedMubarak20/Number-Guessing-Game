import random

target_number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))

if guess == target_number:
    print("Congratulations! You guessed the number.")
else:
    print(f"Sorry, the number was {target_number}.")

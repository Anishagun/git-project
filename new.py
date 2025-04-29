import random

number = random.randint(1, 10)

print("Guess a number between 1 and 10")
guess = int(input("Enter your guess: "))

i = 1

while i < 10:
    if guess == number:
        print("Congratulations! You guessed the number.")
        break
    elif guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    
    guess = int(input("Enter your guess: "))
    i += 1
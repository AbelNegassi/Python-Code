# Number Guessing Game: Generate a random number and have the user guess with hints given back after each guess.
import numpy as nd
import random
# Generate random number
random_num = random.randint(1,100)

print("Guess a number between 1 and 100!")
for i in range(100):
    guess = int(input())
    if guess > random_num: #If the random number is less than the guess, tell the user the number is lower.
        print("Nice try! The number is lower. Guess again!")
    elif guess < random_num:
        print("NIce try! The number is higher. Guess again!")
    else:
        print("Congratulations! You got the number! Thank you for playing!")
        break


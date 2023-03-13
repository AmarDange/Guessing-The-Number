# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import pyfiglet

print("Welcome to 'NUMBER GUESSING GAME' ")

print(" please Enter your name :  ")


playing = input("Do you want to play?")

if playing !="yes":
    quit()

print("Okay! Let's start to  play game ! :")

def guess(x):
    random_number = random.randint(1, x)
    user_guess = None
    guess_count = 0
    while user_guess != random_number:
        user_guess = int(input(f"Guess the number between 1 to {x}  -  \n"))

        guess_count+=1

        if user_guess > random_number:
                print("Sorry, It's too high. Try Again")
        elif user_guess < random_number:
                print("Sorry, It's too low. Try Again")
    print(f"Congrats... You Guess The Correct Number in {guess_count} times.")

guess(101) 
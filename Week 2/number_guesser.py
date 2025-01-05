# Project 3
# January 5th, 2025
# The computer will randomly guess a number between 1 and 100 and it is up to you to guess it in 7 tries or less

import random

def random_generator():
    num1 = random.randint(1,100)
    return num1

def main_game():
    playing = True
    tries_left = 7
    min = 1
    max = 100
    win_state = False
    num1 = random_generator()
    while playing:
        
        num2 = int(input(f"Guess a number between {min} and {max}. You have {tries_left} tries left: "))

        if num1 > num2:
            print("Too low!")
            tries_left -= 1
            if num2 > min:
                min = num2

        elif num1 < num2:
            print("Too high!")
            tries_left -= 1
            if max > num2:
                max = num2

        elif num1 == num2:
            print("Damn, you win!")
            win_state == True
            response = input("Do you wish to continue? Type Y/N: ")
            response = response.capitalize().strip()
            playing = (response == "Y")
            num1 = random_generator()
            tries_left = 7
            min = 1
            max = 100

        if tries_left == 0:
            print(f"Better Luck Next Time! The correct number was {num1}")
            win_state = False
            response = input("Do you wish to continue? Type Y/N: ")
            response = response.capitalize().strip()
            playing = (response == "Y")
            num1 = random_generator()
            tries_left = 7
            min = 1
            max = 100

        if not playing:
            print("Thank you, and have a nice day!")
            break

main_game()
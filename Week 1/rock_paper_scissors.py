# Project 1
# January 4th, 2025
# This is meant to be a simple Rock, Paper, Scissors Game Playing Against the Computer

from time import sleep
import random

# Loading Screen
print("loading.")
sleep(1)
print("loading..")
sleep(1)
print("loading...")
sleep(1)

# Game Introduction
print("Hello, Welcome to the Ultimate game of Rock Paper Scissors")
sleep(1)
print("You go first, and I will independently come up with a response. I promise I won't cheat!")
sleep(1)
name = input("To begin, please say your name: ")
name = name.capitalize()

sleep(1)
print(f"Aha, welcome {name}! My name is Neo. Let's see who prevails.")
sleep(1)

# Initialize Variables
playing = True
player_score = 0
neo_score = 0

# Main Loop
while playing:

    print("Next Round Starting in")
    sleep(0.5)
    print("3")
    sleep(0.5)
    print("2")
    sleep(0.5)
    print("1")
    sleep(0.5)

    collection = ["Rock", "Scissors", "Paper"]

    print("Rock")
    print("Paper")
    print("Scissors")
    # Computer Selects Choice
    computer_selection = random.randint(0,2)

    # Player Selects Choice
    while True:
        try:
            player_selection = input(f"{name}: ")
            player_selection = player_selection.capitalize().strip()

            # Check if the player's choice is valid
            if player_selection not in collection:
                raise ValueError("Invalid choice")  # Manually raise ValueError if not valid

            player_index = collection.index(player_selection)  # Get the index if valid
        except ValueError:
            print("Please Input a Valid Selection: 'Rock', 'Paper' or 'Scissors'.")
        else:
            print("Neo: " + collection[computer_selection])  # Show computer's choice
            break

    player_index = collection.index(player_selection)

    if player_index == computer_selection:
        print("Draw!")
        player_score += 0.5
        neo_score += 0.5
    elif player_index == (computer_selection - 1) % 3:
        print("You win!")
        player_score += 1
    else:
        print("You lose!")
        neo_score += 1

    print(f"The Scores are: Neo - {neo_score}, {name} - {player_score}")
    response = input("Do you wish to continue? Type Y/N: ")
    response = response.capitalize()
    playing = (response == "Y")

    if not playing:
        print("Thank you, and have a nice day!")
        if player_score > neo_score:
            print(f"And well done on beating me, {name}!")
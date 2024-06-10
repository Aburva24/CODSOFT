#Rock,Paper, Scissors Game
import random
print("Welcome you all! Let's play Rock, Paper, Scissor with Computer")
help = input("Do you need help to understand this game or not (Yes, No)= ").lower()
if help == "yes":
    print("Rock vs Paper -> Paper Wins")
    print("Rock vs Scissor -> Rock Wins")
    print("Scissor vs Paper -> Scissor Wins")
    print("Hope you understand the game")
elif help == "no":
    print("Let's start the game")

user_score = 0
machine_score = 0

while True:
    user_choice = input("Enter your choice (1 , 2 , 3): ")
    if user_choice == '1':
        choice_name = 'Rock'
        print("You selected", user_choice, "So you play as", choice_name)
    elif user_choice == '2':
        choice_name = 'Paper'
        print("You selected", user_choice, "So you play as", choice_name)
    elif user_choice == '3':
        choice_name = 'Scissor'
        print("You selected", user_choice, "So you play as", choice_name)
    else:
        print("Please enter a valid choice (1, 2, or 3).")
        continue

    computer_choice = random.randint(1, 3)
    while computer_choice==user_choice:
        computer_choice=random.randint(1,3)

    if computer_choice == 1:
        comp_name = "Rock"
    elif computer_choice == 2:
        comp_name = "Paper"
    elif computer_choice == 3:
        comp_name = "Scissor"

    print("Computer selected", comp_name)

    if user_choice == str(computer_choice):
        print("You both chose the same thing")
        print("This round ends in a tie")
    elif (user_choice == '1' and computer_choice == 2) or (user_choice == '2' and computer_choice == 3) or (user_choice == '3' and computer_choice == 1):
        print(f"You chose {choice_name}, Computer chose {comp_name}")
        print(f"{comp_name} vs {choice_name} -> Computer won this round")
        machine_score += 1
    else:
        print(f"You chose {choice_name}, Computer chose {comp_name}")
        print(f"{choice_name} vs {comp_name} -> You won this round")
        user_score += 1

    print(f"Your score = {user_score}")
    print(f"Computer score = {machine_score}")

    if user_score > machine_score:
        print("Hurray, you won this match!")
    elif machine_score > user_score:
        print("Computer won this match...")
    else:
        print("Oops! You both end in a tie")

    ans = input("Do you want to continue the game (Yes/No): ").lower()
    if ans == "no":
        break

print("Thanks for playing! See You Again")
#Output
# Welcome you all! Let's play Rock, Paper, Scissor with Computer
# Do you need help to understand this game or not (Yes, No)= Yes
# Rock vs Paper -> Paper Wins
# Rock vs Scissor -> Rock Wins
# Scissor vs Paper -> Scissor Wins
# Hope you understand the game
# Enter your choice (1 , 2 , 3): 1
# You selected 1 So you play as Rock
# Computer selected Rock
# You both chose the same thing
# This round ends in a tie
# Your score = 0
# Computer score = 0
# Oops! You both end in a tie
# Do you want to continue the game (Yes/No): Yes
# Enter your choice (1 , 2 , 3): 3
# You selected 3 So you play as Scissor
# Computer selected Rock
# You chose Scissor, Computer chose Rock
# Rock vs Scissor -> Computer won this round
# Your score = 0
# Computer score = 1
# Computer won this match...
# Do you want to continue the game (Yes/No): No
# Thanks for playing! See You Again

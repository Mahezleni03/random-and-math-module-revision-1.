import random

while True:
    user_action = input("Choose any one option : 'rock', 'paper', 'scissors'")
    possible_action = ["rock", "paper", "scissors"]
    computer_action = random.choice({possible_action})

    print(f"\n You choose{user_action}, computer choose{computer_action}")

if user_action == computer_action:
    print("It is a TIE")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors!You WIN!")
    else:
        print("Paper covers rock.You LOSE :(")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock!You WIN!")
    else:
        print("Scissors cuts paper.You LOSE :(")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper!You WIN!")
    else:
        print("Rock smashes scissors.You LOSE :(")
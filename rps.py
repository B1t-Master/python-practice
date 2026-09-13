import sys
import random
import re
from enum import Enum
print("")


class RPS (Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def get_computer_choice():
    return (random.choice("123"))


def determine_winner(player_selection, computer_choice):
    player_selection = int(player_selection)
    computer_choice = int(computer_choice)
    if player_selection == computer_choice+1:
        print("You win!" + " 🐍 chose: " +
              str(RPS(computer_choice)).replace("RPS.", ""))

    elif computer_choice == player_selection+1:
        print("You lose!" + " 🐍 chose: " +
              str(RPS(computer_choice)).replace("RPS.", ""))

    elif player_selection == computer_choice+2:
        print("You lose!" + " 🐍 chose: " +
              str(RPS(computer_choice)).replace("RPS.", ""))

    elif computer_choice == player_selection+2:
        print("You win!" + " 🐍 chose: " +
              str(RPS(computer_choice)).replace("RPS.", ""))

    else:
        print("its a draw")


player_selection = input(
    'please enter your choice:\n 1.For rock \n 2.For paper\n 3.For scissors\n q.To quit\n')

while (player_selection):
    if (not re.search("[123q]", player_selection)):
        print("wrong value please select again")
        player_selection = input(
            'please enter your choice\n 1.For rock \n 2.For paper\n 3.For scissors\n q.To quit\n')

    if player_selection == "q":
        sys.exit("Thank you for playing")
    determine_winner(player_selection, get_computer_choice())
    player_selection = input(
        'please enter your choice\n 1.For rock \n 2.For paper\n 3.For scissors\n q.To quit\n')

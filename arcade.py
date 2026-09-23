import argparse
import rps
import guess_number
from sys import exit


if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser(
        description="This is the guess my number game")

    parser.add_argument("-n", "--name", metavar="name", required=True,
                        help="Your name for a personalized game experiece")

    args = parser.parse_args()
    # message = f"{args.name}"
    # print(message)
    print(f"Welcome to the arcade 👾 {args.name}")

    def start_arcade():
        print("Which game would you like to play\n1.Rock Paper Scissor\n2.The guessing game\nq.To exit the arcade\n")
        user_choice = input()
        if user_choice not in ["1", "2", "q"]:
            print("You chose and invalid choice try again!\n")
            start_arcade()
        while (user_choice):
            # return play_round()
            if user_choice == "1":
                play_game = rps.play_game()
            if user_choice == "2":
                play_game = guess_number.play_game(args.name)
            if user_choice == "q":
                exit("\nThank you for playing with us, come again next time")
            play_game()
            print(f"")

            print(f"Welcome to back the arcade 👾 {args.name}")

            start_arcade()

    # arcade = play_arcade()
    # arcade()
    start_arcade()

from random import choice


def play_game(name="player 1"):
    win_percentage = player_wins = total_rounds = 0
    print(f"Welcome {name} to the guessing game 🍀\n")

    def calc_win_percentage():
        nonlocal win_percentage
        nonlocal player_wins
        nonlocal total_rounds

        win_percentage = f"{player_wins/total_rounds:.2%}"

        return win_percentage

    def get_computer_choice():
        computer_choice = choice("1,2,3")
        return computer_choice

    def get_player_choice():
        print(
            "Guess which number I have in mind 1, 2 or 3...\nq - quit ")
        return input()

        # return player_choice

    def is_player_choice_valid(player_choice):
        if player_choice not in ["1", "2", "3", "q"]:
            print("You chose and invalid choice try again!\n")
            return play_round()

    def play_round(player_choice=True):
        nonlocal name
        nonlocal player_wins
        nonlocal total_rounds
        # player_choice = get_player_choice()

        # is_player_choice_valid(player_choice)

        while (player_choice):
            player_choice = get_player_choice()
            # print(player_choice)
            is_player_choice_valid(player_choice)
            if player_choice == "q":
                print("Thank you for playing the guessing game")
                break
            total_rounds += 1

            if player_choice == get_computer_choice():
                player_wins += 1
                print(
                    f"\n{name} wins  \nYou have won that round 🎉\nyour current win percentage is {calc_win_percentage()} \n")
            else:
                print(
                    f"\ncomputer wins 🐍 \nSorry you lost that round 😭\nyour current win percentage is {calc_win_percentage()} \n")

    return play_round

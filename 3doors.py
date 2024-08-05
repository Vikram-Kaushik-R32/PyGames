import random


def monty_hall_game():
    """
    Play the Monty Hall game where the user can choose to stick or switch.
    """
    print("Welcome to the Monty Hall Game!")
    doors = [0, 0, 1]  # 0 = goat, 1 = car
    random.shuffle(doors)

    print("There are 3 doors. Behind one door is a car, and behind the other two are goats.")
    print("Pick a door (1, 2, or 3):")
    player_choice = int(input()) - 1

    # Host reveals a door with a goat
    host_options = [i for i in range(3) if i != player_choice and doors[i] == 0]
    host_reveal = random.choice(host_options)

    print(f"The host opens door {host_reveal + 1} to reveal a goat.")

    # Ask the player if they want to switch
    print("Do you want to switch to the remaining unopened door? (yes/no)")
    switch = input().lower() == 'yes'

    if switch:
        player_choice = [i for i in range(3) if i != player_choice and i != host_reveal][0]

    print(f"You have chosen door {player_choice + 1}.")

    if doors[player_choice] == 1:
        print("Congratulations! You won the car!")
    else:
        print("Sorry, you got a goat. Better luck next time!")


def main():
    play_again = 'yes'
    while play_again.lower() == 'yes':
        monty_hall_game()
        print("Do you want to play again? (yes/no)")
        play_again = input()


if __name__ == "__main__":
    main()

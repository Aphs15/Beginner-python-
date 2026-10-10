import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]

    #define what beats what
    beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

    player_score = 0
    computer_score = 0

    while player_score < 3 and computer_score < 3:
        player = input("Make your choice rock/paper/scissors (or 'quit'): ").lower()

        if player == "quit":
            break
        if player not in choices:
            print("Invalid choice. Try again.")
            continue

        computer = random.choice(choices)
        print(f"Computer chose: {computer}")

        if player == computer:
            print("Tie")
        elif beats[player] == computer:
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round.")
            computer_score += 1

        print(f"Score - You: {player_score} | Computer: {computer_score}")

    if player_score == 3:
        print("You won the game!")
    elif computer_score == 3:
        print("Computer won the game.")


rock_paper_scissors()

import random

def guessing_game():
    secret = random.randint(1, 100)
    attempts = 0

    print("I'm thinking about a number between 1 and 100. Can you guess?")

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
                print("Please enter a whole number")
                continue

        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high")
        else:
            if attempts < 10:
                print(f"Your good at this You got it in {attempts} attempts")
            elif attempts >10:
                print(f"You got it in {attempts} attempts. You can do better than that common try again")
            break
                
guessing_game()

while True:
    Answer = input("Do you want to Continue? (Y/N): ").strip().upper()
    
    # 1. Catch numbers immediately
    if Answer.isdigit():
        print("Invalid input! Numbers are not allowed.\n")
        continue

    # 2. Check for exact valid answers
    if Answer in ["Y", "YES"]:
        guessing_game()
        break
    elif Answer in ["N", "NO"]:
        print("Thanks for playing!")
        break
    else:
        # This catches "Yellow", "Yikes", or random letters
        print("Invalid choice. Please type Y or N.\n")


import random

def guessing_game():
    secret = random.randint(1, 100)
    attempts = 0

    print("I'm thinking about a number between 1 and 15. Can you guess?")

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
            print(f"correct! You got it in {attempts} attempts")
            break
                
guessing_game()
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
from random import randint
from num_guess_art import logo

# This is a game where the computer will pick a number and the user has to guess what the computer's pick is
# The program will allow the user to either guess 5 or 10 times depending on the difficulty the user picks

easy_level = 10
hard_level = 5

# Check user's guess against the actual answer
def check_num(guess, answer, turns):
    """checks the answer against the guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer} 🎆")

# set difficulty
def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': \n").lower()
    if level == "easy":
        return easy_level
    else:
        return hard_level


def game():
    print(logo)

    print("Welcome to the Number Guessing Game! 🥳")
    print("I am thinking if a number between 1 and 100")
    # The computer will chose a random number between 1 and 100 to set as the answer
    answer = randint(1, 101)
    #checking if above works:
    print(answer)

    # this will call the difficulty() created above. nad determing if user has 5 or 10 tries
    turns = difficulty()

    guess = 0
    while guess != answer:
        # There will be a countdown each time the user gets it incorrectly
        print(f"You have {turns} attempts remaining to guess the number")

        # user should make a guess
        guess = int(input("Make a guess: "))

        # track the number of turns the user has left and start the count-down. call the check_num()
        turns = check_num(guess, answer, turns)
        if turns == 0:
            print("You have run out of gusses, you lose! ❌")
            return
        elif guess != answer:
            print("Guess again.")

game()
import random
def roll_dice():
    return random.randint(1,6)
def play_game():
    you_roll = roll_dice()
    comp_roll = roll_dice()
    print("your roll is", you_roll)
    print("computer's roll is", comp_roll)
    if you_roll > comp_roll:
        print("You won!")
    elif you_roll < comp_roll:
        print("Computer won!")
    else:
        print("It's a tie!")

while True:
    play_game()
    user = input("Do you want to play again? (yes/no): ").strip().lower()
    if user != "yes":
        print("Thank you for playing!")
        break
import random

while True:
    choice = input("Input your selection: [rock, paper, scissors] ")
    possibleChoices = ["rock", "paper", "scissors"]
    computerChoice = random.choice(possibleChoices)
    print(f"\nYou selected {choice}, while the computer selected {computerChoice}.\n")

    if choice == computerChoice:
        print(f"You and the computer both chose {choice}. It's a tie!")
    elif choice == "rock":
        if computerChoice == "scissors":
            print("Rock beats scissors, you win!")
        else:
            print("Paper beats rock, you lose.")
    elif choice == "paper":
        if computerChoice == "rock":
            print("Paper beats rock, you win!")
        else:
            print("Scissors beats paper, you lose.")
    elif choice == "scissors":
        if computerChoice == "paper":
            print("Scissors beats paper, you win!")
        else:
            print("Rock beats scissors, you lose.")

    play = input("Would you like to play again? (yes/no): ")
    if play.lower() != "yes":
        break
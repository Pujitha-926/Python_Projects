import random
print("Welcome to Rock-Paper-Scissors Game!")
print("Game rules are:")
print("Rock beats Scissors")
print("Scissors beats Paper")
print("Paper beats Rock")

choices=["rock","paper","scissors"]
while True:
    print("Enter your choice (rock, paper, scissors) or 'exit' to quit:")
    user_choice=input().lower()
    if user_choice=="exit":
        print("Thanks for playing! Goodbye!")
        break
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue
    computer_choice=random.choice(choices)
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)
    if user_choice==computer_choice:
        print("It's a tie!")
    elif (user_choice=="rock" and computer_choice=="scissors") or (user_choice=="scissors" and computer_choice=="paper") or (user_choice=="paper" and computer_choice=="rock"):
        print("You win!")
    else:
        print("Computer wins!")

    print("Do you want to play again? (yes/no)")
    play_again = input().lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break
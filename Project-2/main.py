import random
print("Welcome to the Number Guessing game!")
low=int(input("Enter the lower limit: "))
high=int(input("Enter the upper limit: "))
print(f"You have 5 chances to guess the number between {low} and {high}.")
number=random.randint(low,high)
chances=5
guess=0
while guess<chances:
    user_guess=int(input("Enter your guess:"))
    if user_guess<low or user_guess>high:
        print("please enter a number within the range.")
        break
    elif user_guess<number:
        print("Your guess is too low.")
    elif user_guess>number:
        print("Your guess is too high.")
    else:
        print(f"Congratulations! You guessed the number {number} correctly.")
        break
    guess+=1
    print(f"You have {chances - guess} chances left.")
    
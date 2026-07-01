import random
print("welcome to snake-water-gun game")
n=int(input("Enter the number of rounds you want to play: "))
options=['s','w','g']
rounds=1
computer_score=0
user_score=0
while rounds<=n:
    print(f"Round {rounds}:")
    try:
        player=input("Choose your option:")
    except EOFError as e:
        print(e)
        continue
    if player not in options:
        print("Invalid option.Please choose from snake,water,gun")
        continue
    computer=random.choice(options)
    if computer =='s':
        if player=='w':
            print("Computer chose snake and you chose water. Computer wins this round.")
            computer_score+=1
        elif player=='g':
            print("Computer chose snake and you chose gun. You win this round.")
            user_score+=1
    elif computer=='w':
        if player=='g':
            print("Computer chose water and you chose gun. Computer wins this round.")
            computer_score+=1
        elif player=='s':
            print("Computer chose water and you chose snake. You win this round.")
            user_score+=1
    elif computer=='g':
        if player=='s':
            print("Computer chose gun and you chose snake. Computer wins this round.")
            computer_score+=1
        elif player=='w':
            print("Computer chose gun and you chose water. You win this round.")
            user_score+=1
    if user_score>computer_score:
        print(f"You won the game with a score of {user_score} against computer's score of {computer_score}.")
    elif computer_score>user_score:
        print(f"Computer won the game with a score of {computer_score} against your score of {user_score}.")
    else:
        print(f"The game is a tie with both scoring {user_score}.")

    rounds+=1
if user_score>computer_score:
    print(f"You won the game with a score of {user_score} against computer's score of {computer_score}.")
elif computer_score>user_score:
    print(f"Computer won the game with a score of {computer_score} against your score of {user_score}.")    
else:
    print(f"The game is a tie with both scoring {user_score}.")



        
        


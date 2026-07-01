import random
name=input("Enter your name: ")
print("Hello " + name+ "! Welcome to the Word Guessing Game!")
words=['rainbow','cat','science','reverse','suspect','water','questions','gemini','examples']
word=random.choice(words)
print("Guess the characters")
guesses=''
turns=10
while turns>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char,end=" ")
        else:
            print("_",end=" ")
            failed+=1
    print()
    if failed==0:
        print("You Win")
        print("The word is: ",word)
        break
    guess=input("guess a character:").lower()
    if len(guess)!=1:
        print("Please enter a single character.")
        continue
    guesses+=guess
    if guess not in word:
        turns-=1
        print("Wrong")
        print("You have", turns, 'more guesses')
        if turns==0:
            print("You Lose")
            print("The word is: ",word)

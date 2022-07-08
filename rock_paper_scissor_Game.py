import random

l=['Rock', 'Scissor', 'Paper']

while True:
    uCount=0
    cCount=0
    usr=int(input('''
    Game Start...
    1. Yes
    2. No | Exit
                                '''))

    if usr == 1:
        for i in range(1,6):
            user=int(input('''
            1. Rock
            2. Scissor
            3. Paper
                                '''))
            if user == 1:
                uChoice="Rock"
            elif user == 2:
                uChoice="Scissor"
            elif user == 3:
                uChoice="Paper"
            cChoice=random.choice(l)
            if uChoice == cChoice :
                print("Game Draw....")
                print("User input : ",uChoice)
                print("Computer input : ",cChoice)
                cCount=cCount+1
                uCount=uCount+1
            elif (uChoice == "Rock" and cChoice == "Scissor") or (uChoice == "Scissor" and cChoice == "Paper") or (cChoice == "Paper" and cChoice == "Rock"):
                print("User Win...")
                print("User input : ",uChoice)
                print("Computer input : ",cChoice)
                uCount=uCount+1
            else:
                print("Computer Win...")
                print("User input : ",uChoice)
                print("Computer input : ",cChoice)
                cCount=cCount+1
        if uCount == cCount:
            print("*"*30)
            print("Finally Game Draw...")
            print("User Score : ",uCount)
            print("Computer Score : ",cCount)
            print("*"*30)
        elif uCount > cCount:
            print("*"*30)
            print("Finally User win the game")
            print("User Score : ",uCount)
            print("Computer Score : ",cCount)
            print("*"*30)
        else:
            print("*"*30)
            print("Finally Computer Win the game")
            print("User Score : ",uCount)
            print("Computer Score : ",cCount)
            print("*"*30)

    else:
        break
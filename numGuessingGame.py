import random


def playGame():
    score = 10
    trials = 3
    randomNumber = random.randint(1,10)

    while trials != 0:
        guessNumber = int(input("Make Your Guess: "))

        if guessNumber == randomNumber:
            trials = trials -1
            
            print(f'CORRECT! The random number is {randomNumber}')
            print(f'Your Score is {score} and you won with {trials} trials left\n')
            playAgain()
            break
        else:
            trials = trials -1
            score = score-3

            if trials == 0:
                print(f'Too Bad, you lost. The number is {randomNumber}\n')
                playAgain()
                break

            if guessNumber < randomNumber:
                print(f'Guess Higher. You have {trials} left.\n')
            else:
                print(f'Guess Lower. You have {trials} left.\n')

    
def playAgain():
    again = int(input("\nClick 1 to play again and 2 to exit: "))
    
    if again == 1:
        playGame()
    else:
        print("Bye!")
        


print(
    "Welcome to my Random Number Guessing Game.\n\nRules\n1.Guess a number from 1 to 10.\n2.You have 3 trials to get the number."
)
print(
    "3.You will get hints along the game.\n4.You score 10 for getting the number at first trial,7 at second trial and 4 at last trial."
)
print("GOODLUCK!\n\n")


start = int(input("Press 1 to start game and 2 to exit: "))
if start == 1:
    playGame()
else:
    print("Bye!")
    pass


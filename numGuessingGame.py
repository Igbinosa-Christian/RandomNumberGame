# A random number game where you have to guess between 1 and 10 for a random number. You have 3 trials to make a guess.
# 10 points for getting the number on first trial, 7 on second trial and 4 on third trial.
# You will get clues as you go.




# Import random to generate random number
import random


# Main game function
def playGame():
    score = 10
    trials = 3
    randomNumber = random.randint(1,10)

    while trials != 0:
        guessNumber = int(input("Make Your Guess: "))
        

        # If-Else block to check if user has won the game or did not get the number
        if guessNumber == randomNumber:
            trials = trials -1
            
            print(f'CORRECT! The random number is {randomNumber}')
            print(f'Your Score is {score} and you won with {trials} trial(s) left\n')
            playAgain()
            break
        else:
            trials = trials -1
            score = score-3

            
            # If block to check if user has exhausted trials
            if trials == 0:
                print(f'Too Bad, you lost. The number is {randomNumber}\n')
                playAgain()
                break
            
            # If block to give user clue of the random number(Higher/Lower)
            if guessNumber < randomNumber:
                print(f'Guess Higher. You have {trials} trial(s) left.\n')
            else:
                print(f'Guess Lower. You have {trials} trial(s) left.\n')
# End of Main Game Function

    
# Function to ask if user wants to play again    
def playAgain():
    again = int(input("\nClick 1 to play again and 2 to exit: "))
    
    if again == 1:
        playGame()
    else:
        print("Bye!")
# End of function      


# Rules beofre starting game
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


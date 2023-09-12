##imports
import random
import math

##Ask user for limits and generate random number
lowerLim = int(input("Please enter the lower limit: "))
upperLim = int(input("Please enter the upper limit: "))
randomNum = random.randint(lowerLim, upperLim)

##Calculate number of guesses allowed
noGuessAllow = round(math.log(upperLim - lowerLim + 1, 2))
print("\n\tYou've only got ", noGuessAllow, " chances to guess the integer!\n")

##Initializing the number of guesses taken
guessCount = 0
 
##Loop for number of guesses allowed, or until correct number guessed
while guessCount <= noGuessAllow:
    guessCount += 1
 
 # If Guessing is more than required guesses,
# shows this output.
    if guessCount > noGuessAllow:
        print("\nThe number is %d" % randomNum)
        print("\tBetter Luck Next time!")
 
    ##taking guessing number as input
    guess = int(input("Guess a number: "))
    #if guess(int.
 
    # Condition testing
    if randomNum == guess:
        if guessCount == 1:
            print("Congratulations! You got it on your first try!")
        elif guessCount > 1 and guessCount < noGuessAllow:
            print("Congratulations! You got it in ", guessCount, " attempts!")
        # Once guessed, loop will break
        break
    elif randomNum > guess:
        print("Too Low!")
    elif randomNum < guess:
        print("Too High!")
 


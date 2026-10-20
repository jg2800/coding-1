# loop - a loop is a construct ( special function ) that repeats itself.
# In programming, a loop allows to repeat code instructions.

# there are teo types of loops: For loop and while loop 

# while loop - a type of loop where so long as a condition is equal.
# to true it will keep it running forever.

# the keyboard is while --> do while

# syntax 
num = 4 
while 2+2 == num # Condition ---> operation - must be TRUE 
       print ("the program is running ")
       num = int(input(" please type in a number: "))

    # while loops will ALWAYS  run unless you change the contitions!
    # we can do this by writting instructions to manually change it.
     
     # def guessing():
        correctAnswer = 12 
        attempts = 0
        userGuess = input(" please guess a number between 1 and 50 ")
        print("GUESSING GAME HAS STARTED")

       While userGuess != correctAnswer: 
           print("Incorrect. Please try again...")

       guessingGame
       while userGuess == correctAnswer:
    print("Incorrect. Please try again...")
    attempts +=1 
    print("Guess attempts: " + str(attempts))
    userguess = input ("please guess a number between 1 and 50.")

print("Congrats! you guessed the right number!")
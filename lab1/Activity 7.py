# Generate a random number between 1 and 9 Ask the user to guess the number, 
#then tell them whether they guessed too low, too high, or exactly right
#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken, and when the game ends, print this out

import random
# Awroken
MINIMUM = 1
MAXIMUM = 9
NUMBER = random.randint(MINIMUM, MAXIMUM)
GUESS = None
ANOTHER = None
TRY = 0
RUNNING = True
print("Alright...")
while RUNNING:
 GUESS = input("What is your lucky number? ")
 if int(GUESS) < NUMBER:
     print("Wrong, too low.")
 elif int(GUESS) > NUMBER:
     print("Wrong, too high.")
 elif GUESS.lower() == "exit":
     print("Better luck next time.")
 elif int(GUESS) == NUMBER:
     print("Yes, that's the one, %s." % str(NUMBER))
 if TRY < 2:
     print("Impressive, only %s tries." % str(TRY))
 elif TRY > 2 and TRY < 10:
     print("Pretty good, %s tries." % str(TRY))
 else:
     print("Bad, %s tries." % str(TRY))
 RUNNING = False
 TRY += 1


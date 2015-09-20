#! /usr/bin/env python

# Import Required Modules
import os
import random

#Define main() Function
def main():

    # Print Welcome Messages
    print "Welcome to Guess the Number!"
    print "\nI'm thinking of a number from 0 to 100, guess what it is.\n"

    # Select a Random Number from 0 to 100
    num = random.randrange(100)

    # Create a Variable 'guess' to Store Guessed Value
    guess = ""

    # Loop Until Guess is Correct
    while guess != num:

        # Get Guessed Value from User
        guess = int(raw_input("Take a guess: "))

        #If Guessed Value is Lesser Than Number
        if guess < num:
            print "Guess higher next time\n"

        #If Guessed Value is Higher Than Number
        elif guess > num:
            print "Guess lower next time\n"

    # Congratulate User once Loop is Broken and Number is Found
    print "Congratulations, you guessed it right!"

    # Wait for User Input Before Closing
    raw_input()

# Call main() Function
main()  

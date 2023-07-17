#!/usr/bin/env python3

"""
This is a simple dice game where the player will bet money and guess the dice roll
The player can't bet more than there current holdings
Once the players loses all their money the game ends
This game also features colored text output and a simple animation
"""

import random
import time

class colors:
    """Colors class:
    Reset all colors with colors.reset
    Two subclasses fg for foreground and bg for background.
    Use as colors.subclass.colorname.
    i.e. colors.fg.red or colors.bg.green
    Also, the generic bold, disable, underline, reverse, strikethrough,
    and invisible work with the main class
    i.e. colors.bold
    """
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'

def main():

    #print a greeting and simple directions to the game
    print(f"\n{colors.fg.green}+++ Welcome to the Guess the Dice Game! +++{colors.reset}")
    print(f"\n{colors.fg.yellow}---Directions---{colors.reset}")
    print(f"{colors.fg.cyan}You will start with $100 and will be asked to place a bet.")
    print(f"A single dice will be rolled and you will have a chance to guess the number rolled.")
    print(f"You can't bet more than your holdings and the game ends when you have no money left.{colors.reset}")
    
    #start the game with $100
    money = int(100)
    #loop until the player runs out of money
    while money > 0:
        
        #print current holdings
        print(f"\n\nCurrent holdings is {colors.fg.green}${money}{colors.reset}")
        
        #ask for bet amount and check it doesn't exceed current holdings
        while True:
            bet = int(input(f"\nPlace your bet: {colors.fg.green}$"))
            if bet > money:
                print(f"\n{colors.fg.red}You cannot bet more than what you have...{colors.reset}")
                continue
            else:
                break

        #get the player's guess and save to guess
        while True:
            guess = int(input(f"{colors.reset}\nEnter a number 1 - 6: "))
            if guess > 6 or guess <= 0:
                print(f"\n{colors.fg.red}You entered in invalid number...{colors.reset}")
                continue
            else:
                break

        print(f"\n")
        
        #animate rolling the dice output
        for _ in range(4):
            for x in range (4): # three dots
                string = "Rolling the dice" + "." * x + "   "
                print(f"{string}", end="\r")
                time.sleep(.25)

        #generate a random number (1-6) for the dice roll and print
        number = random.randrange(6) + 1
        print(f"\n\nThe dice rolled was a {number}")
        
        #check the roll dice with the guess and make money adjusts accordingly
        if guess == number:
            print(f"\n\n{colors.fg.green}Your guess is right!{colors.reset}")
            print(f"Congrats you won {colors.fg.green}${bet}{colors.reset}!")
            money = money + bet           
        else:
            print(f"\n\n{colors.fg.red}Sorry but you guessed wrong!{colors.reset}")
            money = money - bet
    
    #game has ended, the player has no more moeny
    print(f"\n\n{colors.fg.yellow}---Game Over---{colors.reset}")
    print(f"{colors.fg.cyan}You lost all your money!{colors.reset}\n")

if __name__ == "__main__":
    main()
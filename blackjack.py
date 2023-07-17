#!/usr/bin/env python3

"""
This is a Black Jack game where the player can choose to start with
a max of $1,000,000 dollars to bet with.
The player can't bet more than their current chip count
Once the player loses all their money the game ends
This game also features colored text output
"""

import os
import random

"""
colors class:
    Reset all colors with colors.reset
    Two subclasses fg for foreground and bg for background.
    Use as colors.subclass.colorname.
    i.e. colors.fg.red or colors.bg.green
    Also, the generic bold, disable, underline, reverse, strikethrough,
    and invisible work with the main class
    i.e. colors.bold
"""
class colors:
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

#create tuple for suits
suits = ( 'Spades', 'Clubs', 'Hearts', 'Diamonds' )

#create tuple for cards in each suit
ranks = ( 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace' )

#create a dictionary with keys to reference (same as ranks tuple) and values
values = { 'Two' : 2, 'Three' : 3, 'Four' : 4, 'Five' : 5, 'Six': 6, 
           'Seven' : 7, 'Eight' : 8, 'Nine' : 9, 'Ten' : 10, 'Jack' : 10,
           'Queen' : 10, 'King' : 10, 'Ace' : 11 }
           
#create class Card
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit

#create class Deck, with string, shuffle, and deal methods
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

#creae class Hand, with add_card method, and ace card handling
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        self.tens = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
        if card.rank == 'Ten':
            self.tens += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1 

#create class Chips, with win_bet and lose_bet methods
class Chips:
    def __init__(self):
        self.total = 0
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

#hit or stand function w/ input validation
def hit_stand(deck, dealer_hand, player_hand):
    while player_hand.value <= 21:
        answer = input(f"\nHit or Stand? Enter h or s: ")
        if answer.lower() == 'h':
            player_hand.add_card(deck.deal())
            player_hand.adjust_for_ace()
            print_player_hand(dealer_hand, player_hand)
            continue
        elif answer.lower() == 's':
            break
        else:
            print(f"{colors.fg.cyan}")
            print("Please enter a valid input!")
            print(f"{colors.reset}")
            continue
        break

#print fucntion to output the dealer and player hands
def print_hands(dealer_hand, player_hand):
    #clear the screen
    clrs()

    #print the dealer's hand
    print(f"{colors.fg.green}Dealer's Hand: {dealer_hand.value}")
    print(f"{colors.fg.yellow}", end="")
    for cards in dealer_hand.cards:
        print(f"{cards}")
    print(f"{colors.reset}")

    #print the player's hand
    print(f"{colors.fg.green}Your Hand: {player_hand.value}")
    print(f"{colors.fg.cyan}", end="")    
    for cards in player_hand.cards:
        print(f"{cards}")
    print(f"{colors.reset}")

def print_player_hand(dealer_hand, player_hand):
    #clear the screen
    clrs()

    #Show dealer card to player (first one hidden)
    print(f"{colors.fg.green}Dealer's Hand:{colors.fg.yellow}")
    print(f"***Card Hidden***")
    print(f"{dealer_hand.cards[1]}")
    print(f"{colors.fg.green}")

    #print the player's hand
    print(f"{colors.fg.green}Your Hand: {player_hand.value}")
    print(f"{colors.fg.cyan}", end="")    
    for cards in player_hand.cards:
        print(f"{cards}")
    print(f"{colors.reset}")

#simple function to clear the screen
def clrs():
    os.system('cls')
    

def main():
    
    #clear the screen
    clrs()

    #print a greeting and simple directions to the game
    print(f"{colors.fg.green}+++ Welcome to Black Jack! +++")
    print(f"{colors.fg.yellow}")
    print(f"\n---Directions---")
    print(f"{colors.fg.cyan}", end="")
    print(f"Enter how much $ to start with. (max $1,000,000)")
    print(f"You and the dealer will be dealt 2 cards each")
    print(f"The rules are to TODO!!!")
    print(f"{colors.reset}")
   
    #init Chips class
    chips = Chips()

    #prompt for starting chips amount and loop until amount is valid
    while True:
        try:
            chips.total = int(input(f"\nStarting Chips: {colors.fg.green}$"))
            print(f"{colors.reset}")
        except ValueError:
            print(f"{colors.fg.red}")
            print(f"Please enter a valid number!")
            print(f"{colors.reset}")
        else:
            if chips.total > 1000000:
                print(f"{colors.fg.red}")
                print(f"Max amount is $1,000,000...please re-enter amount")
                print(f"{colors.reset}")
            else:
                break

    #clear the screen
    clrs()

    #loop until the player runs out of money
    while chips.total > 0:

        #print current holdings
        print(f"Current holdings is {colors.fg.green}${chips.total}")
        print(f"{colors.reset}")

        #ask for bet amount and check it doesn't exceed current holdings
        while True:
            try:
                chips.bet = int(input(f"Place bet: {colors.fg.green}$"))
            except ValueError:
                print(f"{colors.fg.red}")
                print(f"Please enter a valid number!")
                print(f"{colors.reset}")
            else:
                if chips.bet > chips.total:
                    print(f"{colors.fg.red}")
                    print(f"You cannot bet more than ${chips.total}")
                    print(f"{colors.reset}")
                else:
                    break

        #clear the screen
        clrs()
        
        #initialize full deck from class Deck
        deck = Deck()

        #shuffle the full deck with method shuffle
        deck.shuffle()

        #initialize player and dealer hands with class Hand
        player_hand = Hand()
        dealer_hand = Hand()

        #deal 2 cards (alternating) to player and dealer
        #with methods deal (class Deck) & add_card (class Hand)
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        print_player_hand(dealer_hand, player_hand)
        
        #TODO
        if dealer_hand.aces + dealer_hand.tens != 2:
            if player_hand.aces + player_hand.tens == 2:
                print_hands(dealer_hand, player_hand)
                print(f"Player has a Black Jack!\n")
                chips.win_bet()

        if player_hand.aces + player_hand.tens < 2:
            hit_stand(deck, dealer_hand, player_hand)
            print_hands(dealer_hand, player_hand)
            while dealer_hand.value < 17:
                dealer_hand.add_card(deck.deal())
                dealer_hand.adjust_for_ace()
            if player_hand.value > 21:
                print_player_hand(dealer_hand, player_hand)
                print(f"{colors.fg.red}You busted...You lose the hand!")
                print(f"{colors.reset}")
                chips.lose_bet()
            elif dealer_hand.value > 21:
                print_hands(dealer_hand, player_hand)
                print(f"{colors.fg.green}Dealer busts...You win the hand!")
                print(f"{colors.reset}")
                chips.win_bet()
            elif dealer_hand.value > player_hand.value:
                print_hands(dealer_hand, player_hand)
                print(f"{colors.fg.red}Dealer wins...You lose the hand!")
                print(f"{colors.reset}")
                chips.lose_bet()
            elif dealer_hand.value < player_hand.value:
                print_hands(dealer_hand, player_hand)
                print(f"{colors.fg.green}Dealer loses...You win the hand!")
                print(f"{colors.reset}")
                chips.win_bet()
            else:
                print_hands(dealer_hand, player_hand)
                print(f"You tied the dealer...Your hand is a push.\n")

    #clear the screen
    clrs()
    
    #print end of game message
    print(f"{colors.fg.yellow}---Game Over---{colors.reset}\n")
    print(f"{colors.fg.cyan}You lost all your money!{colors.reset}\n")

if __name__ == "__main__":
    main()
# To generate random cards
import random
# To allow user input control
import pyinputplus as pyip

# The Card class definition
class Card:

    def __init__(self, suit, value, card_value):
         
        # Suit of the Card like Spades and Clubs
        self.suit = suit
 
        # Representing Value of the Card like A for Ace, K for King
        self.value = value
 
        # Score Value for the Card like 10 for King
        self.card_value = card_value

# Function to print the cards
def print_cards(cards, hidden):

    # Card shape will be randomly populated with card value and symbols
    card_shape = ""
    for card in cards:
        card_shape = card_shape + "\t ________________"
    if hidden:
        card_shape += "\t ________________"
    print(card_shape)
 
    card_shape = ""
    for card in cards:
        card_shape = card_shape + "\t|                |"
    if hidden:
        card_shape += "\t|                |"    
    print(card_shape)
 
    card_shape = ""
    for card in cards:
        if card.value == '10':
            card_shape = card_shape + "\t|  {}            |".format(card.value)
        else:
            card_shape = card_shape + "\t|  {}             |".format(card.value)  
    if hidden:
        card_shape += "\t|                |"    
    print(card_shape)
 
    card_shape = ""
    for card in cards:
        card_shape = card_shape + "\t|                |"
    if hidden:
        card_shape += "\t|      * *       |"
    print(card_shape)    
 
    card_shape = ""
    for card in cards:
        card_shape = card_shape + "\t|                |"
    if hidden:
        card_shape += "\t|    *     *     |"
    print(card_shape)    
 
    card_shape = ""
    for card in cards:
        card_shape = card_shape + "\t|                |"
    if hidden:
        card_shape += "\t|   *       *    |"
    print(card_shape)    
 
    card_shape = ""
    for card in cards:
        card_shape = card_shape + "\t|                |"
    if hidden:
        card_shape += "\t|   *       *    |"
    print(card_shape)    
 
    card_shape = ""
    for card in cards:
        card_shape = card_shape + "\t|       {}        |".format(card.suit)
    if hidden:
        card_shape += "\t|          *     |"
    print(card_shape)    
 
    card_shape = ""
    for card in cards:
        card_shape = card_shape + "\t|                |"
    if hidden:
        card_shape += "\t|         *      |"
    print(card_shape)    
 
    card_shape = ""
    for card in cards:
        card_shape = card_shape + "\t|                |"
    if hidden:
        card_shape += "\t|        *       |"
    print(card_shape)
 
    card_shape = ""
    for card in cards:
        card_shape = card_shape + "\t|                |"
    if hidden:
        card_shape += "\t|                |"
    print(card_shape)
 
    card_shape = ""
    for card in cards:
        card_shape = card_shape + "\t|                |"
    if hidden:
        card_shape += "\t|                |"
    print(card_shape)    
 
    card_shape = ""
    for card in cards:
        if card.value == '10':
            card_shape = card_shape + "\t|            {}  |".format(card.value)
        else:
            card_shape = card_shape + "\t|            {}   |".format(card.value)
    if hidden:
        card_shape += "\t|        *       |"        
    print(card_shape)    
         
    card_shape = ""
    for card in cards:
        card_shape = card_shape + "\t|________________|"
    if hidden:
        card_shape += "\t|________________|"
    print(card_shape)        
 
    print()

# Function for a single game of blackjack
def blackjack_game(deck):

    # Game title with light green color code
    print("""\033[92m
.-..-. _  .-.                 .--.  .-.                .-.   .--.
: :; ::_;.' `.               : .--'.' `.               : :  :_,. :
:    :.-.`. .'   .--. .--.   `. `. `. .'.--.  ,-.,-. .-' :    ,','
: :: :: : : :   ' .; :: ..'   _`, : : :' .; ; : ,. :' .; :   :_;
:_;:_;:_; :_;   `.__.':_;    `.__.' :_;`.__,_;:_;:_;`.__.'   :_;
    \033[0m""")

# Loop to check user input and avoid blank selections. Numbers are allowed as user can utilise them for a nickname.
    while True:
        player1 = input("What is your name, superstar? ")

        if player1 == '':
            print("Username is empty, please select a name")

        elif player1 != '':
            break
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

    # Welcome message
    print("Welcome {}! Let's play! ".format(player1.upper()))
    print("-"*40)
    print("\033[92mWELCOME TO THE BLACKJACK TABLE\033[0m")
    print("-"*40)

    # User input validation for drink selection
    drink = pyip.inputYesNo(prompt="Would you like a drink? (Y/N) ")
    
    # In case user selected Yes in the previous input
    if drink == "yes":
        drink_choice = pyip.inputNum(prompt="What kind of drink would you like? eg.(1,2,3)\n 1. Beer  2. Wine  3. Cocktail   ", min=1, lessThan=4)

        # Beer drink choice
        if drink_choice == 1:
            print("""\033[93m
         .   *   ..  . *  *
       *  * @()Ooc()*   o  .
           (Q@*0CG*O()  ___
          |\_________/|/ _ \'
          |  |  |  |  | / | |
          |  |  |  |  | | | |
          |  |  |  |  | | | |
          |  |  |  |  | | | |
          |  |  |  |  | | | |
          |  |  |  |  | \_| |
          |  |  |  |  |\___/  
          |\_|__|__|_/|
           \_________/
There you are! Enjoy your beer!\n
The bartenders are efficient around here.
    \033[0m""")
        
        # Wine drink choice
        if drink_choice == 2:
            print("""\033[35m
               __
              [__]
              |  |
              |  |
              |  |
              |  |
              |  |
 ,----.      /`-. \'
(      )    /-._|  \'
|`----'|   |        |
\      /   |`-...   |
 `.  ,'    |'` . |  |
   ||      |`,'- |  |
 ,-||-.    |`-...|  |
(  ''  )   |        | 
 `----'     `-....-' 
There you are! Enjoy your wine!\n
The bartenders are efficient around here.
    \033[0m""")

        # Cocktail drink choice
        if drink_choice == 3:
            print('''\033[96m        
         \ 
   .\"""""""""-.
   \`\-------'`/
    \ \__ o . /
     \/  \  o/
      \__/. /
       \_ _/
         Y
         |
         |
     _.-' '-._
    `---------`
There you are! Enjoy your cocktail!\n
The bartenders are efficient around here.
        \033[0m''')

    print("-"*40)

    # User input validation for rules selection
    rules = pyip.inputYesNo(prompt="Do you know how to play? (Y/N) ")

    # In case user selected No in the previous input
    if rules == "no":
        print("Okay! The rules are simple. You and the dealer will receive two cards in your hand. \n"
              "Your goal is to beat the dealer by getting closer to 21.\nIf you and the dealer have the same number, it's a tie or push \n"
              "Cards 2 - 10 counts as it's own number; jacks, queens, and kings counts as 10 each, and aces can count\n"
              "as either 1 or 11. You can draw up to four cards at this table.")
        print("-"*40)
        print("Let's begin blackjack!")
        print("-"*40)
    else:
        print("Let's begin blackjack!")
        print("-"*40)

    # Cards for both dealer and player
    player_cards = []
    dealer_cards = []
 
    # Scores for both dealer and player
    player_score = 0
    dealer_score = 0

    # Initial hand for player and dealer
    while len(player_cards) < 2:

        # Randomly dealing a card
        player_card = random.choice(deck)
        player_cards.append(player_card)
        deck.remove(player_card)

        # Updating the player score
        player_score += player_card.card_value

        # In case both the cards are Ace, make the first ace value as 1 
        if len(player_cards) == 2:
            if player_cards[0].card_value == 11 and player_cards[1].card_value == 11:
                player_cards[0].card_value = 1
                player_score -= 10

        # Print player cards and score      
        print("{}'S CARDS: ".format(player1.upper()))
        print_cards(player_cards, False)
        print("{}'S SCORE = ".format(player1.upper()), player_score)

        input()

        # Randomly dealing a card
        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)
 
        # Updating the dealer score
        dealer_score += dealer_card.card_value

        # Print dealer cards and score, keeping in mind to hide the second card and score
        print("DEALER CARDS: ")
        if len(dealer_cards) == 1:
            print_cards(dealer_cards, False)
            print("DEALER SCORE = ", dealer_score)
        else:
            print_cards(dealer_cards[:-1], True)    
            print("DEALER SCORE = ", dealer_score - dealer_cards[-1].card_value)

        # In case both the cards are Ace, make the second ace value as 1 
        if len(dealer_cards) == 2:
            if dealer_cards[0].card_value == 11 and dealer_cards[1].card_value == 11:
                dealer_cards[1].card_value = 1
                dealer_score -= 10
 
        input()

    # Player gets a blackjack   
    if player_score == 21:
        print("{} HAS A BLACKJACK!!!!".format(player1.upper()))
        print("{} WINS!!!!".format(player1.upper()))

        # User input validation for another game question
        anothergame = pyip.inputYesNo(prompt="Want to try another round?(Y/N) ")
        if anothergame == "no":
            print("Thanks for playing! Come back for free drinks anytime!")
            quit()

        elif anothergame == "yes":
            blackjack_game(deck)

    # Print dealer and player cards
    print("DEALER CARDS: ")
    print_cards(dealer_cards[:-1], True)
    print("DEALER SCORE = ", dealer_score - dealer_cards[-1].card_value)

    print() 
 
    print("{}'S CARDS: ".format(player1.upper()))
    print_cards(player_cards, False)
    print("{}'S SCORE = ".format(player1.upper()), player_score)

    # Managing the player moves
    while player_score < 21:
        choice = input("Enter H to Hit or S to Stand : ")
 
        # Sanity checks for player's choice
        if len(choice) != 1 or (choice.upper() != 'H' and choice.upper() != 'S'):
            print("Wrong choice!! Try Again")

        # If player decides to HIT
        if choice.upper() == 'H':
 
            # Dealing a new card
            player_card = random.choice(deck)
            player_cards.append(player_card)
            deck.remove(player_card)
 
            # Updating player score
            player_score += player_card.card_value

            # Updating player score in case player's card have ace in them
            ace_card = 0
            while player_score > 21 and ace_card < len(player_cards):
                if player_cards[ace_card].card_value == 11:
                    player_cards[ace_card].card_value = 1
                    player_score -= 10
                    ace_card += 1
                else:
                    ace_card += 1 
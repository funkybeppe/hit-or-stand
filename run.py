# To generate random cards
import random
# To allow user input control
import pyinputplus as pyip

# The definition for Card class
class Card:

    def __init__(self, suit, value, card_value):
         
        # Suit of the Card 
        self.suit = suit
 
        # Representing Value of the Card 
        self.value = value
 
        # Score Value for the Card 
        self.card_value = card_value

# Function that prints a sequence of lines populated by the card value and shape
def print_cards(cards, hidden):

    # Card shape will be randomly populated with card value and symbols
    card_shape = ""
    for card in cards:
        card_shape = card_shape + " _____________ "
    if hidden:
        card_shape += " _____________ "
    print(card_shape)
 
    card_shape = ""
    for card in cards:
        card_shape = card_shape + "|             |"
    if hidden:
        card_shape += "|             |"    
    print(card_shape)
 
    card_shape = ""
    for card in cards:
        if card.value == '10':
            card_shape = card_shape + "| {}          |".format(card.value)
        else:
            card_shape = card_shape + "| {}           |".format(card.value)  
    if hidden:
        card_shape += "|░░░░░░░░░░░░░|"    
    print(card_shape)
 
    card_shape = ""
    for card in cards:
        card_shape = card_shape + "|             |"
    if hidden:
        card_shape += "|░░░░░░░░░░░░░|"
    print(card_shape)    
 
    card_shape = ""
    for card in cards:
        card_shape = card_shape + "|             |"
    if hidden:
        card_shape += "|░░░░░░░░░░░░░|"
    print(card_shape)    
 
    card_shape = ""
    for card in cards:
        card_shape = card_shape + "|             |"
    if hidden:
        card_shape += "|░░░░░░░░░░░░░|"
    print(card_shape)    
 
    card_shape = ""
    for card in cards:
        card_shape = card_shape + "|      {}      |".format(card.suit)
    if hidden:
        card_shape += "|░░░░░░░░░░░░░|"
    print(card_shape)    
 
    card_shape = ""
    for card in cards:
        card_shape = card_shape + "|             |"
    if hidden:
        card_shape += "|░░░░░░░░░░░░░|"
    print(card_shape)    
 
    card_shape = ""
    for card in cards:
        card_shape = card_shape + "|             |"
    if hidden:
        card_shape += "|░░░░░░░░░░░░░|"
    print(card_shape)
 
    card_shape = ""
    for card in cards:
        card_shape = card_shape + "|             |"
    if hidden:
        card_shape += "|░░░░░░░░░░░░░|"
    print(card_shape)

    card_shape = ""
    for card in cards:
        if card.value == '10':
            card_shape = card_shape + "|          {} |".format(card.value)
        else:
            card_shape = card_shape + "|           {} |".format(card.value)
    if hidden:
        card_shape += "|░░░░░░░░░░░░░|"        
    print(card_shape)    
         
    card_shape = ""
    for card in cards:
        card_shape = card_shape + "|_____________|"
    if hidden:
        card_shape += "|_____________|"
    print(card_shape)        
 
    print()

# Main function for a single game
def game(deck):

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
        player1 = input("What is your name, superstar?\n ")

        if player1 == '':
            print("Username is empty, please select a name")

        elif player1 != '':
            break

    # Welcome message
    print("Welcome {}! Let's play! ".format(player1.upper()))
    print("-"*50)
    print("\033[92mWELCOME TO THE BLACKJACK TABLE\033[0m")
    print("-"*50)

    # User input validation for drink selection
    drink = pyip.inputYesNo(prompt="Would you like a drink? (Y/N)\n ")
    
    # In case user selected Yes in the previous input
    if drink == "yes":
        drink_choice = pyip.inputNum(prompt="What kind of drink would you like? eg.(1,2,3)\n 1. Beer  2. Wine  3. Cocktail\n  ", min=1, lessThan=4)

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
            print("""\033[95m
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

    print("-"*50)

    # User input validation for rules selection
    rules = pyip.inputYesNo(prompt="Do you know how to play? (Y/N)\n ")

    # In case user selected No in the previous input
    if rules == "no":
        print("Okay! The rules are simple.\nYou and the dealer will receive two cards in your hand.\n"
              "Your goal is to beat the dealer by getting closer to 21.\nIf you and the dealer have the same number, it's a tie or push.\n"
              "Cards 2 - 10 counts as it's own number.\nJacks, queens, and kings counts as 10 each.\nAces can count "
              "as either 1 or 11.\nYou can draw up to four cards at this table.")
        print("-"*50)
        print("Let's play blackjack!")
        print("-"*50)
    else:
        print("Let's play blackjack!")
        print("-"*50)

    # Dealer and player cards
    player_cards = []
    dealer_cards = []
 
    # Dealer and player scores
    player_score = 0
    dealer_score = 0

    # First hand for dealer and player
    while len(player_cards) < 2:

        # Random card deal
        player_card = random.choice(deck)
        player_cards.append(player_card)
        deck.remove(player_card)

        # Player score update
        player_score += player_card.card_value

        # If both cards are Ace, make the first ace value as 1
        if len(player_cards) == 2:
            if player_cards[0].card_value == 11 and player_cards[1].card_value == 11:
                player_cards[0].card_value = 1
                player_score -= 10

        # Print player cards and score      
        print("         ==== {}'S CARDS ====         ".format(player1.upper()))
        print_cards(player_cards, False)
        print("{}'S SCORE ---->  ".format(player1.upper()), player_score)

        input()

        # Random card deal
        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)
 
        # Update dealer score
        dealer_score += dealer_card.card_value

        # Print dealer cards and score, second card is hidden and score too
        print("         ==== DEALER CARDS ====         ")
        if len(dealer_cards) == 1:
            print_cards(dealer_cards, False)
            print("DEALER SCORE ---->  ", dealer_score)
        else:
            print_cards(dealer_cards[:-1], True)    
            print("DEALER SCORE ---->  ", dealer_score - dealer_cards[-1].card_value)

        # If both cards are Ace, make the first ace value as 1
        if len(dealer_cards) == 2:
            if dealer_cards[0].card_value == 11 and dealer_cards[1].card_value == 11:
                dealer_cards[1].card_value = 1
                dealer_score -= 10
 
        input()

    # Player has blackjack 
    if player_score == 21:
        print("{} HAS BLACKJACK!!".format(player1.upper()))
        print("{} WINS!!".format(player1.upper()))

        # User input validation for another game question
        anothergame = pyip.inputYesNo(prompt="Want to try another round?(Y/N)\n ")
        if anothergame == "no":
            print("Thanks for playing! Come back for free drinks anytime!")
            quit()

        elif anothergame == "yes":
            game(deck)

    # Print player and dealer cards
    print("         ==== DEALER CARDS ====         ")
    print_cards(dealer_cards[:-1], True)
    print("DEALER SCORE ---->  ", dealer_score - dealer_cards[-1].card_value)

    print() 
 
    print("         ==== {}'S CARDS ====         ".format(player1.upper()))
    print_cards(player_cards, False)
    print("{}'S SCORE ---->  ".format(player1.upper()), player_score)

    # Player moves
    while player_score < 21:
        choice = input("Enter H to hit or S to stand :\n ")
 
        #  Player's choice
        if len(choice) != 1 or (choice.upper() != 'H' and choice.upper() != 'S'):
            print("Wrong choice! Try Again")

        # If player hits
        if choice.upper() == 'H':
 
            # Deal new card
            player_card = random.choice(deck)
            player_cards.append(player_card)
            deck.remove(player_card)
 
            # Update player score
            player_score += player_card.card_value

            # Update player score in case player has an ace in his cards
            ace_card = 0
            while player_score > 21 and ace_card < len(player_cards):
                if player_cards[ace_card].card_value == 11:
                    player_cards[ace_card].card_value = 1
                    player_score -= 10
                    ace_card += 1
                else:
                    ace_card += 1

            # Print dealer and player cards
            print("         ==== DEALER CARDS ====         ")
            print_cards(dealer_cards[:-1], True)
            print("DEALER SCORE ---->  ", dealer_score - dealer_cards[-1].card_value)
 
            print()
 
            print("         ==== {}'S CARDS ====          ".format(player1.upper()))
            print_cards(player_cards, False)
            print("{}'S SCORE ---->  ".format(player1.upper()), player_score)

        # If player stands
        if choice.upper() == 'S':
            break

    # Print dealer and player cards
    print("         ==== {}'S CARDS ====         ".format(player1.upper()))
    print_cards(player_cards, False)
    print("{}'S SCORE ---->  ".format(player1.upper()), player_score)
 
    print()
    print("DEALER IS REVEALING THE CARDS...")
 
    print("         ==== DEALER CARDS ====          ")
    print_cards(dealer_cards, False)
    print("DEALER SCORE ---->  ", dealer_score)

    # In case player has blackjack
    if player_score == 21:
        print("{} HAS A BLACKJACK!".format(player1.upper()))

        # User input validation for another game question
        anothergame = pyip.inputYesNo(prompt="Want to try another round?(Y/N)\n ")
        if anothergame == "no":
            print("Thanks for playing! Come back for free drinks anytime!")
            quit()

        elif anothergame == "yes":
            game(deck)
    
    # Player busts
    if player_score > 21:
        print("{} BUSTED! GAME OVER!!".format(player1.upper()))
        print("-"*50)

        # User input validation for another game question
        anothergame = pyip.inputYesNo(prompt="Want to try another round?(Y/N)\n ")
        if anothergame == "no":
            print("Thanks for playing! Come back for free drinks anytime!")
            quit()

        elif anothergame == "yes":
            game(deck)

    input()

    # Dealer moves
    while dealer_score < 17:
 
        print("DEALER DECIDES TO HIT...")
 
        # Deal new card for dealer
        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)

        # Update dealer's score
        dealer_score += dealer_card.card_value
 
        # Update player's score if has a ace in his cards
        ace_card = 0
        while dealer_score > 21 and ace_card < len(dealer_cards):
            if dealer_cards[ace_card].card_value == 11:
                dealer_cards[ace_card].card_value = 1
                dealer_score -= 10
                ace_card += 1
            else:
                ace_card += 1

        # Print dealer and player cards
        print("         ==== {}'S CARDS ====          ".format(player1.upper()))
        print_cards(player_cards, False)
        print("{}'S SCORE ---->  ".format(player1.upper()), player_score)
 
        print()
 
        print("         ==== DEALER CARDS ====          ")
        print_cards(dealer_cards, False)
        print("DEALER SCORE ---->  ", dealer_score)      
 
        input()

    # Dealer busts
    if dealer_score > 21:        
        print("DEALER BUSTED! YOU WIN!!") 
        print("-"*50)

        # User input validation for another game question
        anothergame = pyip.inputYesNo(prompt="Want to try another round?(Y/N)\n ")
        if anothergame == "no":
            print("Thanks for playing! Come back for free drinks anytime!")
            quit()

        elif anothergame == "yes":
            game(deck)

    # Dealer has blackjack
    if dealer_score == 21:
        print("DEALER HAS BLACKJACK! {} LOSES".format(player1.upper()))

        # User input validation for another game question
        anothergame = pyip.inputYesNo(prompt="Want to try another round?(Y/N)\n ")
        if anothergame == "no":
            print("Thanks for playing! Come back for free drinks anytime!")
            quit()

        elif anothergame == "yes":
            game(deck)

    # When game ends in a push(tie)
    if dealer_score == player_score:
        print("IT'S A TIE!!")

        # User input validation for another game question
        anothergame = pyip.inputYesNo(prompt="Want to try another round?(Y/N)\n ")
        if anothergame == "no":
            print("Thanks for playing! Come back for free drinks anytime!")
            quit()

        elif anothergame == "yes":
            game(deck)

    # Player Wins
    elif player_score > dealer_score:
        print("{} WINS!!".format(player1.upper()))

        # User input validation for another game question
        anothergame = pyip.inputYesNo(prompt="Want to try another round?(Y/N)\n ")
        if anothergame == "no":
            print("Thanks for playing! Come back for free drinks anytime!")
            quit()

        elif anothergame == "yes":
            game(deck)

    # Dealer Wins
    else:
        print("DEALER WINS!!")
        anothergame = pyip.inputYesNo(prompt="Want to try another round?(Y/N)\n ")

        # User input validation for another game question
        if anothergame == "no":
            print("Thanks for playing! Come back for free drinks anytime!")
            quit()
        elif anothergame == "yes":
            game(deck)  

if __name__ == "__main__":   
 
    # The suits kind list to populate the card shape
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
 
    # The suits value list to populate the card shape 
    suits_values = {"Hearts":"♥","Spades":"♠", "Clubs": "♣", "Diamonds": "♦"}
 
    # Card type list
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
 
    # Card value list
    cards_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
 
    # The list of cards
    deck = []
 
    # For kind of suit
    for suit in suits:
 
        # For  type of card in a suit
        for card in cards:
 
            # Add card to the deck list
            deck.append(Card(suits_values[suit], card, cards_values[card]))

    # Game function taking deck as unique parameter
    game(deck)
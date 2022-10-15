# Milestone Project 3
![Screenshot 2022-10-13 at 11 48 42](https://user-images.githubusercontent.com/105980082/195933957-80ce96a9-f0b1-44ce-a6d0-1255d4abd796.png)



## Purpose

This Website was created for the sole purpose of completing the second Milestone Project for the Code Institute's Full Stack Developer course. It was built using the knowledge gained from the Python modules. A full list of technologies used can be found in the technologies section of this document.

## Hit or Stand? Blackjack game.

Hit or Stand is a blackjack game ran in Python terminal where the user faces the CPU dealer. The gameallows users to make decisions via inputs and play the world famous game in a entertaining way.

The live link can be found here - [Hit or Stand?](https://hit-or-stand.herokuapp.com/).

![Screenshot 2022-10-14 at 18 38 22](https://user-images.githubusercontent.com/105980082/195929651-27003155-f385-4fbe-8aa8-5838768bfc89.png)

## How to play

Hit or Stand is the classic Blackjack game, you can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Blackjack).
In this version, the player enters their name, and a message will appear asking if they would like a drink.
There will be the options to see the rules in case a user is not familiar with the game.
The player will receive two cards, the score will be printed just below.
The dealer will receive two cards as well, one of those will be covered, player will be able to see only the first one and the score will be calculated based on the value of the first card.
The player now will decide either to get another card ("Hit") or to keep the cards received in the first deal ("Stand").
At this point the dealer will draw another card, the winning hand will be calculated in this way: 
  * If player's total score is greater than dealer's score, player wins;
  * If player's and dealer's scores are the same, it's a tie game ("Push");
  * If player's score is lower than dealer's score, dealer wins.

## Game logic

* Player flowchart
    * ![Screenshot 2022-10-14 at 18 14 25](https://user-images.githubusercontent.com/105980082/195945073-e58122d0-94c5-42b8-8224-781cc5f8b540.png)

* Dealer flowchart
    * ![Screenshot 2022-10-14 at 18 29 40](https://user-images.githubusercontent.com/105980082/195945126-a42fe65e-8453-4ffc-824f-43384cf94d37.png)



# User Experience Design

### First Time Visitor Goals
* As a First Time user, I want to easily understand the main purpose of the site.
* As a First Time user, I want to be able to easily understand the content displayed.
* As a First Time user, I want to be able to make decisions and expect the correct output.
* As a First Time user, I want to easily play the game and expect a score tracking system.

### Returning Visitor Goals
* As a Returning user, I want to play the game and have some fun time.
* As a Returning user, I want to beat the computer.

## Design
* I choose to implement ASCII art with colors for the logo and for drink options
* The cards are generated using ASCII art and icons representing the value
![Screenshot 2022-10-13 at 11 48 42](https://user-images.githubusercontent.com/105980082/195939116-0eb80e6c-3f05-48f3-834b-9bc99fca75fb.png)
![Screenshot 2022-10-13 at 12 07 26](https://user-images.githubusercontent.com/105980082/195939133-089be4b1-716c-47e1-9970-21f7a41c7c31.png)
![Screenshot 2022-10-13 at 11 52 24](https://user-images.githubusercontent.com/105980082/195939148-1dcec45e-8e0e-4f56-85f6-75b3c89b4597.png)
![Screenshot 2022-10-13 at 11 53 18](https://user-images.githubusercontent.com/105980082/195939170-7a6a004e-1a33-49e5-a45d-abe48d88c25d.png)

## Features

* Random card generation
    * Cards are randomly created and displayed for both player and dealer
    * The player won't be able to see dealers second card as it will be concealed
  
![Screenshot 2022-10-15 at 19 03 49](https://user-images.githubusercontent.com/105980082/196001875-e006c8b7-cf37-40b5-9877-11e88e6647fb.png)

* Play against the computer
* Accepts user inputs:
    * The username is requested to begin the game
    * Drinks are offered
    * The rules can be displayed if users has the need to read them
    ![Screenshot 2022-10-13 at 11 49 01](https://user-images.githubusercontent.com/105980082/195934364-e1679624-754b-42e5-bb80-3dca47cf6a24.png)
    ![Screenshot 2022-10-13 at 11 50 31](https://user-images.githubusercontent.com/105980082/195934550-3777cce6-808c-4163-b1f1-d763a63ff6aa.png)
    ![Screenshot 2022-10-13 at 11 52 03](https://user-images.githubusercontent.com/105980082/195934717-5e232313-d95e-4f6c-9f74-948a8f503e77.png)
    ![Screenshot 2022-10-15 at 19 03 00](https://user-images.githubusercontent.com/105980082/196001956-c69051ee-662e-481a-8cfa-4cdca010ac35.png)
* Calculates scores automatically
  * ![Screenshot 2022-10-15 at 19 03 00](https://user-images.githubusercontent.com/105980082/196001901-83c3166c-28c7-4790-99b7-fe5d2e27e96c.png)
* Announces the winner
  * ![Screenshot 2022-10-15 at 19 05 42](https://user-images.githubusercontent.com/105980082/196001908-512eb8dc-ee56-41b9-b726-7d89a21c4145.png)
* Input validation and error-checking
    * User cannot input numbers on yes/no questions
    * User must enter yes or no to yes/no questions
    * User cannot leave blank inputs
    * ![Screenshot 2022-10-13 at 11 51 22](https://user-images.githubusercontent.com/105980082/195937972-14cf03a4-d0d2-46f4-87d3-6f92774b98f2.png)
* Data is maintained in class instances

## Features to implement

* I would like to add the ability for the user to play with another player against the CPU
* A betting system with fund tracking feature
* The ability to purchase drinks using the game funds
* A more appealing graphic design

## Technologies

* Languages
    * [Python](https://www.python.org/)
      * Python language is used for the game ran in terminalqew3
    * JavaScript
      * Used to run the mock terminal
    * HTML
      * Used to define layout for mock terminal on browser
* Packages, Libraries
    * random
      * used to generate random cards
    * [PyInputPlus](https://pypi.org/project/PyInputPlus/)
      * package used to prevent wrong user input
      
* Other tools
   * [Heroku](https://heroku.com/)
      * The game is hosted in Heroku
    * [Lucidchart](https://lucid.app/)
      * The flowcharts for the game logic were designed in Lucidchart
    * [Python Lint](https://infoheap.com/python-lint-online/)
      * project's code is verified and validated in Pylint
    * [Visual Studio Code](https://code.visualstudio.com/)
      * VS Code is the Integrated Development Environment used to develop the Website.
    * [GitHub](https://github.com/)
      * GithHub is the hosting site used to store the source code for the Website and Git Pages is used for the deployment of the live site.
    * [Git](https://git-scm.com/)
      * Git is used as version control software to commit and push code to the GitHub repository where the source code is stored.


  
## Testing

### Summary 

Testing is required on Milestone Project 3 - Hit or Stand? Blackjack game.

The testing is performed on the correct inputs entered by user, random card generation and correct score calculation.

The cards should appearing next to each other, fit in the mockup terminal in Heroku and not overlap.

The live Project can be found [here](https://hit-or-stand.herokuapp.com/)

### Tests Performed
     
* Validate user inputs
* Validate card generation
* Validate score calculation
* Validate outcome check
* Validate color display
* Validate drink options display
* Validate end game functionality

### Tests Results

![Screenshot 2022-10-15 at 20 23 28](https://user-images.githubusercontent.com/105980082/196004462-3654d8a4-780c-4842-9132-b20dab70b6a3.png)


## Bugs

In the first deployment, I figured out the cards were too big to fit 4 in a row in the mockup terminal.
![Screenshot 2022-10-13 at 12 26 16](https://user-images.githubusercontent.com/105980082/195998686-7cc93573-a8cc-4e8f-8265-577337484897.png)

I decided to assign integers to the drinks selections as it was easier to control with PyinputPlus, as by assigning strings the code was not processed in a correct way.


## Validator Testing

No errors were returned when passing through Python Linter
Problems are present when the file is open on VScode, only regarding spaces and long code lines. I'm aware of these and I am satisfied these can be dismissed.

![Screenshot 2022-10-13 at 11 21 55](https://user-images.githubusercontent.com/105980082/195998995-462d8478-55f8-4ca8-a58a-963a6c91de6c.png)

 
* Accessibility

  * I confirmed that the colors used in the terminal are easy to read and accessible by running it through lighthouse in devtools.
  ![Screenshot 2022-10-14 at 22 10 15](https://user-images.githubusercontent.com/105980082/195998979-16c69868-5613-4068-a07d-8fd8acdc2447.png)



## Unfixed bugs

No unfixed bugs

# Deployment

The application was deployed to Heroku and can be accessed from the following link: https://hit-or-stand.herokuapp.com/

The steps to deploy the application to Heroku are:

1. Create a Heroku account if you don't have one.
2. In the dashboard, go to the "Apps" tab.
3. Click on the "New" button and choose "Create a new app".
4. Enter a name for the app.
5. Choose a region.
6. Click on the "Create" button.
7. Open the app you created and go to the "Settings" tab.
8. At the "Config Vars" section, click on the "Add" button and enter the following:
    * key: PORT
    * value: 8000
9. At the "Buildpacks" section, click on the "Add" button and choose:
    * Python
    * Node.js The order of the buildpacks is important.
10. After that, click on the "Deploy" tab.
11. At the "Deployment method" section, choose GitHub and connect your GitHub account.
12. Then, you need to choose the repository you want to deploy.
13. Go down to the "Manual deploy" section, choose the branch you want to deploy, and click on the "Deploy branch" button.
14. The application will be deployed to Heroku. You can access it by clicking on the "View" button.

The steps to run the application locally on your machine are:

1. The application requires you to have Python 3 installed on your machine.
    * If you are using Windows, you can download Python 3 from Python website.
    * If you are using Linux, the Python 3 installation is probably already included in your distribution, but if not, you can install it by running the following command in your terminal:
        * For Ubuntu or other Debian based distributions: sudo apt-get install python3
        * For Fedora or other Red Hat based distributions: sudo yum install python3
        * For Arch Linux based distributions: sudo pacman -S python3
        * Other installation instructions can be found here.
    * If you are using macOS, you can download Python 3 from Python website.
2. Now, you need to download the application source code from GitHub.
    * Go to the GitHub repository, click on the "Download ZIP" button, and extract the zip file's contents to the folder where you want to place the application.
    * Or use the following command to download the application source code:
        * git clone https://github.com/funkybeppe/hit-or-stand
3. Now, you need to install the dependencies.
    * Navigate to the folder where you placed the application source code and run the following command:
        * pip3 install -r requirements.txt
4. Now, you can run the application on your machine by running the following command:
    * python3 run.py

# Credits

## Content

The content of this website was created by Luca Barbero.

## Code

* Python: code snippet for card generation was taken from and modified[Stackoverflow](https://stackoverflow.com/questions/23704521/python-random-playing-card-generator-game)
* Python: code snippet for ascii card generation inspired by [Stackexchange](https://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards)
* Game is inspired by this project from [AskPython](https://www.askpython.com/python/examples/blackjack-game-using-python)
* PyInputPlus package: how to use this package was explained by the life saver book [Automate the boring stuff with Python](https://automatetheboringstuff.com/2e/chapter8/)
* Terminal color codes were taken from [GeeksforGeeks](https://www.geeksforgeeks.org/print-colors-python-terminal/)
* ASCII art logo was generated from [Security-Science](http://www.security-science.com/ascii-art)
* The project is using a [CodeInstitute](https://github.com/Code-Institute-Org/python-essentials-template) template for the mockup terminal in browser

## Acknowledgements

* Thank you to my partner Jessica, for her relentless patience and support.
* Thank you to my mentor, Ronan McLelland, for his encouragement and guidance.

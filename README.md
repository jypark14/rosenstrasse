# **ROSENSTRASSE PYGAME**

This is a pygame application that was built to serve as the front end of an online version of the Rosenstrasse tabletop role playing game.  This applications includes all aspects of the paper copy game including the game cards, workshop and character assignment, risk matrix, and sound recordings.
This project requires the installation of python as well as the pygame library in order to work properly.  

To install the latest version of python, follow this link -> https://www.python.org/downloads/
To install the latest version of pygame, follow this link -> https://www.pygame.org/download.shtml

This application was created in order to serve as a tool for facilitators of the game.  The goal of this application was to make the job of facilitators easier and more efficient.  Ease of use and flexibility for the facilitator was kept in mind during the creation of this game.

## **STARTUP**

To run the application, from the command terminal, first switch into the directory which contains the Rosenstrasse python file.  Then type "python Rosenstrasse.py" to run the game.  When the programs loads you will be met with the home screen.  There will be options to start with the instructions pages or proceed into the game.

##  **WORKSHOP**

To access the workshop portion of the game, the user must click the instructions button.  This brings up sets of instructions and guidelines for how the game is to be played as well as a workshop session.  The facilitator can move through these instructions by pressing the right arrow key to move forward or the left arrow key to move backwards.  The workshop section is where players will be assigned to characters for the game.

## **Risk Matrix**

The risk matrix can be accessed by pressing on the risk matrix icon on any given card screen.  When pressed, the facilitator will be taken to the risk matrix page which will have risk options for each risky situation Izak, Kurt, Josef, or Max may encounter.  To increase or decrease the risk of a certain character, the facilitator should click on the risk box for the player that corresponds to the correct situation and press enter.  The risk box will be updated to reflect the new risk addition and the total risk score for that character will automatically be updated as well.

At the bottom of the risk_matrix is a column for characters who become exempt from risk through their actions.  Characters who become exempt have their total risk score lowered to 0.  Once a player becomes exempt, they can not be unexempted.  They will continue to be exempt for the rest of the game.

The risk matrix was created using a class called "Input_Box".  Each character has 9 input boxes for each situation that could increase or decrease their risk status.  Each input box stores its own risk score variable and adds that variable to the total sum for a specific character.  That sum is stored in the input box named "Total" near the bottom of the risk matrix.  This method ensures that individual risk scores for a decision are saved independent of each other.  This design decision allows for scores for each decision to be seen and analyzed individually and/or as a whole.

## **Cards**

Each card is displayed with the back visible, the context visible, and the facilitator instructions visible.  The facilitator navigates through the cards by pressing the right arrow button to move forward and the back arrow button to see the previous card.  The front images of the cards were placed in a list as well as the back images.  A while loop was used to track each new button press and display the appropriate card.  It simply made a lot of sense to assign each card a place in a list.  Using an index variable as a tracker, each card was displayed according to the current index.  This index was remembered throughout the breadth of the code.  For example, if the facilitator was to go back to the menu, when they returned they would be looking at the same card they had left.  This was true for when the facilitator would open the risk matrix as well.  In order to save card placement, we used parameters for all of our functions that involved the card screen, or were linked to the card screen.  We saved the current card index as a parameter and passed it through our functions so that it would always be remembered.

For cards that had instructions to long for us to fit on a single page, we accomodated for this by alerting the facilitator that this card had more text.  By pressing the down arrow, the facilitator access the next instructions of this card on a new page so as to avoid clutter and make the instructions readable.  

For cards that may require the facilitator to update the risk matrix, there is a black alert that informs the facilitator of this possibility.  The facilitator has the option to click on the risk matrix at any time.  We believed that the facilitator should update the risk matrix at their own discretion but should be alerted at times when a characters actions make it clear that an update should occur.

# **WHY WE CHOSE PYTHON AND PYGAME**

There were many different platforms available for us to use to create the front end of this application.  We chose python and pygame for the following reasons

## **Active Developer Community**

Since python is one of the most popular languages currently being used, there are many people actively making posts about python code and libraries every day.  This made it easier for use to use pygame because we knew that if we came across problems that we were not familiar with, we could see help from other python developers online.  In addition, many of our peers and professors are familiar with python.  Debugging was much easier because there we had many examples online of similar problems as well as help from those around us at our disposal.

We specifically chose pygame because it is a library made exclusively for game programs.  It offers very specific built-in functions that make it easy to draw words, images, gifs, and other items on our screens.  The pygame documentation is full of examples and code snippets that make it one of the easier libraries to understand.

## **Easy to Understand and Maintain.  High longevity.**

One of the most important reasons we chose python and pygame was that it was easy to understand.  It is not a syntax heavy language and pygame is very intuitive.  When this project is handed off to other developers, it is very likely that they will also be familiar with the language and will quickly be able to understand what the code is doing.  This allows for easy maintenance and ensures the code will have a long life span.  Programs created with languages that are hard to use and unpopular usually don't have long life spans.  It was one of our goals to make sure that the Rosenstrasse application would be used by many people for many years and would be able to be adapted and extended as necessary.

# **Next Steps**

Like in any project, there are areas that we would like to add and see improved so that this application can be more outstanding.

## **Buttons**

During the creation of this project we focused a lot on functionality.  This meant that when we made buttons, we wanted to know if pressing them brought about the correct action more than if they were visually appealing.  One next step that can be taken is to redesign the "play" button, "instruction" button and the "risk" button to better match the other visual aspects of the game.

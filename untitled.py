# Import the pygame library and initialise the game engine

import pygame
import time  
import sys
import os 
import random
pygame.init()

# Define some colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)


backgroundImg = pygame.transform.scale(pygame.image.load("images/mainbg.png"), (1000,700))
optionImg = pygame.transform.scale(pygame.image.load("images/gameimages/back_opt.png"), (230,80))
logoTextImg = pygame.transform.scale(pygame.image.load("images/mainlogo.png"), (400,100))



# Open a new window
size = (1000, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Rosenstrasse") 

# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            carryOn = False # Flag that we are done so we exit this loop
 
     # --- Game logic should go here
 
     # --- Drawing code should go here
     # First, clear the screen to white. 
     	screen.fill(WHITE)
     	screen.blit(backgroundImg, (0,0))	
     	screen.blit(optionImg, (100,600))	
     	screen.blit(logoTextImg, (300,10))	


     #The you can draw different shapes and lines or add text to your background stage.
     	# pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
     	# pygame.draw.ellipse(screen, BLACK, [20,20,250,100], 2)
 
 
     # --- Go ahead and update the screen with what we've drawn.
     	pygame.display.flip()
     
     # --- Limit to 60 frames per second
     	clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
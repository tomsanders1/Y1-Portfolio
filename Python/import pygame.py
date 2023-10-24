import pygame
pygame.init()
# import and initialise pygame
size_x = 800
size_y = 800
# size of screen
screen = pygame.display.set_mode((size_x, size_y))
# sets the size of the pygame window
colour = (255,0,0)
#setting a colour variable
font = pygame.font.Font(None, 40)
#text size
location = (400,400)
#location variable of text
screen.blit(font.render("hello!",True, colour), location)
#setting up variables
pygame.display.update
#updates the window
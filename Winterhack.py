import pygame
import random as r
x = 1920  #dimensions for display surface object
y = 1080
x1 = r.randint(0,1700) #randomize value for snowflake drop   
pygame.init()
screen = pygame.display.set_mode([1920,1080])
white = [0, 0, 0]
screen.fill(white)
abc = 1
number_of_snowflakes = 0
pygame.display.set_caption('Image')
display_surface = pygame.display.set_mode((x,y))
while (abc == 1):
    # create a surface object, image is drawn on it. 
    snowflake2 = pygame.image.load('snowflake2.png')
    display_surface.fill(white)
    #copying image surface object
    display_surface.blit(snowflake2, (x1, 0)) #Y extreme is -260
    pygame.display.update()
        

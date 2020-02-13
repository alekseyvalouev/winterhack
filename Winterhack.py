import pygame
import random as r

#snowflake array
snowflakes = []

#movement speed
dx = 0
dy = 3

#dimensions for display surface object
x = 1080
y = 720

#randomize initial placing for first snowflake
x1 = r.randint(0,980)

#chooses which image of snowflake to use
picchooser = r.randint(0,3)

#loop placeholder
abc = 1

#bg colour
black = [0, 0, 0]

#start pygame and set up canvas
pygame.init()
screen = pygame.display.set_mode([1080,720])
screen.fill(black)
pygame.display.set_caption('Image')
display_surface = pygame.display.set_mode((x,y))

#define images and scale them
snowflake2 = pygame.image.load('snowflake2.png')
snowflake1 = pygame.image.load('snowflake1.png')
snowflake2_c = pygame.transform.scale(snowflake2, (7, 7))
snowflake1_c = pygame.transform.scale(snowflake1, (7, 7))

#make bg black
display_surface.fill(black)

for i in range(1000):
    picchooser = r.randint(1,2)
    snowflakes.append([r.randint(0, 1080), r.randint(0,720), picchooser])

#perpetual loop
while (abc == 1):

    #clear background for next snowflake
    display_surface.fill(black)

    #determines which image to use
    for q in snowflakes:
        q[1] += dy
        if (q[2] == 1):
            display_surface.blit(snowflake1_c, (q[0], q[1]))
        elif (q[2] == 1):
            display_surface.blit(snowflake2_c, (q[0], q[1]))

    #updates
    pygame.display.update()
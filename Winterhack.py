import pygame
import random as r

#snowflake array
snowflakes = []

#gravity in the y direction (pixels per frame)
gy = 0.066
wind = [7, -1]

#dimensions for display surface object
x = 1080
y = 720

#randomize initial placing for first snowflake
x1 = r.randint(0,980)

#chooses which image of snowflake to use
picchooser = r.randint(0,3)

#loop placeholder
abc = False

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
    yspeed = r.randint(1, 5)
    snowflakes.append([r.randint(0, 1580), r.randint(0, 720), picchooser, 0, yspeed, yspeed])

#perpetual loop
while (not abc):

    #kill switch
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            abc == True
            pygame.quit()

    #clear background for next snowflake
    display_surface.fill(black)

    #loops through array of snowflakes
    for q in snowflakes:
        #adds more and more speed each frame (rudimentary gravity)
        q[4] += gy
        #moves snowflake 
        q[1] += (q[4] - wind[1])
        #wind on x axis
        q[0] += -wind[0]
        q[1] = 720
        #picks snowflake image and spawns snowflakes
        if (q[2] == 1):
            display_surface.blit(pygame.transform.rotate(snowflake1_c, 1), (q[0], q[1]))
        elif (q[2] == 1):
            display_surface.blit(pygame.transform.rotate(snowflake2_c, 1), (q[0], q[1]))
            

        #checks if snowflake is offscreen
        if (q[1] > 720 or q[0] < 0):
            #resets y
            q[1] = r.randint(-180, 0)
            #resets x
            q[0] = r.randint(0, 1580)
            #resets speed
            q[4] = q[5]

    #updates
    pygame.display.update()
# main class for pygame RPS
import pygame, sys, random

# initialize pygame
pygame.init()

# set up the window
windowSurface = pygame.display.set_mode((500, 400), 0, 32) # 32 bit color, 0 = full screen, 500x400 = window size
pygame.display.set_caption('Rock, Paper, Scissors Gamble Your Life Away!')

#icon
icon = pygame.image.load('iconRPS.png')
pygame.display.set_icon(icon)

# paper player
paperPlayer = pygame.image.load('paper.png')
paperPlayer = pygame.transform.scale(paperPlayer, (50, 50)) # scale the image to 200x200
paperPlayerRect = paperPlayer.get_rect() # get the rect of the image
paperPlayerRect.center = (250, 200) # set the center of the rect to 250x200 (center of the screen)
paperPlayerRect.x = 0 # set the x position of the rect to 0
paperPlayerRect.y = 0 # set the y position of the rect to 0
paperPlayerRect.width = 200 # set the width of the rect to 200
paperPlayerRect.height = 200 # set the height of the rect to 200


# rock player
rockPlayer = pygame.image.load('rock.png')

# scissors player
scissorsPlayer = pygame.image.load('scissors.png')

# generate array of random starting coordinates for the players
def randomStartArray():
    x = []
    y = []
    for i in range(10):
        x.append(random.randint(0, 500))
        y.append(random.randint(0, 400))
    return x, y

# a function which takes array of x,y values and checks if they are too close to each other
def checkDistance(x, y):
    for i in range(len(x)):
        for j in range(len(x)):
            if i != j:
                if x[i] - x[j] < 50 and x[i] - x[j] > -50:
                    if y[i] - y[j] < 50 and y[i] - y[j] > -50:
                        return False
    return True

# check if players are out of screen bounds
def checkBounds(x, y):
    for i in range(len(x)):
        if x[i] < 0 or x[i] > 500:
            return False
        if y[i] < 0 or y[i] > 400:
            return False
    return True

# function which gets random starting coordinates for the players then checks if they are too close to each 
# other or out of screen it calls itself again
def getStartCoords():
    x, y = randomStartArray()
    if checkDistance(x, y) and checkBounds(x, y):
        return x, y
    else:
        return getStartCoords()
  

def PlayerPaper(x,y):
    windowSurface.blit(paperPlayer, (x, y)) # draw the image to the screen at 0x0
    pygame.display.update() # update the screen



# is the screen running?
running = True

#game loop
while running:
    # check for events
    for event in pygame.event.get(): #loop through all events, get() returns a list of all events.
        if event.type == pygame.QUIT: #if the event is a quit event
            running = False #stop the game loop
            pygame.quit() #stop pygame
            sys.exit()  #stop python
    
    # start of game

    # draw the background
    windowSurface.fill((192, 192, 192)) # fill the window with a color
    #--------------------------------------------------------------------
    # draw the player
    #for every elemtn in getStartCoords() draw a player
    for i in range(len(getStartCoords()[0])):
        PlayerPaper(getStartCoords()[0][i], getStartCoords()[1][i])

    



  

    # draw the window onto the screen
    pygame.display.update() 

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set up the fonts



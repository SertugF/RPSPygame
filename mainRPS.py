#example https://9gag.com/gag/ap92GVn#comment

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
paperPlayerRect.width = 50 # set the width of the rect to 200
paperPlayerRect.height = 50 # set the height of the rect to 200


# rock player
rockPlayer = pygame.image.load('rock.png')
rockPlayer = pygame.transform.scale(rockPlayer, (50, 50)) # scale the image to 200x200
rockPlayerRect = rockPlayer.get_rect() # get the rect of the image
rockPlayerRect.center = (250, 200) # set the center of the rect to 250x200 (center of the screen)
rockPlayerRect.x = 0 # set the x position of the rect to 0
rockPlayerRect.y = 0 # set the y position of the rect to 0
rockPlayerRect.width = 50 # set the width of the rect to 200
rockPlayerRect.height = 50 # set the height of the rect to 200


# scissors player
scissorsPlayer = pygame.image.load('scissors.png')
scissorsPlayer = pygame.transform.scale(scissorsPlayer, (50, 50)) # scale the image to 200x200
scissorsPlayerRect = scissorsPlayer.get_rect() # get the rect of the image
scissorsPlayerRect.center = (250, 200) # set the center of the rect to 250x200 (center of the screen)
scissorsPlayerRect.x = 0 # set the x position of the rect to 0
scissorsPlayerRect.y = 0 # set the y position of the rect to 0
scissorsPlayerRect.width = 50 # set the width of the rect to 200
scissorsPlayerRect.height = 50 # set the height of the rect to 200


# generate random starting coordinates for the player
def randomStart(): #depre
    x = random.randint(20, 450)
    y = random.randint(20, 350)
    return x, y

# generate array of random starting coordinates for the players
def randomStartArray(): #deprecated
    x = []
    y = []
    for i in range(10):
        x.append(random.randint(20, 450))
        y.append(random.randint(20, 350))
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

# check if players are out of screen bounds include player size
def checkBounds(x, y):
    for i in range(len(x)):
        if x[i] < 0 or x[i] > 450:
            return False
        if y[i] < 0 or y[i] > 350:
            return False
    return True

# function which gets random starting coordinates for the players then checks if they are too close to each 
# other or out of screen it calls itself again
def getStartCoords(): #deprecated
    x, y = randomStartArray()
    if checkDistance(x, y) and checkBounds(x, y):
        return x, y
    else: # recreate x,y pair for array
        return getStartCoords() #breaks cause of recursion limit

# function which creates random starting coordinates for a player then checks if they are too close to each or out of screen  
# this function is used to get the starting coordinates for the player. İf succesful it adds the coordinates to an array
def getStartCoords2(playerCount):
    x = []
    y = []
    
    succesfullCoords = 0
    while succesfullCoords < playerCount:
        xTemp, yTemp = randomStart()
        if checkDistance(x, y) and checkBounds(x, y):
            x.append(xTemp)
            y.append(yTemp)
            succesfullCoords += 1
        else:
            continue
    return x, y


  

def PlayerPaper(x,y):
    windowSurface.blit(paperPlayer, (x, y)) # draw the image to the screen at 0x0
    pygame.display.update() # update the screen

def PlayerRock(x,y):
    windowSurface.blit(rockPlayer, (x, y)) # draw the image to the screen at 0x0
    pygame.display.update() # update the screen

def PlayerScissors(x,y):
    windowSurface.blit(scissorsPlayer, (x, y)) # draw the image to the screen at 0x0
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
    arrStartCoordsPaper = getStartCoords2(2)
    arrStartCoordsRock = getStartCoords2(2)
    arrStartCoordsScissors = getStartCoords2(2)
    #--------------------------------------------------------------------
    #for every element in getStartCoords() draw a player
    for i in range(len(arrStartCoordsPaper)):
        PlayerPaper(arrStartCoordsPaper[i][0], arrStartCoordsPaper[i][1])
    for i in range(len(arrStartCoordsRock)):
        PlayerRock(arrStartCoordsRock[i][0], arrStartCoordsRock[i][1])
    for i in range(len(arrStartCoordsScissors)):
        PlayerScissors(arrStartCoordsScissors[i][0], arrStartCoordsScissors[i][1])


    



  

    # draw the window onto the screen
    pygame.display.update()
    
    pygame.display.flip()
    
   
    
 
# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set up the fonts



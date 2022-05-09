# 4x4 grid or 5x5 grid (resizable)
# Click on row to add chip 
# Check if 4 in a row
# Switch players

# Tutorial
# https://www.raywenderlich.com/2614-multiplayer-game-programming-for-teens-with-python-part-1 
# On "Drawing the board and lines on the screen"
# Super excited :>

import pygame

class Connect4Game():
    def initGraphics(self):
        # In the tutorial he loaded images but I can use pygame to draw the objects myself
       
        # if option is 5 by 5:
        # 100 pixels for each square (5x5)
        # 125 pixels for each square (4x4)
        self.fulltitle = pygame.image.load("Connect4 Graphics/Fulltitle.png") # Loads the images for later use
        self.grid4x4 = pygame.image.load("Connect4 Graphics/Grid.png")
        # make a 5 by 5 grid too OR draw with code (easier and expandable)

        checkersize = 100
        self.redchecker = pygame.image.load("Connect4 Graphics/redchecker.png")
        self.redchecker = pygame.transform.scale(pygame.image.load("Connect4 Graphics/redchecker.png"), (checkersize, checkersize))

        self.bluechecker = pygame.image.load("Connect4 Graphics/bluechecker.png")
        self.bluechecker = pygame.transform.scale(pygame.image.load("Connect4 Graphics/bluechecker.png"), (checkersize, checkersize))

    def __init__(self):
     #   return super().__init__(*args, **kwargs)

        pygame.init()
        pygame.display.init()
        pygame.display.set_caption("Connect_4_V1")
        self.windx = 500
        self.windy = 500
        
        self.screen = pygame.display.set_mode((self.windx, self.windy))
        self.clock = pygame.time.Clock() # Initializes clock

        self.initGraphics()

    def drawchecker(self):
        self.screen.blit(self.grid4x4, (0,0))
        n = 10
        for x in range(4):
            self.screen.blit(self.bluechecker, (n,0))
            n+=125
        pygame.draw.rect(self.screen, (255, 0, 0), (0, 0, 125, self.windy))   # rect are coords for rows
        pygame.draw.rect(self.screen, (0, 255, 0), (125, 0, 125, 500))
        pygame.draw.rect(self.screen, (0, 0, 255), (250, 0, 125, 500))
        pygame.draw.rect(self.screen, (255, 255, 0), (375, 0, 125, 500))

    def update(self):
        self.clock.tick(60) # Makes the game 60fps (wowowo)
        self.screen.fill(0) # Clears screen
        self.drawchecker()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Exits game if closed
                exit()

        pygame.display.update() # updates screen


        # display.flip() will update the contents of the entire display
        # display.update() allows to update a portion of the screen, instead of the entire area of the screen. Passing no arguments, updates the entire display

        # Define some arrays for the spaces (self.boardh = [[False for x in range(6)] for y in range(7)] for example)


bg = Connect4Game() # __init__ is called here (bg is the object)
while 1:
    bg.update()

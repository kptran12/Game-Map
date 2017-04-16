import pygame
import sys
import random
from pygame.locals import *


#Constants for resources
grass = 0
path = 1
water = 2


resources =[grass, path, water]

#Another way to display:
gameMap = [ [1, 0, 0, 0, 0, 0, 0, 0, 1, ],
            [1, 1, 2, 2, 2, 2, 2, 1, 1] ,
            [0, 1, 2, 2, 2, 2, 2, 1, 0],
            [0, 1, 2, 2, 2, 2, 2, 1, 0],
            [0, 1, 2, 2, 2, 2, 2, 1, 0] ,
            [0, 1, 1, 1, 1, 1, 1, 1, 0] ,
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0]
            ]

#Resource Colors
green = (114, 193, 33)
blue = (18, 46, 91)
brown = (156, 78 , 0)

#Linking resources to colors using dictionary
textures = {
    grass : pygame.image.load('grass.png'),
     water: pygame.image.load('water.png'),

}

TileSize = 50
MapWidth = 9
MapHeight = 9


#Display
pygame.init()
#Displays game with 4 cells per column and each cell is 25 pixels wide
DisplaySurf = pygame.display.set_mode((MapWidth*TileSize,MapHeight*TileSize))

#Player settings
Player = pygame.image.load('player.png').convert_alpha()
playerPos = [0,0]


#Object settings
rock = pygame.image.load('rock.png').convert_alpha()
rockPos = [1,7]

tree = pygame.image.load('tree.png').convert_alpha()
treePos = [7,7]



#Run user events and allows the program to stay open
#Note for later: prevent player from moving off map
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if (event.key == K_RIGHT):
                if playerPos[0] == 8:
                    pass
                elif playerPos == [6,7]:
                    pass
                else:
                    playerPos[0] += 1
            elif (event.key == K_LEFT):
                if playerPos[0] == 0:
                    pass
                elif playerPos == [8,7]:
                        pass
                else:
                    playerPos[0] -= 1
            elif (event.key == K_UP):
                if playerPos[1] == 0:
                    pass
                elif playerPos == [7,8]:
                        pass
                else:
                    playerPos[1] -= 1
            elif (event.key == K_DOWN):
                if playerPos[1] == 8:
                    pass
                elif playerPos == [7,6]:
                            pass
                else:
                    playerPos[1] += 1

#Draws the resource of the position in the Map
    for row in range(MapHeight):
        for column in range(MapWidth):
            DisplaySurf.blit(textures[gameMap[row][column]], (column*TileSize,row*TileSize))
            DisplaySurf.blit(Player,(playerPos[0]*TileSize,playerPos[1]*TileSize))
            DisplaySurf.blit(rock,(rockPos[0]*TileSize,rockPos[1]*TileSize))
            DisplaySurf.blit(tree,(treePos[0]*TileSize,treePos[1]*TileSize))

#Show display update
    pygame.display.update()

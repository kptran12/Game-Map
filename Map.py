import pygame
import sys
import random
from pygame.locals import *
# 4 x 3 grid
# Coordinates are still x and y so (1,1) would print 6
#gameMap = [['1','2','3','4'] , ['5','6','7','8'], ['9', '10', '11','12']




#Constants for resources
grass = 0
water = 1
dirt = 2
sand = 3
ice = 4
lava = 5

resources =[grass, water, dirt, sand, ice, lava]

#Another way to display:
#gameMap = [[grass, grass, grass, dirt] ,
            #[grass, water, water, dirt] ,
            #[grass,water,water,dirt]]

#Resource Colors
green = (114, 193, 33)
blue = (18, 46, 91)
brown = (156, 78 , 0)

#Linking resources to colors using dictionary
textures = {
    grass : pygame.image.load('grass.png'),
    water : pygame.image.load('water.png'),
    dirt : pygame.image.load('dirt.png'),
    sand : pygame.image.load('sand.png'),
    ice : pygame.image.load('ice.png'),
    lava : pygame.image.load('lava.png')
}

TileSize = 50
MapWidth = 10
MapHeight = 10

gameMap = [[random.choice(resources) for w in range(MapWidth)] for h in range (MapHeight) ]

#Display
pygame.init()
#Displays game with 4 cells per column and each cell is 25 pixels wide
DisplaySurf = pygame.display.set_mode((MapWidth*TileSize,MapHeight*TileSize))

#Player settings
Player = pygame.image.load('player.png').convert_alpha()
playerPos = [0,0]

#Test
jelly = pygame.image.load('jelly1.png').convert_alpha()
jellyPos = [3,5]

#Run user events and allows the program to stay open
#Note for later: prevent player from moving off map
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if (event.key == K_RIGHT):
                if playerPos[0] == 9:
                    playerPos[0] == 9
                else:
                    playerPos[0] += 1
            elif (event.key == K_LEFT):
                if playerPos[0] == 0:
                    playerPos[0] == 0
                else:
                    playerPos[0] -= 1
            elif (event.key == K_UP):
                if playerPos[1] == 0:
                    playerPos[1] == 0
                else:
                    playerPos[1] -= 1
            elif (event.key == K_DOWN):
                if playerPos[1] == 9:
                    playerPos[1] == 9
                else:
                    playerPos[1] += 1

#Draws the resource of the position in the Map
    for row in range(MapHeight):
        for column in range(MapWidth):
            DisplaySurf.blit(textures[gameMap[row][column]], (column*TileSize,row*TileSize))
            DisplaySurf.blit(Player,(playerPos[0]*TileSize,playerPos[1]*TileSize))
            DisplaySurf.blit(jelly,(jellyPos[0]*TileSize,jellyPos[1]*TileSize))
#Show display update
    pygame.display.update()

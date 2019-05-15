import pygame
import random
import time
from map import Map
import square
from menu import menu



gameState = menu()

if gameState == 'aloita':

    pygame.init()
    gameDisplay = pygame.display.set_mode((1600,900))
    pygame.display.set_caption('Jugilization')
    pygame.display.update()
    gameExit = False

    black = (0,0,0)
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    white = (255,255,255)
    gameDisplay.fill(black)
    
    random.seed()
    seeds = []
    siemenia = 100
    heigth = 90
    width = 160

    MAASTO = ["vesi","maa"]
    map = []

    for i in range(width):
        map.append([])
        for j in range(height):
            map[i].append("vesi")

    for i in range (siemenia):
        map[random.randint(0,width-1)][random.randint(0,height-1)] = "maa"

    for i in range(width):
        for j in range(height):
            if map[i][j] == "maa":
                pygame.draw.rect(gameDisplay, green, [10*i,10*j,10,10])
            if map[i][j] == "vesi":
                pygame.draw.rect(gameDisplay, blue, [10*i,10*j,10,10])
        pygame.display.update()
        time.sleep(0.1)

        

elif gameState == 'lataa':
    #lataa peli
    print "latasit pelin"
elif gameState == 'asetukset':
    #aloita asetusnakyma
    print "halusit muutta asetuksia"


pygame.quit()
quit()
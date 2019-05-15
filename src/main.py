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
    img_tasanko = pygame.image.load('maa.png')
    img_vesi = pygame.image.load('vesi.png')
    img_aavikko = pygame.image.load('aavikko.png') 

    gameDisplay.fill(black)

    kartta = Map(160, 90, 40)
    kartta.clean()
    kartta.clean()
    

    for i in range(kartta.get_width()):
        for j in range(kartta.get_height()):
            if kartta.get_pos(i,j) == "maa":
                #pygame.draw.rect(gameDisplay, green, [10*i,10*j,10,10])
                gameDisplay.blit(img_tasanko,(10*i,10*j))
            if kartta.get_pos(i,j) == "vesi":
                #pygame.draw.rect(gameDisplay, blue, [10*i,10*j,10,10])
                gameDisplay.blit(img_vesi,(10*i,10*j))
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
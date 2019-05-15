import pygame


def menu():
    menu = True
    pygame.init()
    gameDisplay = pygame.display.set_mode((1600,900))
    pygame.display.set_caption('Jugilization')
    pygame.display.update()
    gameExit = False
    gameState = ''

    black = (0,0,0)
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    white = (255,255,255)
    gameDisplay.fill(black)
    titlefont = pygame.font.SysFont(None, 200)
    menufont = pygame.font.SysFont(None, 60)
    titlesurf = titlefont.render('JUGILIZATION', False, white)
    menusurf1 = menufont.render('Aloita peli', False, black)
    menusurf2 = menufont.render('Lataa peli', False, black)
    menusurf3 = menufont.render('Asetukset', False, black)
    menusurf4 = menufont.render('Lopeta', False, black)

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
            if pygame.mouse.get_pressed()[0] and sprite_rect_aloita.collidepoint(pygame.mouse.get_pos()):
                gameState = 'aloita'
                pygame.quit()
                return gameState
            if pygame.mouse.get_pressed()[0] and sprite_rect_lataa.collidepoint(pygame.mouse.get_pos()):
                gameState = 'lataa'
                pygame.quit()
                return gameState
            if pygame.mouse.get_pressed()[0] and sprite_rect_asetukset.collidepoint(pygame.mouse.get_pos()):
                gameState = 'Asetukset'
                pygame.quit()
                return gameState
            if pygame.mouse.get_pressed()[0] and sprite_rect_lopeta.collidepoint(pygame.mouse.get_pos()):
                menu = False

            pygame.display.update()
            gameDisplay.blit(titlesurf,(300,200))
            sprite_rect_aloita = pygame.draw.rect(gameDisplay, white, [700,450,200,50])
            sprite_rect_lataa = pygame.draw.rect(gameDisplay, white, [700,550,200,50])
            sprite_rect_asetukset = pygame.draw.rect(gameDisplay, white, [700,650,200,50])
            sprite_rect_lopeta = pygame.draw.rect(gameDisplay, white, [700,750,200,50])
            gameDisplay.blit(menusurf1,(700,450))
            gameDisplay.blit(menusurf2,(705,550))
            gameDisplay.blit(menusurf3,(700,650))
            gameDisplay.blit(menusurf4,(720,750))
            
    pygame.quit()
    return gameState
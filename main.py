from fonts import *
from pygame.locals import *
import random
from colors import *
import time

pygame.init()
pygame.font.init
pygame.display.set_caption('Hangman')

screen=pygame.display.set_mode((800,500))
DISPLAYSURF=pygame.display.set_mode((800,500))

def ESC_func(running):
    if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
        running= False
    return running

def display_game():
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(COMIC_SANS_BIG.render('salut', True, BLACK), (200, 100))

if __name__ == "__main__":
    running=True
    while running:
        display_game()
        events=pygame.event.get()
        for event in events:
            running=ESC_func(running)
        pygame.display.update()
        pygame.time.wait(200)
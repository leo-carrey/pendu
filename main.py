from fonts import *
from pygame.locals import *
import random
from colors import *
import time

AUTHORIZED_KEYS=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
display_keys=''.join(AUTHORIZED_KEYS)

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
    DISPLAYSURF.blit(COMIC_SANS_SMALL.render(' '.join(display_keys[:13]), True, BLACK), (450, 50))
    DISPLAYSURF.blit(COMIC_SANS_SMALL.render(' '.join(display_keys)[26:], True, BLACK), (450, 100))
    pygame.display.update()

def replace_all_word(AUTHORIZED_KEYS,word):
    new_str=''
    for i in AUTHORIZED_KEYS:
        if i in word:
            new_str+='#'
        else:
            new_str+=i
    return new_str


if __name__ == "__main__":
    running=True
    typed_words=''
    word_to_guess=''
    while running:
        display_game()
        events=pygame.event.get()
        for event in events:
            print()
            
            running=ESC_func(running)
        pygame.display.update()
        pygame.time.wait(200)
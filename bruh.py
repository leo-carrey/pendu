import pygame
from pygame.locals import *
import pygame, sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

def quick_esc(running):
    if event.type==pygame.KEYDOWN and event.key ==pygame.K_ESCAPE:
        running=False
    return running

running=True
while running:
    sysFont = pygame.font.SysFont("None", 32)
    rendered = sysFont.render('Hello World', 0, (255,100, 100))
    screen.blit(rendered, (100, 100))
    events=pygame.event.get()
    for event in events:
        running=quick_esc(running)
        if event.type == QUIT:
            pygame.quit()
            
    pygame.display.update()
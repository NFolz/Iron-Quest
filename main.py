import pygame
from settings import *
from Mission import MissionClass
# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #initializing the screen dimensions
pygame.display.set_caption('Iron Quest')
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BG_COLOR)

    pygame.display.update()
    clock.tick(60)



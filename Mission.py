import pygame
from settings import *
class MissionClass:
    def __init__(self):

        #level setup
        self.display_surface = pygame.display.get_surface() 

        # sprite group setup
        self.visible_sprites = pygame.sprite.Group() # sprites that actually get drawn onto the screen
        self.active_sprites = pygame.sprite.Group() # sprites that will be updated, like the main character
        self.collision_sprites = pygame.sprite.Group() #sprites that the player can collide with
        

    def run(self): 
        # run the level



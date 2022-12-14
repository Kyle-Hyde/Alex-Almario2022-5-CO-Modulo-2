import pygame
from pygame.sprite import Sprite
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD
from  dino_runner.components.obstacles.obstacle_manager import obstacle_manager

class bird(Obstacle):
    def __init__(self):
        self.image_b=BIRD[0]
        self.bird_rect =self.image.get_rect()
        self.bird_rect.y=200
        self.step_index=0
        self.bird_fly=True
    
    def update(self):
        if self.bird_fly:
            self.fly()
    
    def fly(fly):
        self.image_b= BIRD[0] if self.step_index < 5 else BIRD[1]
        self.bird_rect =self.image.get_rect()
        self.bird_rect.y =self.Y_POS
        self.step_index -= 1

    def draw(self,screen):
        screen.blit(self.image, (self.bird_rect.x,self.bird_rect.y))
   



        

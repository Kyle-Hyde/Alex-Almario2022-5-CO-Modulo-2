import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.cactus import Cactustwo
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS


class ObstacleManager:
    def __init__(self):
        self.obstacles=[]

    def update(self,game):
        if len(self.obstacles)==0:
            cactus= Cactus(SMALL_CACTUS)
            self.obstacles.append(cactus)
            if len(self.obstacles)>=1:
                cactus_two=Cactustwo(LARGE_CACTUS)
                self.obstacles.append(cactus_two)
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed,self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(10000)
                game.playing=False
                break

    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
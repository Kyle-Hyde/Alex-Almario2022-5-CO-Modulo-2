import pygame

from dino_runner.utils.constants import FONT_STYLE,BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.menu import Menu

class Game:
    GAME_SPEED=20
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = self.GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player=Dinosaur()
        self.obstacle_manager=ObstacleManager()
        self.running=False
        self.score=0
        self.death_count=0
        self.menu= Menu('Press any key to start', self.screen)

    def execute(self):
        self.running=True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.obstacle_manager.reset_obstacles()
        self.score=0
        self.game_speed=self.GAME_SPEED
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input= pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        #pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_menu(self):
        self.menu.reset_screen_color(self.screen)
        half_screen_height= SCREEN_HEIGHT//2
        half_screen_widht= SCREEN_WIDTH//2

        if self.death_count==0:
            self.menu.draw(self.screen)
        else:
            self.menu.update_message('You died, Press any key to restart')
            self.draw_score()
            self.menu.draw(self.screen)


        self.screen.blit(ICON,(half_screen_widht-50,half_screen_height-140))

        self.menu.update(self)  


    def update_score(self):
        self.score+= 1
        self.max_score=0
        if self.score %100 ==0 and self.game_speed < 500:
            self.game_speed += 5
        elif self.playing==False and self.score >= self.max_score:
            self.max_score= self.score +0

    def draw_bestscor(self):
        font= pygame.font.Font(FONT_STYLE,30)
        text=font.render(f'Best score:{self.max_score}',True,(0,0,0))
        text_rect=text.get_rect()
        text_rect.center=(1000,50)
        self.screen.blit(text,text_rect)

    def draw_score(self):
        font= pygame.font.Font(FONT_STYLE,30)
        text=font.render(f'Score:{self.score}',True,(0,0,0))
        text_rect=text.get_rect()
        text_rect.center=(1000,50)
        self.screen.blit(text,text_rect)

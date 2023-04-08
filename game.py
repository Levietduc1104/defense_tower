
import os
import pygame
from enemies.scorpion import Scorpion
from enemies.club import Club
from enemies.wizard import Wizard

pygame.font.init()

class Game:
    def __init__(self) -> None:
        self.width: int = 1200
        self.height: int = 800
        self.win = pygame.display.set_mode((self.width, self.height))
        self.towers: list = []
        self.enemys = [Club()]
        # self.enemys = []
        self.lives: int = 10
        self.money: int = 100
        self.img = pygame.image.load(os.path.join("/Users/levietduc/Documents/Learning/Tower/craftpix-net-519305-tower-defense-2d-game-kit/2d-monster-sprites/PNG/1", "1_enemies_1_run_000.png")).convert_alpha()
        self.bg = pygame.image.load(os.path.join("/Users/levietduc/Documents/Learning/Tower/craftpix-net-519305-tower-defense-2d-game-kit/td-tilesets1-2/tower-defense-game-tilesets/PNG/game_background_2/", "game_background_2.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width,self.height)) # make the image of the game fit to size of image
        self.clicks = []



    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            # pygame.time.delay(00)
            clock.tick(300)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                # display the click
                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:  # get the mouse position
                    pass
                #     self.clicks.append(pos)
                # print (self.clicks)
            # loop through enemies
            to_del = []
            for en in self.enemys:
                if en.x < -15:
                    to_del.append(en)

            for d in to_del:
                self.enemys.remove(d)


            self.draw()


        pygame.quit()

    def draw(self):
        # The draw method is responsible for drawing the game elements on the screen,
        # such as the background image
        self.win.blit(self.bg, (0,0)) #load the background
        # for p in self.clicks:
        #     pygame.draw.circle(self.win,(255,0,0),(p[0],p[1]),5,0)
        # pygame.display.update()
        for enemy in self.enemys:
            enemy.draw(self.win)
        self.debug(f"{pygame.mouse.get_pos()}", pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        pygame.display.update()

    def debug(self, info, x=10, y=10):
        display_surf = pygame.display.get_surface()
        debug_surf = pygame.font.SysFont("Arial", 30).render(str(info), True, "Red")
        debug_rect = debug_surf.get_rect(topleft=(x,y))
        pygame.draw.rect(display_surf, "Black", debug_rect)
        display_surf.blit(debug_surf, debug_rect)

g = Game()
g.run()
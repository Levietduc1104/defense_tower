import pygame
from .tower import Tower
import os

class ArcherTowerLong(Tower):


    def __init__(self, x, y):
        super().__init__( x ,y)
        self.tower_imgs = []
        self.archer_imgs = []
        self.archer_count = 0



        #load the archer tower images
        for x in range (7,10):
            self.tower_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("/Users/levietduc/Documents/Learning/Tower/craftpix-net-519305-tower-defense-2d-game-kit/archer-tower-game-assets/PNG" , str(x)+ ".png")).convert_alpha(),(90,90)))
        # load the archer images

        for x in range (37,43):
            self.archer_imgs.append(pygame.image.load(os.path.join("/Users/levietduc/Documents/Learning/Tower/craftpix-net-519305-tower-defense-2d-game-kit/archer-tower-game-assets/PNG" , str(x)+ ".png")).convert_alpha(),)

    def attack(self,enemies):
        """
        attachks enemy in the enemy list, modifies list.
        :param: enemies: list of enemies
        :return: None
        """
        pass

    def draw (self,win):
        """ draw the ancher and animated archer """
        super().draw(win)
        if self.archer_count >= len(self.archer_imgs) * 10:
            self.archer_count  = 0

        archer = self.archer_imgs[self.archer_count // 10]
        win.blit(archer, ((self.x + archer.get_width()/2 - 40 ), (self.y - archer.get_height() + 30)))
        self.archer_count += 1


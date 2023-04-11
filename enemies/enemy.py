import pygame
import math
import os

class Enemy:

    imgs = []

    def __init__(self) -> None:

        self.images: list = []
        self.animation_count: int = 0
        self.health: int = 1
        self.img = None
        self.width: int = 64
        self.height: int = 64
        self.velocity: int = 3
        self.path_position: int = 0
        self.move_count: int = 0
        self.dis: int = 0
        # self.imgs = []

        self.path = [(5, 261), (200, 279), (302, 325), (577, 304), (644, 120), (725, 59), (826, 154), (872, 296), (1027, 359), (1030, 527), (918, 581), (757, 579), (660, 642), (144, 637),(87,501), (4, 420), (-5,392), (-20, 392)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.flipped = False

    def draw(self, win):

        """
            Draw the enemy with the given images
            : param: win : surface
            : return: None
        """

        self.img = self.imgs[self.animation_count]


        # for dot in self.path:
        #     pygame.draw.circle(win, (255, 0, 0), dot , 10 , 0  )
        #     print(dot)
        win.blit(self.img, (self.x - self.img.get_width()/2, self.y - self.img.get_height()/2 -35))

        # print (self.y)
        self.move()


    def collide(self, X,Y):
        """
        Returns if position has hit the enemy.

        """
        if X <= self.x + self.width and X >= self.x: # (self.x + self.width) is the right side of enemy and self.x is\
                                                     # the left side of enemy. Basically, if the X (given position) is in range of
                                                     # enemy, it is hit.
            if Y <= self.y + self.height and Y>= self.y:# (self.y + self.width) is the bottom side of enemy and self.y is\
                                                     # the top  of enemy. Basically, if the Y (given position) is in range of
                                                     # enemy, it is hit.
                return True
        return False


    def move(self):

        """Move enemy"""
        self.animation_count += 1
        x1 = 0
        y1 = 0
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0
        if self.path_position < len(self.path):

            x1,y1 = self.path[self.path_position] # geting position of the enemy.

        if self.path_position +1 >= len(self.path): # if the current position of the enemy  at the end of the path then the enemy is moved to a point outside of the screen
                                                       # which presumably represents the enemy leaving the game area.
            x2,y2 = (-10,355)
        else: # the enemy position is the next postition
            x2,y2 = self.path[self.path_position + 1]

        dirn = ((x2-x1)*2 , (y2-y1)*2)

        length = math.sqrt((dirn[0]) ** 2 + (dirn[1]) ** 2)
        dirn = (dirn[0]/length, dirn[1]/length)
        # print("dirn", dirn)

        if dirn[0] < 0 and not (self.flipped): # flip the enemy when it run in oposite path
            self.flipped = True
            for x, img in enumerate (self.imgs):
                self.imgs[x] = pygame.transform.flip(img, True, False)

        move_x, move_y = ((self.x + dirn[0]), (self.y + dirn[1]))

        self.x = move_x
        self.y = move_y


        # Go to next point

        if dirn[0] >= 0: # moving right
            if dirn[1] >= 0: # moving down
                if self.x >= x2 and self.y >= y2:
                    self.path_position += 1
            else:
                if self.x >= x2 and self.y <= y2:
                    self.path_position += 1
        elif dirn[0] <= 0: # moving left
            if dirn[1] >= 0:  # moving down
                if self.x  <= x2 and self.y >= y2:
                    self.path_position += 1
            else:
                if self.x <= x2 and self.y >= y2:
                    self.path_position += 1
        # return True



    def hit(self):
        """
        Returns if an enemy has died and removes one health each call

        """
        self.health -= 1
        if self.health < 0:
            return True
        return False


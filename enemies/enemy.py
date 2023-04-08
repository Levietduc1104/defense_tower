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

        # self.path = [(-10, 262),(13, 262), (55, 262), (103, 262), (134, 262), (177, 268), (203, 287), (223, 307), (247, 319), (293, 322), (513, 321), (564, 309), (593, 277), (608, 229), (626, 164), (651, 113), (687, 87), (754, 76), (794, 96), (815, 139), (834, 204), (846, 242), (879, 289), (917, 306), (969, 335), (1025, 376), (1045, 444),  (1034, 485), (1029, 503), (1022, 517), (1016, 528), (1002, 538), (992, 545), (972, 547), (954, 551), (942, 560), (922, 572), (898, 572), (879, 572), (865, 575), (850, 575), (833, 577), (814, 579), (794, 578), (770, 581), (757, 582), (745, 587), (729, 595), (713, 605), (701, 617), (689, 627), (668, 638), (651, 638), (635, 640), (619, 639), (602, 637), (587, 637), (569, 642), (554, 641), (543, 641), (525, 641), (510, 641), (496, 641), (485, 641), (471, 641), (452, 641), (435, 641), (420, 641), (402, 640), (386, 641), (367, 640), (341, 641), (326, 642), (309, 641), (291, 641), (273, 641), (260, 641), (246, 640), (231, 641), (213, 638), (194, 637), (179, 631), (169, 626), (155, 617), (146, 607), (129, 594), (116, 582), (112, 566), (103, 547), (101, 533), (99, 514), (93, 495), (83, 477), (75, 462), (68, 447), (60, 434), (56, 426), (44, 413), (31, 403), (19, 396), (5, 387), (-20,387)]

        self.path = [(-10, 262),(13, 262), (55, 262), (103, 262), (134, 262), (177, 268), (203, 287), (223, 307), (247, 319), (293, 322),(513, 321), (564, 309), (593, 277), (608, 229), (626, 164), (651, 113), (687, 87), (754, 76), (794, 96),(815, 139), (834, 204), (846, 242), (879, 289), (917, 306), (969, 335), (1025, 376), (1045, 444),  (1034, 485), (1029, 503), (1022, 517), (1016, 528),(1002, 538), (992, 545), (972, 547), (954, 551)]

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
        # self.animation_count += 1
        # if self.animation_count >= len(self.imgs):
        #     self.animation_count = 0

        if self.y > 538:
            win.blit(self.img, (self.x - self.img.get_width()/2 -35, self.y - self.img.get_height()/2 -35))
        elif self.y < 538:
            win.blit(self.img, (self.x - self.img.get_width()/2 -35, self.y - self.img.get_height()/2 -35))
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
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0
        x1,y1 = self.path[self.path_position] # geting position of the enemy.



        if self.path_position + 1 >= len(self.path): # if the current position of the enemy  at the end of the path then the enemy is moved to a point outside of the screen
                                         # which presumably represents the enemy leaving the game area.
            x2,y2 = (-10,355)
        else: # the enemy position is the next postition
            x2,y2 = self.path[self.path_position + 1]



        # move_dis = math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)
        # self.move_count += 1
        # dirn = ((x2-x1), (y2-y1) )
        dirn = ((x2-x1)*2, (y2-y1)*2)

        length = math.sqrt((dirn[0]) ** 2 + (dirn[1]) ** 2)
        dirn = (dirn[0]/length, dirn[1]/length)
        # print("dirn", dirn)

        if dirn[0] < 0 and not (self.flipped): # flip the enemy when it run in oposite path
            self.flipped = True
            for x, img in enumerate (self.imgs):
                self.imgs[x] = pygame.transform.flip(img, True, False)

        move_x, move_y = ((self.x + dirn[0]), (self.y + dirn[1]))
        # print(move_x, move_y)

        self.x = move_x

        if move_y > 520:

            self.y = move_y
        else:

            self.y = move_y
        # print("dirn[1]", dirn[1])
        # print("self.y", self.y)
        print("move_y", move_y)
        # self.dis += math.sqrt((move_x-x1) ** 2 + (move_y-y1) ** 2)

        # if self.dis >= length:
        #     # self.dis = 0
        #     self.move_count = 0
        #     self.path_position += 1
        #     if self.path_position >= len(self.path):
        #         return False

        # Go to next point

        if dirn[0] >= 0: # moving right
            if dirn[1] >= 0: # moving down
                if self.x >= x2 and self.y >= y2:
                    self.path_position += 1
            else:
                if self.x >= x2 and self.y <= y2:
                    self.path_position += 1
        else: # moving left
            if dirn[1] >= 0:  # moving down
                if self.x <= x2 and self.y >= y2:
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


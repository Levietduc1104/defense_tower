import pygame

class Tower:

    def __init__(self,x,y) -> None:
        self.x: int = x
        self.y: int = y
        self.width: int = 0
        self.height: int = 0
        self.sell_price: list = [0, 0, 0]
        self.price: list = [0,0, 0]
        self.level: int = 1
        self.selected = False
        self.menu = None
        self.tower_imgs = []
        self.animation_count = 0
        self.img = []

    def draw(self,win):
        self.img = self.tower_imgs[self.level - 1]

        win.blit(self.img, (self.x - self.img.get_width()/2, self.y - self.img.get_width()/2 + 55))

    def click (self, X, Y):
        """
        returns it tower is clicked and chosen.
        :param X: int
        :param Y: int
        :return: bool

        """

        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y>= self.y:
                return True
        return False

    def sell(self):
        """
        call to sell the tower, returns the price
        :return: int
        """

        return self.sell_price[self.level - 1]


    def upgrade(self):
        """
        Upgrade the tower for given cost
        """
        self.level += 1

    def get_upgrade_cost(self):
        """
        returns the upgrade cost, if 0 then cant upgrade anymore
        :return: int
        """
        return self.price[self.level -1]


    def move(self , x ,y):
        self.x = x
        self.y = y



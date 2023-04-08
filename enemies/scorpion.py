import pygame
import os
from .enemy import Enemy


class Scorpion(Enemy):
    imgs = []


    for x in range (20):
        add_str = str(x)
        if x < 10:
            add_str = "0" + add_str
        imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("/Users/levietduc/Documents/Learning/Tower-Defense-Game/craftpix-net-519305-tower-defense-2d-game-kit/2d-monster-sprites/PNG/1", "1_enemies_1_run_0" + \
                add_str + ".png")),(64,64)))


    def __init__(self) -> None:
        super().__init__()
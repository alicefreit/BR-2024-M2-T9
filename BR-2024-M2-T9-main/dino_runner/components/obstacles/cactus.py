import random

from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS
from dino_runner.components.obstacles.obstacle import Obstacle


class Cactus(Obstacle):

    CACTUS = [
        (LARGE_CACTUS, 300),
        (SMALL_CACTUS, 325),
    ] # diz o tamanho  das imagens dos cactus

    def __init__(self):
        image, cactus_pos = self.CACTUS[random.randint(0, 1)] # fala do intervalo das imagens de forma aleatoria 
        self.type = random.randint(0, 2) # tipo das imagens de forma aleatoria
        super().__init__(image, self.type)
        self.rect.y = cactus_pos
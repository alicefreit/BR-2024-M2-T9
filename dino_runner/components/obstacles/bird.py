from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.obstacle import Obstacle


class Bird(Obstacle):
    def __init__(self): # chama imagem e diz a posição
        super().__init__(BIRD, 0)
        self.rect.y = 250 # posição das imagens do passáro
        self.step_index = 0

    def draw(self, screen): # diz o intervalo da da imagen
        screen.blit(self.image[self.step_index // 5], self.rect)
        self.step_index += 1 # índice de autopasso

        if self.step_index >= 10:
            self.step_index = 0
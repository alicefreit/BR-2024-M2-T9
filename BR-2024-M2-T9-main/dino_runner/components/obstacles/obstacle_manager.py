import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game): 
        obstacle_type = [ #chama os cactus e os passaros
            Cactus(),
            Bird(),
        ]

        if len(self.obstacles) == 0:            
            self.obstacles.append(obstacle_type[random.randint(0,1)]) # fala para os obstaculos aparecenrem de forma aleatoria
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up: # enquanto um obstaculo estiver aparecendo. Se o jogador bater no obstáculo, o jogo acabe e fecha
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break
                else: # Se não a imagem sai e o jogo continua
                    self.obstacles.remove(obstacle)

    def reset_obstacles(self):
        self.obstacles = [] 

    def draw(self, screen):
        for obstacle in self.obstacles: # para um obstaculo em "self.obstacles"
            obstacle.draw(screen) # o desenho passa de forma continua
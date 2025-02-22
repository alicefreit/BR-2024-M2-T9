import pygame
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Other/logo.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/jonhRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/jonhRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/JonhRunS1.0.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/JonhRunS2.0.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/JonhRunH1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/JonhRunH2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/jonhRun1.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/JonhRunS1.0.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/JonhRunH1.png"))
JUMPING_VEVENO = pygame.image.load(os.path.join(IMG_DIR, "Dino/JonhAngel.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/JonhDuck1.0.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/JonhDuck2.0.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/JonhDuckS1.0.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/JonhDuckS2.0.png")),
]

ANGEL = [
     pygame.image.load(os.path.join(IMG_DIR, "Dino/JonhAngel.png")),
      pygame.image.load(os.path.join(IMG_DIR, "Dino/JonhAngel2.png")),

]


ANGEL1 = [
     pygame.image.load(os.path.join(IMG_DIR, "Dino/JonhAngel.png")),
      pygame.image.load(os.path.join(IMG_DIR, "Dino/JonAngel2.png")),

]


DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/JonhDuckH1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/JonhDuckH2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/smallT1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/smallT2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/smallT3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/largeG1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/largeG2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/largeG3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/gaspar1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/gaspar2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/pocao.png'))
VEVENO = pygame.image.load(os.path.join(IMG_DIR, 'Other/veveno.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/fantasma.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/rua.jpeg'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"
DEATH_TYPE = "veneno"


FONT_COLOR = (0, 0, 0)
FONT_SIZE = 22
FONT_STYLE = "freesansbold.ttf"


def draw_message_component(
    message,
    screen,
    font_color=FONT_COLOR,
    font_size=FONT_SIZE,
    pos_y_center=SCREEN_HEIGHT // 2,
    pos_x_center=SCREEN_WIDTH // 2
):
    font = pygame.font.Font(FONT_STYLE, font_size)
    text = font.render(message, True, font_color)
    text_rect = text.get_rect()
    text_rect.center = (pos_x_center, pos_y_center)
    screen.blit(text, text_rect)




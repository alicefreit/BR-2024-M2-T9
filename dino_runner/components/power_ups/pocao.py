from dino_runner.utils.constants import VEVENO, DEATH_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class Veveno(PowerUp):
    def __init__(self):
        self.image = VEVENO
        self.type = DEATH_TYPE
        super().__init__(self.image, self.type)
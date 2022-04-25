from random import random

import arcade
import math
import random

from sprites.unit import Unit


class Factory(arcade.SpriteSolidColor):
    GREEN_BUILDING_COLOR_RGB = (12, 206, 106)
    RED_BUILDING_COLOR_RGB = (209, 52, 91)

    BUILDING_RADIUS = 70
    ROTATION_SPEED = 0.3
    BUILDING_BASE_HEALTH = 1000

    def __init__(
        self, name: str, color, center_x: float = 0, center_y: float = 0
    ) -> None:
        super().__init__(Factory.BUILDING_RADIUS, Factory.BUILDING_RADIUS, color=color)
        self.name = name
        self.health = Factory.BUILDING_BASE_HEALTH

        self.center_x = center_x
        self.center_y = center_y
        self.alpha = 200
        self.change_angle = Factory.ROTATION_SPEED

    def take_damage(self, damage: float) -> None:
        if not self.is_destroyed():
            if self.health - damage > 0:
                self.health -= damage
            else:
                self.health = 0
                super().kill()

    def is_destroyed(self) -> bool:
        return self.health == 0

    def build_unit(self, name, sprite_name) -> Unit:
        x, y = Factory.get_position(
            self.center_x, self.center_y, 50.0, random.random() * 360
        )
        return Unit(name, sprite_name, x, y)

    def get_position(x: float, y: float, distance: float, angleDegrees: float):
        angle_radians = math.pi / 2 - math.radians(angleDegrees)
        return x + distance * math.cos(angle_radians), y + distance * math.sin(
            angle_radians
        )

    def update_animation(self, delta_time: float = 1 / 60):
        self.angle += self.change_angle
        super().update_animation(delta_time)

import os


SCREEN_TITLE = "Hermes"

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 680

BACKGROUND_COLOR_RGB = (46, 53, 50)
GREEN_COLOR_RGB = (12, 206, 106)
RED_COLOR_RGB = (209, 52, 91)

RED_POSITION = (SCREEN_WIDTH / 8, SCREEN_HEIGHT - SCREEN_HEIGHT / 8)
GREEN_POSITION = (SCREEN_WIDTH - SCREEN_WIDTH / 8, SCREEN_HEIGHT / 8)

START_RESOURCES = 1000
UNITS_LIMIT = 30
DRONES_LIMIT = 10

FACTORY_BASE_HEALTH = 1000

UNIT_SPEED = 2
UNIT_BUILD_COST = 100
UNIT_BASE_HEALTH = 100
ATTACK_RANGE = 150.0
ROOT_DIR = os.path.abspath(os.curdir)
RED_UNIT_SPRITE_NAME = f"{ROOT_DIR}/assets/unit_red.png"
GREEN_UNIT_SPRITE_NAME = f"{ROOT_DIR}/assets/unit_green.png"

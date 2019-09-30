import sys
import pygame
import game_functions as gf

from settings import Settings
from ship import Ship


def run_game():
    pygame.init()
    settings = Settings()

    # screen is a pygame.Surface object
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption('Space Invader')

    # Create a Space ship object.
    ship = Ship(screen)

    while True:
        gf.check_event(ship)
        ship.update()
        # pygame will not draw anything new before flip,
        # anything drawn will be buffered until flip() is called.
        gf.update_screen(settings, screen, ship)


run_game()

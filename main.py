import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
   pygame.init()
   settings = Settings()

   # screen is a pygame.Surface object
   screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
   pygame.display.set_caption('Space Invader')

   ship = Ship(screen)

   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            sys.exit()

      # pygame will not draw anything new before flip,
      # anything drawn will be buffered until flip() is called.
      screen.fill(settings.bg_color)
      ship.blitme()
      pygame.display.flip()

run_game()
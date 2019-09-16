import sys
import pygame

def run_game():
   pygame.init()

   # screen is a pygame.Surface object
   screen = pygame.display.set_mode((640,480))
   pygame.display.set_caption('Space Invader')

   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            sys.exit()

      # pygame will not draw anything new before flip,
      # anything drawn will be buffered until flip() is called.
      pygame.display.flip()

run_game()
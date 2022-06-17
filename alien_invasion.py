import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Class to manage game asset and behaviors"""
    def __init__(self):
        """Initialize the game"""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_heigth))

        # title
        pygame.display.set_caption("Alien Invasion")

        # shows the ship element
        # self == current instance of AlienInvasion
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
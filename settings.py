class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game setting's"""
        # window size
        self.screen_width = 1200
        self.screen_heigth = 800
        # background color
        self.bg_color = (192, 192, 192)

        # Ship setting's
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 5
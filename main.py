import sys

import pygame

import assets
import config
from game_object import GameObject
from spaceship import Spaceship


# pressed input map.
PRSD_INPUT_MAP = {
    pygame.K_RIGHT: lambda game: game.spaceship.rotate_right(game.delta_time),
    pygame.K_LEFT: lambda game: game.spaceship.rotate_left(game.delta_time),
    pygame.K_UP: lambda game: game.spaceship.set_accel_state(True),
}

# released input map.
REL_INPUT_MAP = {pygame.K_UP: lambda game: game.spaceship.set_accel_state(False)}


class Main:
    def __init__(self):
        self.init_engine()
        self.clock = pygame.time.Clock()
        self.background = assets.load.image("space.png", alpha=False)
        self.spaceship = Spaceship(
            image=assets.scale.image(
                assets.load.image("spaceship.png", alpha=True),
                config.SPACESHIP_SZ_SCALE,
            ),
            center_pos=(config.WINDOW_HEIGHT / 2, config.WINDOW_WIDTH / 2),
            accel=config.SPACESHIP_ACCEL,
            max_accel=config.SPACESHIP_MAX_ACCEL,
            rot_vel=config.SPACESHIP_ROT_VEL
        )
        self.game_end = False

    def init_engine(self):
        pygame.init()
        self.screen = pygame.display.set_mode(config.WINDOW_SIZE)
        pygame.display.set_caption(config.WINDOW_TITLE)

    def main_loop(self):
        while not self.game_end:
            self.delta_time = self.clock.tick(60) / 1000.0
            self.handle_input()
            self.process_game_logic()
            self.draw()
            pygame.display.flip()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if executioner := REL_INPUT_MAP.get(event.key):
                    executioner(self)
        keys = pygame.key.get_pressed()
        for key, executioner in PRSD_INPUT_MAP.items():
            if keys[key]:
                executioner(self)

    def process_game_logic(self):
        GameObject.update_all(self.delta_time)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        GameObject.draw_all(self.screen)


if __name__ == "__main__":
    game = Main()
    game.main_loop()

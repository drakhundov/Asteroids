from typing import Tuple

import pygame


class GameObject(pygame.sprite.Sprite):
    _instance = set()

    def __init__(
        self,
        image: "pygame.Surface",
        center_pos: Tuple[int, int] = (0, 0)
    ):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pygame.Vector2(center_pos)
        # Will be used to rotate the sprite.
        self.orig_img = self.image
        # Radius vector.
        # Used for collision detection.
        self.r_vec = pygame.Vector2(self.image.get_width() / 2)
        GameObject._instance.add(self)

    def draw(self, surface: "pygame.Surface"):
        pos = self.rect.center - self.r_vec
        surface.blit(self.image, pos)

    def collides_with(self, game_obj: "GameObject"):
        dist = self.rect.center.distance_to(game_obj.rect.center)
        return dist < self.radius + game_obj.radius

    @classmethod
    def update_all(cls, delta_time: float):
        for inst in cls._instance:
            if hasattr(inst, "update"):
                inst.update(delta_time)

    @classmethod
    def draw_all(cls, surface: "pygame.Surface"):
        for inst in cls._instance:
            inst.draw(surface)#

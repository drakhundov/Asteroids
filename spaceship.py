import math
from typing import Tuple

import pygame

from game_object import GameObject


class Spaceship(GameObject):
    def __init__(
        self,
        image: "pygame.Surface",
        center_pos: Tuple[int, int] = (0, 0),
        accel: int = 0,
        max_accel: int = 0,
        rot_vel: int = 0,
    ):
        super().__init__(image, center_pos)
        self.accel = accel
        self.max_accel = max_accel
        self.is_accel = True
        self.accel_dir = 1
        self.rot_vel = rot_vel
        self.vel_vec = pygame.Vector2(0, 0)
        self.rot = 30
        self.rotate(1, 1)
        self.move(1)

    def update(self, delta_time: float):
        print(self.vel_vec)
        if math.sqrt(self.vel_vec * self.vel_vec) <= self.max_accel:
            rad_rot = self.rot / 180 * math.pi
            self.vel_vec += (
                (self.accel * delta_time * (1 if self.is_accel else -1))
                % self.max_accel
            ) * pygame.Vector2(math.cos(rad_rot), math.sin(rad_rot))
        if self.vel_vec.x < 0 and self.vel_vec.y < 0:
            self.vel_vec = pygame.Vector2(0, 0)
        else:
            self.move(delta_time)

    def rotate_right(self, delta_time: float):
        self.rotate(1, delta_time)

    def rotate_left(self, delta_time: float):
        self.rotate(-1, delta_time)

    def rotate(self, dir: int, delta_time: float):
        """
        dir == 1 - right
        dir == -1 - left
        """
        self.rot = (self.rot + self.rot_vel * dir * delta_time) % 360
        self.image = pygame.transform.rotate(self.orig_img, -self.rot)
        self.rect = self.image.get_rect(center=self.rect.center)

    def set_accel_state(self, state: bool):
        self.is_accel = state

    def move(self, delta_time: float):
        self.rect.center += self.vel_vec * delta_time

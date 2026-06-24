import random

import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self) -> None:
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            log_event("asteroid_split")

            split_one_velocity = pygame.Vector2(0, 1)
            split_two_velocity = pygame.Vector2(0, 1)
            split_one_direction = split_one_velocity.rotate(random.uniform(20, 50))
            split_two_direction = split_two_velocity.rotate(-random.uniform(20, 50))
            split_radius = self.radius - ASTEROID_MIN_RADIUS
            split_one = Asteroid(self.position.x, self.position.y, split_radius)
            split_one.velocity = split_one_direction * 10.2
            split_two = Asteroid(self.position.x, self.position.y, split_radius)
            split_two.velocity = split_two_direction * 100.2
            self.kill()

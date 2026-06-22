import sys

import pygame

from asteroid import Asteroid
from logger import log_state, log_event
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from player import Player
from asteroidfield import AsteroidField

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    width_ = SCREEN_WIDTH / 2
    height_ = SCREEN_HEIGHT / 2
    player = Player(width_, height_)
    asteroid_field = AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        pygame.Surface.fill(screen, "black")
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print ("Game Over!")
                sys.exit()

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000.0  # Limit to 60 FPS and get delta time in seconds


if __name__ == "__main__":
    main()

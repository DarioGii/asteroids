import pygame
from logger import log_state
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from player import Player


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
    Player.containers = (updatable, drawable)
    width_ = SCREEN_WIDTH / 2
    height_ = SCREEN_HEIGHT / 2
    player = Player(width_, height_)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        pygame.Surface.fill(screen, "black")
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0  # Limit to 60 FPS and get delta time in seconds



if __name__ == "__main__":
    main()

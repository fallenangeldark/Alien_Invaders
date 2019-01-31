import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    # Инициализирует pygame, settings и объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invaders")
    # Назначение цвета фона
    ship = Ship(screen)
    while True:
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            screen.fill(ai_settings.bg_color)
            ship.blitme()
            if event.type == pygame.QUIT:
                sys.exit()

        # Отображение последнего прорисованного экрана
        pygame.display.flip()

run_game()

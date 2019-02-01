import sys
import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf

def run_game():
    # Инициализирует pygame, settings и объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invaders")
    # Назначение цвета фона
    ship = Ship(ai_settings, screen)
    while True:
        # Отслеживание событий клавиатуры и мыши.
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

        # Отображение последнего прорисованного экрана
        pygame.display.flip()

run_game()

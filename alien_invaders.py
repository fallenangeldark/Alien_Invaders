import sys
import pygame
from settings import Settings
from ship import Ship
# from alien import Alien
from pygame.sprite import Group
import game_functions as gf

def run_game():
    # Инициализирует pygame, settings и объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invaders")
    # Создание корабля, группы пуль и группы пришельцев.
    ship = Ship(ai_settings, screen)
    # alien = Alien(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # Создание флота пришельцев.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    while True:
        # Отслеживание событий клавиатуры и мыши.
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

        # Отображение последнего прорисованного экрана
        pygame.display.flip()

run_game()

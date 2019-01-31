import sys
import pygame

def run_game():
    # Инициализирует игру и создает объект экрана
    pygame.init()
    screen = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("Alien Invaders")
    # Назначение цвета фона
    bg_color = (230, 230, 230)
    while True:
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            screen.fill(bg_color)
            if event.type == pygame.QUIT:
                sys.exit()

        # Отображение последнего прорисованного экрана
        pygame.display.flip()

run_game()

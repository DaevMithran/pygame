import random
import sys

import pygame
from pygame.math import Vector2


class Fruit:
    def __init__(self):
        # random positions within screen
        self.x = random.randint(cell_size, cell_area - 1)
        self.y = random.randint(cell_size, cell_area - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        # create a rect
        fruit_rect = pygame.Rect(int(self.pos.x), int(self
                                                      .pos.y), cell_size, cell_size)
        pygame.draw.rect(screen, (255, 0, 0), fruit_rect)


pygame.init()

cell_size = 40
cell_number = 20
cell_area = cell_size * cell_number
screen = pygame.display.set_mode((cell_number * cell_size, cell_area))
fruit = Fruit()

running = True
# while loop runs as fast as the computer can run it
# this can be inconsistent, so fixing a maximum speed will be ideal
clock = pygame.time.Clock()
framerate = 60

# surface
snake_surface = pygame.Surface((100, 200))
snake_rect = snake_surface.get_rect(center=(400, 300))


# snake
def snake():
    screen.blit(snake_surface, snake_rect)


while running:
    screen.fill((155, 200, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    snake()
    fruit.draw_fruit()
    pygame.display.update()
    clock.tick(framerate)

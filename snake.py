import random
import pygame
from pygame.locals import *


def on_grid_random():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return x//10 * 10, y//10 * 10  # // é uma divisão por inteiro 277 / 10 será 27 e não 27,7


def collision(p1, p2):
    return p1[0] == p2[0] and p1[1] == p2[1]


def collision_wall(p1):
    return True


UP = 0
RIGTH = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))  # cria uma tela de 600px por 600px
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220, 200)]  # criar a cobra com 3 segmentos
snake_skin = pygame.Surface((10, 10))  # o surface criar um objeto na tela, nesse caso um quadrado de 10px por 10px
snake_skin.fill((255, 255, 255))  # o fill pinta o objeto criado

apple_pos = on_grid_random()
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))

my_direction = LEFT

clock = pygame.time.Clock()

while True:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGTH
            if event.key == K_LEFT and my_direction != RIGTH:
                my_direction = LEFT

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0, 0))

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    # snake[0] é a cabeça da cobra || (snake[0][0], snake[0][1]) = x e y
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGTH:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)  # printa o objeto na tela na posição informada

    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()

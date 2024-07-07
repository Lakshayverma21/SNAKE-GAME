import pygame
import time
import random

pygame.init()

# Colors
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)

# Window dimensions
win_width = 600
win_height = 400
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Snake Game")

snake_block = 10
snake_speed = 15

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("calibri", 26)
score_font = pygame.font.SysFont("comicsansms", 30)

# Function to display score
def user_score(score):
    number = score_font.render("SCORE: " + str(score), True, red)
    window.blit(number, (0, 0))

# Function to display messages
def message(msg):
    mesg = font_style.render(msg, True, red)
    window.blit(mesg, [win_width / 16, win_height / 3])

# Function to draw the snake
def game_snake(color, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, color, [x[0], x[1], snake_block, snake_block])

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    # Initial snake position
    x1 = win_width / 2
    y1 = win_height / 2

    # Initial movement
    x1_change = 0
    y1_change = 0

    # Initial snake length
    snake_list = []
    snake_length = 1

    # Initial food position
    foodx = round(random.randrange(0, win_width - snake_block) / 10.0) * 10
    foody = round(random.randrange(0, win_height - snake_block) / 10.0) * 10

    while not game_over:

        while game_close:
            window.fill(black)
            message("You Lost! Press P to Play Again or Q to Quit")
            user_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        window.fill(black)
        pygame.draw.rect(window, yellow, [foodx, foody, snake_block, snake_block])

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        game_snake(green, snake_list)
        user_score(snake_length - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, win_width - snake_block) / 10.0) * 10
            foody = round(random.randrange(0, win_height - snake_block) / 10.0) * 10
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
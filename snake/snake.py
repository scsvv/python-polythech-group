from distutils import text_file
from email.mime import image
import pygame
from pygame.locals import *
from sys import exit
from random  import randint

pygame.init()

# 
pygame.display.set_caption("Snake")
screen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()


SPEED = 10
DIRECTION = [SPEED, 0]
COLOR = (255, 255, 255)
GAME_POINT = 0
font = pygame.font.SysFont(None, 32)

def score():
    global GAME_POINT, COLOR
    text = font.render(f'Score: {GAME_POINT}', True, COLOR)
    text_rect = text.get_rect(center=(540, 700))
    screen.blit(text, text_rect)

def load_img(src, x, y):
    image = pygame.image.load(src).convert()
    image = pygame.transform.scale(image, (30, 30))
    rect = image.get_rect(center=(x,y))
    transparent = image.get_at((0, 0))
    image.set_colorkey(transparent)
    return image, rect

def pickup():
    global apple_rect, head_rect, GAME_POINT, snake

    if head_rect.colliderect(apple_rect):
        apple_rect.x = randint(40, 1000)
        apple_rect.y = randint(40, 680)
        GAME_POINT += 10
        snake.append(snake[1].copy())
        

def rand_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

def move(obj):
    global DIRECTION, SPEED, COLOR, KEYS

    if KEYS[K_UP] or KEYS[K_w]:
        DIRECTION = [0, -SPEED]
    elif KEYS[K_DOWN] or KEYS[K_s]:
        DIRECTION = [0, SPEED]
    elif KEYS[K_RIGHT] or KEYS[K_d]:
        DIRECTION = [SPEED, 0]
    elif KEYS[K_LEFT] or KEYS[K_a]:
        DIRECTION = [-SPEED, 0]

    if obj.bottom > 720:
        obj.top = 0
    elif obj.top < 0:
        obj.bottom = 720
    elif obj.left < 0:
        obj.right = 1080
    elif obj.right > 1080:
        obj.left = 0
    
    for i in range( len(snake) - 1, 0, -1):
        snake[i].x = snake[i-1].x
        snake[i].y = snake[i-1].y
    
    obj.move_ip(DIRECTION)



head_image, head_rect = load_img('./img/head.png', 400, 300) 
apple_image, apple_rect = load_img('./img/apple.png', 200, 200) 
body_image, body_rect = load_img('./img/body.png', 370, 300) 

snake = [head_rect, body_rect]

while True:
    screen.fill( (0, 0, 0) )
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    KEYS = pygame.key.get_pressed()
    screen.blit(head_image, head_rect)
    screen.blit(apple_image, apple_rect)

    for el in snake[1:]:
        screen.blit(body_image, el)

    move(head_rect)
    pickup()
    score()
    pygame.display.update()
    clock.tick(30)
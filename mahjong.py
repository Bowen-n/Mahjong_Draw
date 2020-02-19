import pygame
from pygame.locals import *

from board import Board

SCREEN_SIZE = 980, 650

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Mahjong')

background = pygame.image.load('./res/background.jpg')
gameover = pygame.image.load('./res/gameover.jpg')
success = pygame.image.load('./res/success_test.png')
board = Board()

status = 0

while True:
    
    screen.fill(0)
    screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed_array = pygame.mouse.get_pressed()
            position = pygame.mouse.get_pos() # mouse pos
            for index in range(len(pressed_array)):
                if pressed_array[index]:
                    if index == 0: # left 
                        status = board.choose(position)
                    elif index == 2: # right
                        status = board.pop(position)

    
    board.display(screen)
    if status is not 0:
        break
    
    pygame.display.update()

if status == -1:
    screen.blit(gameover, (700, 550))
if status == 1:
    screen.blit(success, (400, 550))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()

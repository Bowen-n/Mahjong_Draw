import pygame
from pygame.locals import *

from board import Board

SCREEN_SIZE = 800, 600

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Mahjong')

background = pygame.image.load('./res/background.jpg')
board = Board()

while True:
    
    screen.fill(0)
    screen.blit(background, (0, 0))
    board.display(screen)

    key_pressed = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            board.pop(position, screen)
    
    pygame.display.update()

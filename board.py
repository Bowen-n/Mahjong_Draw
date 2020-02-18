import math
import os
import random
import sys

import pygame
from pygame.locals import *

# CONSTANTS
TOTALS = 137 # 8 * 17
ROW = 8
COL = 17
TILE_ROW = 41
TILE_COL = 53


class Tile:
    def __init__(self, name, img):
        self.name = name
        self.img = img


class Board:

    def __init__(self):

        self.tile_in_hand = []
        self.tile_list = []

        # read all images
        files = os.listdir('./res/tile')
        for file in files:
            for i in range(4):
                path = os.path.join('./res/tile', file)
                img = pygame.image.load(path)
                name = file.split('.')[0]
                tile = Tile(name, img)
                self.tile_list.append(tile)

        # shuffle and store in col_list
        random.shuffle(self.tile_list)
        self.col_list = []
        for i in range(0, len(self.tile_list), ROW):
            self.col_list.append(self.tile_list[i:i+ROW])

        
    def display(self, screen):

        # board
        pos_row = 50
        for col in self.col_list:
            pos_col = 450
            for item in col:
                screen.blit(item.img, (pos_row, pos_col))
                pos_col -= TILE_COL
            pos_row += TILE_ROW

        # tile in hand
        pos_row = 300
        for tile in self.tile_in_hand:
            screen.blit(tile.img, (pos_row, 540))
            pos_row += TILE_ROW


    def pop(self, pos, screen):
        col_index = math.floor((pos[0]-50)/41)
        row_index = math.floor((503 - pos[1])/53)
        if col_index >= 0 and col_index < len(self.col_list) and \
            row_index >= 0 and row_index == len(self.col_list[col_index])-1:
            
            tile = self.col_list[col_index].pop(len(self.col_list[col_index])-1)
            self.tile_in_hand.append(tile)
            # update tile in hand
            self.tile_in_hand = self._check_in_hand()
            if self._check_succeed():
                print('Success!')
                sys.exit()
            if self._check_fail():
                print('Failed!')
                sys.exit()


    def get_len(self):
        return len(self.tile_list)

    
    def _top(self, col_index):
        return self.col_list[col_index][len(self.col_list[col_index])-1]


    def _top_two_same(self, col_index):
        length = len(self.col_list[col_index])
        if self.col_list[col_index][length-1] == self.col_list[col_index][length-2]:
            return True
        else:
            return False


    def _check_in_hand(self):
        # 0 1 2 3 4
        tile_in_hand_new = []
        repeat1, repeat2 = self._find_same_item(self.tile_in_hand)

        if repeat1 == -1 and repeat2 == -1:
            return self.tile_in_hand

        for index in range(len(self.tile_in_hand)):
            if index != repeat1 and index != repeat2:
                tile_in_hand_new.append(self.tile_in_hand[index])
        
        return tile_in_hand_new
    

    def _check_fail(self):

        # top two same
        for col_index in range(COL):
            if(len(self.col_list[col_index])>1):
                if self._top_two_same(col_index):
                    return False

        top_and_hand = []

        num_in_hand = len(self.tile_in_hand)
        for col_index in range(COL):
            if len(self.col_list[col_index]) > 0:
                top_and_hand.append(self._top(col_index))
        for tile in self.tile_in_hand:
            top_and_hand.append(tile)
        
        repeat1, repeat2 = self._find_same_item(top_and_hand)

        # uncomment the follow code to print hint
        # print('repeat1:{}, repeat2:{}, tile_in_hand:{}'.format(repeat1, repeat2, len(self.tile_in_hand)))

        if repeat1 == -1 and repeat2 == -1 and len(self.tile_in_hand) == 3:
            return True # failed
        else:
            return False


    def _check_succeed(self):
        for col in self.col_list:
            if len(col) > 0:
                return False
        if len(self.tile_in_hand) > 0:
            return False
        return True
        

    def _find_same_item(self, array):
        repeat1 = -1; repeat2 = -1
        for i in range(len(array)-1):
            for j in range(i+1, len(array)):
                if array[i].name == array[j].name:
                    repeat1 = i; repeat2 = j
                    break
        return repeat1, repeat2


    def _print_in_hand(self):
        for tile in self.tile_in_hand:
            print(tile.name)
        print('\n')

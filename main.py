import numpy as np
import math
import random
import pygame
from puzzle import Puzzle
import sys



def __main__():
    puzzle = Puzzle()

    pygame.init()

    screen_width, screen_height = 600, 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    white = (255, 255, 255)
    black = (0, 0, 0)

    tile_width = screen_width // 3
    tile_height = screen_height // 3

    puzzle.scramble(1000)
    puzzle_tiles = puzzle.puzzle

    selected_tile = None

    running = True
    while running:
        screen.fill(white)
        for x in range(1, 3):
            pygame.draw.line(screen, black, (x * tile_width, 0), (x * tile_width, screen_height), 2)
        for y in range(1, 3):
            pygame.draw.line(screen, black, (0, y * tile_height), (screen_width, y * tile_height), 2)
        



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                tile_x = mouse_x // tile_width
                tile_y = mouse_y // tile_height

                if 0 <= tile_x < 3 and 0 <= tile_y < 3:
                    selected_tile = (tile_x, tile_y)
                    puzzle_pos = (tile_y,tile_x)
                    if puzzle_pos in puzzle.get_movable_pieces():
                        puzzle._swap(puzzle_pos, puzzle._get_empty_tile())
            elif event.type == pygame.MOUSEBUTTONUP:

                selected_tile = None

        for i in range(3):
            for j in range(3):
                if puzzle_tiles[i,j] == 0:
                    rect = pygame.Rect(j*200, i*200, 200,200)
                    pygame.draw.rect(screen, black, rect)
                else:
                    number_font = pygame.font.SysFont( None, 16 ) 
                    number_text  = str(puzzle_tiles[i,j])
                    number_image = number_font.render( number_text, True, black, white )
                    screen.blit( number_image, ( j*200 + 100, i*200 + 100) )
        
        if selected_tile is not None:
            tile_x, tile_y = selected_tile
            pygame.draw.rect(screen, (200, 200, 200), (tile_x * tile_width, tile_y * tile_height, tile_width, tile_height))

        pygame.display.flip()



__main__()
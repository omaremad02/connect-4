import math

import numpy as np
import pygame
import sys

# Defining Colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Defining the game dimensions
ROW_COUNT = 6
COLUMN_COUNT = 7


def createBoard():
    newBoard = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return newBoard


def dropPiece(board, row, column, piece):
    board[row][column] = piece


def isLocationValid(board, column):
    # Checking if the last row in the selected column is filled
    return board[ROW_COUNT - 1][column] == 0


def getFreeRow(board, column):
    # Loop to check for the deepest free row in the selected column
    for r in range(ROW_COUNT):
        if board[r][column] == 0:
            return r


def printBoard(board):
    print(np.flip(board, 0))


def drawBoard(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARE_SIZE, r * SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, BLACK, (
                int(c * SQUARE_SIZE + SQUARE_SIZE / 2), int(r * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (
                    int(c * SQUARE_SIZE + SQUARE_SIZE / 2), height - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (
                    int(c * SQUARE_SIZE + SQUARE_SIZE / 2), height - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
    pygame.display.update()


def checkForWin(board, piece):
    # Check horizontal win
    for row in range(ROW_COUNT):
        for col in range(COLUMN_COUNT - 3):
            # Check if all consecutive cells in the row have the same value as 'piece'
            if all(board[row][col + i] == piece for i in range(4)):
                return True

    # Check vertical win
    for row in range(ROW_COUNT - 3):
        for col in range(COLUMN_COUNT):
            # Check if all consecutive cells in the column have the same value as 'piece'
            if all(board[row + i][col] == piece for i in range(4)):
                return True

    # Check diagonal (right) win
    for row in range(ROW_COUNT - 3):
        for col in range(COLUMN_COUNT - 3):
            # Check if all consecutive cells in the diagonal (right) have the same value as 'piece'
            if all(board[row + i][col + i] == piece for i in range(4)):
                return True

    # Check diagonal (left) win
    for row in range(ROW_COUNT - 3):
        for col in range(3, COLUMN_COUNT):
            # Check if all consecutive cells in the diagonal (left) have the same value as 'piece'
            if all(board[row + i][col - i] == piece for i in range(4)):
                return True


board = createBoard()
printBoard(board)
game_over = False
turn = 0

# Initialize Pygame
pygame.init()

SQUARE_SIZE = 100
width = COLUMN_COUNT * SQUARE_SIZE
height = (ROW_COUNT + 1) * SQUARE_SIZE
size = (width, height)
RADIUS = int(SQUARE_SIZE / 2 - 5)

screen = pygame.display.set_mode(size)
drawBoard(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))
            x_position = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (x_position, int(SQUARE_SIZE / 2)), RADIUS)
            elif turn == 1:
                pygame.draw.circle(screen, YELLOW, (x_position, int(SQUARE_SIZE / 2)), RADIUS)
        pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            # Ask for Player 1 Input
            if turn == 0:
                x_position = event.pos[0]
                column = int(math.floor(x_position / SQUARE_SIZE))

                if isLocationValid(board, column):
                    row = getFreeRow(board, column)
                    dropPiece(board, row, column, 1)

                    if checkForWin(board, 1):
                        pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))
                        label = myfont.render("Player 1 wins!", 1, RED)
                        screen.blit(label, (40, 10))
                        game_over = True



            # Ask for Player 2 Input
            else:
                x_position = event.pos[0]
                column = int(math.floor(x_position / SQUARE_SIZE))

                if isLocationValid(board, column):
                    row = getFreeRow(board, column)
                    dropPiece(board, row, column, 2)

                    if checkForWin(board, 2):
                        pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))
                        label = myfont.render("Player 2 wins!", 1, YELLOW)
                        screen.blit(label, (40, 10))
                        game_over = True

            printBoard(board)
            drawBoard(board)
            turn += 1
            turn = turn % 2

            if game_over is True:
                pygame.time.wait(5000)

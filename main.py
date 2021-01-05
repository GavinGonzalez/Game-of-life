from time import sleep
import numpy as np
from random import randint
import pygame
import sys
import random
import time
import copy


pygame.init()
clock = pygame.time.Clock()

def create_shape(shape):
	return np.zeros(shape)

def plot_cell(point, shape):
	shape[point[0]][point[1]] = 1;
	


def random_cells(gameBoard):
	for i in range(50):
		x = random.randint(0, 19)
		y = random.randint(0, 19)

		gameBoard[x][y] = 1
	
def draw_grid(w, r, surface):
	rows = 40
	size = w // r
	x = 0
	y = 0
	for i in range(r):
		x = x + size
		y = y + size

		pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
		pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))

def redrawWindow():
	screen = pygame.display.set_mode((800, 800))
	screen.fill((40, 0, 0))
	draw_grid(800, 20, screen)

def print_cell(surface, color, point, w, gameBoard):
	#pygame.draw.rect(surface, color, (l*shape[point[0
	if gameBoard[point[0]][point[1]]:
		pygame.draw.rect(surface, color, (point[0]*w, point[1]*w, w, w))

def cell_glider(gameBoard):
	gameBoard[6][8] = 1;
	gameBoard[7][8] = 1;
	gameBoard[8][8] = 1;
	gameBoard[10][8] = 1;
	gameBoard[10][7] = 1;
	
	gameBoard[11][8] = 1;
	gameBoard[11][7] = 1;
	gameBoard[11][6] = 1;
	
def num_of_neighbors(point, gameBoard):
	alive_cells = 0
	r_num = len(gameBoard)
	c_num = len(gameBoard[0])

	

	if point[0]-1 > -1 and gameBoard[point[0]-1][point[1]] == 1:
		alive_cells = alive_cells + 1

	if point[1]-1 > -1 and gameBoard[point[0]][point[1]-1] == 1:
		alive_cells = alive_cells + 1

	if point[0]-1 > -1 and point[1]-1 > -1 and gameBoard[point[0]-1][point[1]-1] == 1:
		alive_cells = alive_cells + 1

	if point[0]+1 < c_num and point[1]-1 > -1 and gameBoard[point[0]+1][point[1]-1] == 1:
		alive_cells = alive_cells + 1

	if point[0]+1 < c_num and gameBoard[point[0]+1][point[1]] == 1:
		alive_cells = alive_cells + 1

	if point[0]-1 > -1 and point[1]+1 < r_num and gameBoard[point[0]-1][point[1]+1] == 1:
		alive_cells = alive_cells + 1

	if point[0]+1 < c_num and point[1]+1 < r_num and gameBoard[point[0]+1][point[1]+1] == 1:
		alive_cells = alive_cells + 1

	if point[1]+1 < r_num and gameBoard[point[0]][point[1]+1] == 1:
		alive_cells = alive_cells + 1
	
	return alive_cells	

def check(neighbors, point, gameBoard):

	if gameBoard[point[0]][point[1]] == 1 and (neighbors == 2 or neighbors == 3):
		gameBoard[point[0]][point[1]] = 1

	elif gameBoard[point[0]][point[1]] == 0 and neighbors == 3:
		gameBoard[point[0]][point[1]] = 1

	else:
		
		gameBoard[point[0]][point[1]] = 0


def main():
	arr = create_shape((20, 20)).astype(int)
	num = create_shape((20, 20)).astype(int)
		#random_cells(arr)
	cell_glider(arr)
	run = True
	
	screen = pygame.display.set_mode((800, 800))
	
	while(True):
		redrawWindow()
		
        
		for x in range(len(arr)):
			for y in range(len(arr[0])):
				num[x][y] = num_of_neighbors((x, y), arr)
						
		for x in range(len(arr)):
			for y in range(len(arr[0])):
				check(num[x][y], (x, y), arr)		
				print_cell(screen, (255, 255, 255), (x, y), 40, arr)		 		
				

		
     
		
        

		pygame.display.update()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			######run = True

			if event.type == pygame.KEYDOWN:
				if event.type == pygame.K_a:
					run = False

			if event.type == pygame.KEYDOWN:
				if event.type == pygame.K_b:
					run = True

			if event.type == pygame.MOUSEBUTTONDOWN:
				movement = pygame.mouse.get_pos()
				mouse_c = movement[0]
				mouse_r = movement[1]

				counter_c = 0
				counter_r = 0
				r = 0
				c = 0
				while(counter_c < mouse_c):
					counter_c+=40
					c = c+1

				while(counter_r < mouse_r):
					counter_r+=40
					r = r+1



				mouse_pos = (c-1, r-1)
				plot_cell(mouse_pos, arr)
				


		clock.tick(6)		
if __name__ == '__main__':
	main()

#!/usr/bin/env python3

#This modules contains class responsible for creating the game board.

#Below are number codes for tiles on board object:
#0 is a number for empty tile
#1 is a number for tile with a food
#2 is a number for player tile
#3 is a number for computer tile

import random

class Board(): #This class handles the game board

	def __init__(self, board_size): #Contructor gets single integer which dictates the size of board made of 2d array
		self.board_size = board_size
		self.board = []
		for i in range(board_size):
		    self.board.append([0] * board_size)


	def Fill(self): #This functions fills the board with a food at random places.
		for i in range(self.board_size):
			for j in range(self.board_size):
				if random.randint(0,10) == 1 and self.board[i][j] == 0:
					self.board[i][j] = 1	

	
	def CheckTile(self, posx, posy):
		if self.board[posx][posy] == 0:
			return 0 #Empty tile
		elif self.board[posx][posy] == 1:
			return 1 #Food tile
		elif self.board[posx][posy] == 2:
			return 2 #Player tile
		elif self.board[posx][posy] == 3:
			return 3 #Computer tile

	def ChangeTileState(self, posx, posy, tile_state): #This function changes given tile state i.e. when new player speciman appears on the tile it changes from 0 to 2
		self.board[posx][posy] = tile_state
			

			
########################################################################################		
#################################CREATED FOR TEST PURPOSES##############################
########################################################################################
def main():
	pass

if __name__ == '__main__':
	main()
#!/usr/bin/env python3
#EvoSim v.0.1
#Main module. Handles highest level of abstraction.

import EvoSimBoard
import EvoSimSpec
import EvoSimDisplay
import EvoSimGameLogic
import time

def GameEnd(player_specimen, computer_specimen, turns):
	if len(player_specimen) > 0 and len(computer_specimen) < 1:
		EvoSimDisplay.EndGameDisplay(player_specimen, turns)
	elif len(computer_specimen) > 0 and len(player_specimen) < 1:
		EvoSimDisplay.EndGameDisplay(computer_specimen, turns)
	else:
		EvoSimDisplay.EndGameDisplay(0, turns)



def GameTurn(game_board, player_specimen, computer_specimen, turns): #This function procceses single turn of the game.
	if turns % 32 == 0: #Refills board with food.
		EvoSimBoard.Board.Fill(game_board) #Fills the created board with a food.

	i = 0
	while True: #This loop continues for as long as there are unmoved specimen.
		player_turn_ended = False
		computer_turn_edned = False
		if i < len(player_specimen): #Performs moves for player_species as long as there are species in the list.
			if player_specimen[i].predator == True:
				player_specimen[i].turns_left -= 2
			else:
				player_specimen[i].turns_left -= 1
			conflict, fed = EvoSimGameLogic.MoveSpeciman(game_board, player_specimen[i], 2)
			if (conflict == True or fed == True): 
				EvoSimGameLogic.PostMove(game_board, player_specimen, computer_specimen, player_specimen[i], conflict, fed, 2)
			elif player_specimen[i].turns_left < 1:
					game_board.ChangeTileState(player_specimen[i].positionx, player_specimen[i].positiony, 0)
					player_specimen.pop(i)
		else:
			player_turn_ended = True #Variable is set to True when all specimen performed during this turn.
		if i < len(computer_specimen): #Performs moves for computer_species as long as there are species in the list.
			if computer_specimen[i].predator == True:
				computer_specimen[i].turns_left -= 2
			else:
				computer_specimen[i].turns_left -= 1
			conflict, fed = EvoSimGameLogic.MoveSpeciman(game_board, computer_specimen[i], 3)
			if (conflict == True or fed == True): 
				EvoSimGameLogic.PostMove(game_board, player_specimen, computer_specimen, computer_specimen[i], conflict, fed, 3)
			elif computer_specimen[i].turns_left < 1:
				game_board.ChangeTileState(computer_specimen[i].positionx, computer_specimen[i].positiony, 0)
				computer_specimen.pop(i)

		else:
			computer_turn_edned = True  #Variable is set to True when all specimen performed during this turn.
		if player_turn_ended == True and computer_turn_edned == True: #Once both sides performed actions with all their speciman, turn ends.
			return
		i += 1

def InitiateGameObjects(): #This functions creates game objects: game_board on which game is played and specimen lists which will contains specimen.
	player_specimen = [] #List will contain future specimen of a player
	computer_specimen = [] #List will contain future specimen of a computer
	game_board = EvoSimBoard.Board(EvoSimGameLogic.SetBoardSize()) #Creates the game board object with a size given in SetBoardSize function.
	player_specimen.append(EvoSimGameLogic.CreatePlayerSpecies(game_board)) #Creates first instance of the player species
	computer_specimen.append(EvoSimGameLogic.CreateComputerSpecies(game_board)) #Creates first instance of the computer species
	EvoSimBoard.Board.Fill(game_board) #Fills the created board with a food.
	return player_specimen, computer_specimen, game_board

def Gameplay():
	player_specimen, computer_specimen, game_board = InitiateGameObjects()
	player_name = player_specimen[0].name
	computer_name = computer_specimen[0].name
	player_attrs = [ player_specimen[0]. strength, player_specimen[0].speed, player_specimen[0].resistance, player_specimen[0].predator ]
	computer_attrs = [ computer_specimen[0]. strength, computer_specimen[0].speed, computer_specimen[0].resistance, computer_specimen[0].predator ]
	EvoSimDisplay.GamePreviewDisplay(player_specimen[0], computer_specimen[0])
	turns = 0
	while True:
		turns += 1
		GameTurn(game_board, player_specimen, computer_specimen, turns)
		EvoSimDisplay.DisplayBoard(game_board)
		EvoSimDisplay.DisplayStats(turns, len(player_specimen), len(computer_specimen), player_name, computer_name)
		time.sleep(1) #Creates a pause between turns. Can be modified 
		if (len(player_specimen) == 0 or len(computer_specimen) == 0):
			GameEnd(player_specimen, computer_specimen, turns)
			return
def GameMenu():
	Gameplay()

def main():
	GameMenu()
	EvoSimDisplay.ClearScreen()

if __name__ == '__main__':
	main()
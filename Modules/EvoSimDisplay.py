#!/usr/bin/env python3

#This modules cointains functions responsible for displaying content. Should avoid fonctions responsible for any game logic.

#Below are number codes for tiles on board object:
#0 is a number for empty tile
#1 is a number for tile with a food
#2 is a number for player tile
#3 is a number for computer tile

import EvoSimBoard
import os
from colorama import Fore



def ClearScreen(): #Clears terminal screen, depending on OS.
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
########################################################################################		
######################BLOCK OF FUNCTIONS PRINTING SHORT STATEMENTS######################
########################################################################################
def EndGameDisplay(specimen, turns):
	trs = turns
	ClearScreen()
	if specimen:
		print(specimen[0].name + " has won after " + str(trs) + " turns!")
	elif specimen == 0:
		print("Non of the species survived the game!")
	input("Pres ENTER to continue...")

def GetNameDisplay(): #Function displays query for a name setting
	ClearScreen()
	print("Choose name for Your species(Between 3 to 32 characters): ", end = ' ')
	name = input()
	return name

def GetNameErrorDisplay(): #Function displays error if name requirements haven't been met.
	ClearScreen()
	print("Given name doesn't meet the requirements!", end = "\n\n")
	print("Press ENTER to continue...")
	input()

def GetAttributeDisplay(points_rest, attr_name): #Function displays query for a strength setting
	ClearScreen()
	pr = points_rest
	print("Available points: " + str(pr), end = "\n\n")
	print("Set " + attr_name + " of Your species: ", end = ' ')
	user_input = input()
	return user_input

def GetAttributeErrorDisplay(): #Function displays error if value is higher than possible points to distribute.
	ClearScreen()
	print("Not enough points!", end = "\n\n")
	print("Press ENTER to continue...")
	input()

def GetPredatorDisplay(): #Function displays query for a predator option setting
	ClearScreen()
	print("Do you want Your species to be predator? (Y/N): ", end = ' ')
	user_input = input()
	return user_input

def GetPredatorErrorDisplay(): #Function displays error if the wrong type has been given by a user.
	ClearScreen()
	print("Please insert either letter Y or N!", end = "\n\n")
	print("Press ENTER to continue...")
	input()

def GetBoardSizeDisplay(): #Displays query for integer number to set board size and returns number given by user.
	ClearScreen()
	print("Set the size of a game board(between 8 and 24 tiles): ")
	user_input = input()
	return user_input

def NonIntegerErrorDisplay(): #Is displayed if user gave non-int.
	ClearScreen()
	print("Given value is not an integer!", end = "\n\n")
	print("Press ENTER to continue...")
	input()


def WrongValueErrorDisplay(): #Is displayed is user gave wrong value size for setting board size.
	ClearScreen()
	print("Please input value between 8 and 36!", end = "\n\n")
	print("Press ENTER to continue...")
	input()
########################################################################################		
################BLOCK OF FUNCTIONS RESPONSIBLE FOR DISPLAYING GAME BOARD################
########################################################################################
def GamePreviewDisplay(player, computer):
	ClearScreen()
	pname = player.name
	pstrength = player.strength
	pspeed = player.speed
	priststance = player.resistance
	if player.predator == True:
		ppredator = "Yes"
	else:
		ppredator = "No"

	cname = computer.name
	cstrength = computer.strength
	cspeed = computer.speed
	criststance = computer.resistance
	if computer.predator == True:
		cpredator = "Yes"
	else:
		cpredator = "No"

	print(pname + ": " + str(pstrength) + " " + str(pspeed) + " " + str(priststance) + " Predator: " + ppredator)
	print(cname + ": " + str(cstrength) + " " + str(cspeed) + " " + str(criststance) + " Predator: " + cpredator)
	input("Pres ENTER to continue...")


def DisplayStats(turns, player_specimen_numb, computer_specimen_numb, player_name, computer_name):
	trs = turns
	playernumb = player_specimen_numb
	computernumb = computer_specimen_numb
	print("Turns:	" + str(trs))
	print(player_name + " count:	" + str(playernumb))
	print(computer_name + " count:	" + str(computernumb))

def PrintBorder(board_size, border): #Creates borders that match size of the board
	for i in range(board_size + 2): 
		print(border, end = ' ')
	print('')

def DisplayBoard(board):
	border = 'X' #Border symbol

	ClearScreen()
	PrintBorder(board.board_size, border) #Prints upper border

	for i in range(board.board_size):
		print(border, end = ' ') #Prints border at the beginning of every line
		for j in range(board.board_size):
			if board.board[i][j] == 0:
				print(' ', end = ' ') #Prints symbol for the background
			elif board.board[i][j] == 1: #Prints symbol for the food
				print('*', end = ' ')
			elif board.board[i][j] == 2: #Prints symbol for the player
				print(Fore.GREEN + '@' + Fore.WHITE, end = ' ')
			elif board.board[i][j] == 3: #Prints symbol for the computer
				print(Fore.RED + '%' + Fore.WHITE, end = ' ')
		print(border) #Prints border at the end of every line

	PrintBorder(board.board_size, border) #Prints bottom border

########################################################################################		
#################################CREATED FOR TEST PURPOSES##############################
########################################################################################
def main():
	pass


if __name__ == '__main__':
	main()

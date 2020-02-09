#!/usr/bin/env python3

#This module contains functions responsible for game logic. Should avoid putting any functions responsible for displaying any content!

#Below are number codes for tiles on board object:
#0 is a number for empty tile
#1 is a number for tile with a food
#2 is a number for player tile
#3 is a number for computer tile

import EvoSimDisplay
import EvoSimSpec
import EvoSimBoard
import random

########################################################################################		
#####################################VARIOUS FUNCTIONS##################################
########################################################################################

########################################################################################		
######################BLOCK OF FUNCTIONS RESPONSIBLE FOR  GAMEPLAY######################
########################################################################################
def Combat(board, speciman, player_specimen, computer_specimen, speciman_type):
	input("Fight!")
	if speciman_type == 2: #Checks if the speciman is a player
		for i in range(len(computer_specimen) - 1):
			if (speciman.positionx == computer_specimen[i].positionx and speciman.positiony == computer_specimen[i].positiony): #Finds the specimen occupying the same tile as current speciman.
				if speciman.strength > computer_specimen[i].strength:
					board.ChangeTileState(computer_specimen[i].positionx, computer_specimen[i].positiony, 2)
					computer_specimen.pop(i)
					return True
				elif speciman.strength == computer_specimen[i].strength:
					random_outcome = random.randint(0, 2)
					if random_outcome == 1:
						board.ChangeTileState(computer_specimen[i].positionx, computer_specimen[i].positiony, 2)
						computer_specimen.pop(i)
						return True
					else:
						return False
				else: 
					return False
	elif speciman_type == 3: #Checks if the speciman is a computer, situations below are similiar to the ones above but are for the computer plaer.
		for i in range(len(player_specimen)):
			if (speciman.positionx == player_specimen[i].positionx and speciman.positiony == player_specimen[i].positiony): #Finds the specimen occupying the same tile as current speciman.
				if speciman.strength > player_specimen[i].strength:
					board.ChangeTileState(player_specimen[i].positionx, player_specimen[i].positiony, 3)
					player_specimen.pop(i)
					return True
				elif speciman.strength == player_specimen[i].strength:
					random_outcome = random.randint(0, 2)
					if random_outcome == 1:
						board.ChangeTileState(player_specimen[i].positionx, player_specimen[i].positiony, 3)
						player_specimen.pop(i)
						return True
					else:
						return False
				else: 
					return False

def Mutation(new_speciman): #Creates a random mutation in 3 of the main attributes.
	choose_attr = random.randint(0,3)
	if choose_attr == 1:
		new_speciman.strength += 1
	elif choose_attr == 2:
		new_speciman.speed += 1
	else:
		new_speciman.resistance += 1

def Replicate(specimen, speciman): #This functions creates the copy of a speciman that ate food and adds him to the specimen list.
	new_speciman = EvoSimSpec.Species(
		speciman.name, 
		speciman.strength, 
		speciman.speed, 
		speciman.resistance, 
		speciman.predator, 
		speciman.prev_positionx, 
		speciman.prev_positiony)
	mut_chance = random.randint(0,8) #Determines chance of mutation during replication.
	if mut_chance == 1:
		Mutation(new_speciman)
	specimen.append(new_speciman)

def Feed(board, player_specimen, computer_specimen, speciman, speciman_type): #This function deals with outcomes of previous move.
	speciman.Refill() #Refills turns_left attribute.
	if speciman_type == 2: 
		Replicate(player_specimen, speciman)
	elif speciman_type == 3:
		Replicate(computer_specimen, speciman)

def MoveSpeciman(board, player_specimen, computer_specimen, speciman, speciman_type): #This function is responsible for controlling specimen movement on the board.
	won = True
	for i in range(speciman.speed):
		direction = random.choice(['N', 'S', 'W', 'E', 'NW', 'NE', 'SW', 'SE']) #Creates random direction.
		if (direction == 'N' #This if statement probably should call functions instead doing almost the same thing 8 times, but it looks cool. ;)
		and speciman.positionx != 0 #Checks if next move won't move out of list boundries.
		and board.board[speciman.positionx - 1][speciman.positiony] != speciman_type #Checks if tile is occupied by the same species.
		and [ speciman.prev_positionx, speciman.prev_positiony ] != [(speciman.positionx - 1), speciman.positiony ]): #Checks if drawn tile is not previous tile. (Prevents backtracking)
			if ((speciman_type == 2 and board.board[speciman.positionx - 1][speciman.positiony] == 3 #Checks if choosed tile is occupied by enemy species.
			or speciman_type == 3 and board.board[speciman.positionx - 1][speciman.positiony] == 2)
			and speciman.predator == True):
				 won = Combat(board, speciman, player_specimen, computer_specimen, speciman_type)
			elif board.board[speciman.positionx - 1][speciman.positiony] == 1:
				Feed(board, player_specimen, computer_specimen, speciman, speciman_type)
			speciman.prev_positionx = speciman.positionx
			speciman.prev_positiony = speciman.positiony
			speciman.positionx -= 1
			break
		elif (direction == 'S'
		and speciman.positionx != (board.board_size -1)
		and board.board[speciman.positionx + 1][speciman.positiony] != speciman_type
		and [ speciman.prev_positionx, speciman.prev_positiony ] != [(speciman.positionx + 1), speciman.positiony ]):
			if ((speciman_type == 2 and board.board[speciman.positionx + 1][speciman.positiony] == 3
			or speciman_type == 3 and board.board[speciman.positionx + 1][speciman.positiony] == 2)
			and speciman.predator == True):
				 won = Combat(board, speciman, player_specimen, computer_specimen, speciman_type)
			elif board.board[speciman.positionx + 1][speciman.positiony] == 1:
				Feed(board, player_specimen, computer_specimen, speciman, speciman_type)
			speciman.prev_positionx = speciman.positionx
			speciman.prev_positiony = speciman.positiony
			speciman.positionx += 1
			break
		elif (direction == 'W'
		and speciman.positiony != 0
		and board.board[speciman.positionx][speciman.positiony - 1] != speciman_type
		and [ speciman.prev_positionx, speciman.prev_positiony ] != [ speciman.positionx, (speciman.positiony - 1) ]):
			if ((speciman_type == 2 and board.board[speciman.positionx][speciman.positiony - 1] == 3
			or speciman_type == 3 and board.board[speciman.positionx][speciman.positiony - 1] == 2)
			and speciman.predator == True):
				 won = Combat(board, speciman, player_specimen, computer_specimen, speciman_type)
			elif board.board[speciman.positionx][speciman.positiony - 1] == 1:
				Feed(board, player_specimen, computer_specimen, speciman, speciman_type)
			speciman.prev_positionx = speciman.positionx
			speciman.prev_positiony = speciman.positiony
			speciman.positiony -= 1
			break
		elif (direction == 'E'
		and speciman.positiony != (board.board_size - 1)
		and board.board[speciman.positionx][speciman.positiony + 1] != speciman_type
		and [ speciman.prev_positionx, speciman.prev_positiony ] != [ speciman.positionx, (speciman.positiony + 1) ]):
			if ((speciman_type == 2 and board.board[speciman.positionx][speciman.positiony + 1] == 3
			or speciman_type == 3 and board.board[speciman.positionx][speciman.positiony + 1] == 2)
			and speciman.predator == True):
				 won = Combat(board, speciman, player_specimen, computer_specimen, speciman_type)
			elif board.board[speciman.positionx][speciman.positiony + 1] == 1:
				Feed(board, player_specimen, computer_specimen, speciman, speciman_type)
			speciman.prev_positionx = speciman.positionx
			speciman.prev_positiony = speciman.positiony
			speciman.positiony += 1
			break
		elif (direction == 'NW'
		and speciman.positionx != 0
		and speciman.positiony != 0
		and board.board[speciman.positionx - 1][speciman.positiony - 1] != speciman_type
		and [ speciman.prev_positionx, speciman.prev_positiony ] != [ (speciman.positionx - 1), (speciman.positiony - 1) ]):
			if ((speciman_type == 2 and board.board[speciman.positionx - 1][speciman.positiony - 1] == 3
			or speciman_type == 3 and board.board[speciman.positionx - 1][speciman.positiony - 1] == 2)
			and speciman.predator == True):
				 won = Combat(board, speciman, player_specimen, computer_specimen, speciman_type)
			elif board.board[speciman.positionx - 1][speciman.positiony - 1] == 1:
				Feed(board, player_specimen, computer_specimen, speciman, speciman_type)
			speciman.prev_positionx = speciman.positionx
			speciman.prev_positiony = speciman.positiony
			speciman.positionx -= 1
			speciman.positiony -= 1
			break
		elif (direction == 'NE'
		and speciman.positionx != 0
		and speciman.positiony != (board.board_size - 1)
		and board.board[speciman.positionx - 1][speciman.positiony + 1] != speciman_type
		and [ speciman.prev_positionx, speciman.prev_positiony ] != [ (speciman.positionx - 1), (speciman.positiony + 1) ]):
			if ((speciman_type == 2 and board.board[speciman.positionx - 1][speciman.positiony + 1] == 3
			or speciman_type == 3 and board.board[speciman.positionx - 1][speciman.positiony + 1] == 2)
			and speciman.predator == True):
				 won = Combat(board, speciman, player_specimen, computer_specimen, speciman_type)
			elif board.board[speciman.positionx - 1][speciman.positiony + 1] == 1:
				Feed(board, player_specimen, computer_specimen, speciman, speciman_type)
			speciman.prev_positionx = speciman.positionx
			speciman.prev_positiony = speciman.positiony
			speciman.positionx -= 1
			speciman.positiony += 1
			break
		elif (direction == 'SW'
		and speciman.positionx != (board.board_size - 1)
		and speciman.positiony != 0
		and board.board[speciman.positionx + 1][speciman.positiony - 1] != speciman_type
		and [ speciman.prev_positionx, speciman.prev_positiony ] != [ (speciman.positionx + 1), (speciman.positiony - 1) ]):
			if ((speciman_type == 2 and board.board[speciman.positionx + 1][speciman.positiony - 1] == 3
			or speciman_type == 3 and board.board[speciman.positionx + 1][speciman.positiony - 1] == 2)
			and speciman.predator == True):
				 won = Combat(board, speciman, player_specimen, computer_specimen, speciman_type)
			elif board.board[speciman.positionx + 1][speciman.positiony - 1] == 1:
				Feed(board, player_specimen, computer_specimen, speciman, speciman_type)
			speciman.prev_positionx = speciman.positionx
			speciman.prev_positiony = speciman.positiony
			speciman.positionx += 1
			speciman.positiony -= 1
			break
		elif (direction == 'SE'
		and speciman.positionx != (board.board_size - 1)
		and speciman.positiony != (board.board_size - 1)
		and board.board[speciman.positionx + 1][speciman.positiony + 1] != speciman_type
		and [ speciman.prev_positionx, speciman.prev_positiony ] != [ (speciman.positionx + 1), (speciman.positiony + 1) ]):
			if ((speciman_type == 2 and board.board[speciman.positionx + 1][speciman.positiony + 1] == 3
			or speciman_type == 3 and board.board[speciman.positionx + 1][speciman.positiony + 1] == 2)
			and speciman.predator == True):
				 won = Combat(board, speciman, player_specimen, computer_specimen, speciman_type)
			elif board.board[speciman.positionx + 1][speciman.positiony + 1] == 1:
				Feed(board, player_specimen, computer_specimen, speciman, speciman_type)
			speciman.prev_positionx = speciman.positionx
			speciman.prev_positiony = speciman.positiony
			speciman.positionx += 1
			speciman.positiony += 1
			break
	
	if won == False and speciman_type == 2:
		list_index = player_specimen.index(speciman)
		board.ChangeTileState(speciman.positionx, speciman.positiony, 0)
		player_specimen.pop(list_index)
		return
	elif won == False and speciman_type == 3:
		list_index = computer_specimen.index(speciman)
		board.ChangeTileState(speciman.positionx, speciman.positiony, 0)
		computer_specimen.pop(list_index)
		return

	if speciman_type == 2:
		board.ChangeTileState(speciman.positionx, speciman.positiony, 2)
		board.ChangeTileState(speciman.prev_positionx, speciman.prev_positiony, 0)
	elif speciman_type == 3:
		board.ChangeTileState(speciman.positionx, speciman.positiony, 3)
		board.ChangeTileState(speciman.prev_positionx, speciman.prev_positiony, 0)

########################################################################################		
######################BLOCK OF FUNCTIONS RESPONSIBLE FOR CREATING SPECIES###############
########################################################################################
def CreateComputerSpecies(board):
	attr_points = 10 #Determines how many points computer has to spend, can be modified.
	specname = ''; strength = 0; speed = 0; resistance = 0; predator = False; posx = 0; posy = 0; #Attributes for class object.
	auxlist = [] #Creates auxilary list to shuffle values, for randomness.

	specname = EvoSimSpec.Species.ComputerSpeciesNameGen()

	for i in range(3): #Creates list of random values all below initial attr_points value.
		auxlist.append(random.randint(0, attr_points))
		attr_points -= auxlist[i] #subtracts points from the points to distribute.

	random.shuffle(auxlist) #Shuffles list so value distribution is random. Otherwise last attribute would have on avarage lower points value.
	strength = auxlist[0]
	speed = auxlist[1]
	resistance = auxlist[2]
	predator = random.choice([True, False]) #Sets random value for predator.
	posx, posy = RandomFreeBoardTile(board) #Gets random tile to be starting position.

	computer_species = EvoSimSpec.Species(specname, strength, speed, resistance, predator, posx, posy)
	board.ChangeTileState(posx, posy, 3) #Changes empty file to computer file. 
	return computer_species

def SetAttribute(attr_points, attribute_name):
	while True:
		if attribute_name == "strength":
			user_input = EvoSimDisplay.GetAttributeDisplay(attr_points, "strength")
		elif attribute_name == "speed":
			user_input = EvoSimDisplay.GetAttributeDisplay(attr_points, "speed")
		elif attribute_name == "resistance":
			user_input = EvoSimDisplay.GetAttributeDisplay(attr_points, "resistance")
		else:
			pass
		try: #Checks if the given number is an integer
			attribute = int(user_input)
		except ValueError:
			EvoSimDisplay.NonIntegerErrorDisplay()
			continue
		if attribute <= attr_points and attribute > -1:
			attr_points -= attribute
			break
		else:
			EvoSimDisplay.GetAttributeErrorDisplay()


	return attribute, attr_points;


def CreatePlayerSpecies(board):
	attr_points = 10 #Determines how many points player has to spend, can be modified.
	specname = ''; strength = 0; speed = 0; resistance = 0; predator = False; posx = 0; posy = 0; #Attributes for class object.

	while True: #Sets the name of species.
		specname = EvoSimDisplay.GetNameDisplay()
		if len(specname) > 2 and len(specname) < 33:
			break
		else:
			EvoSimDisplay.GetNameErrorDisplay()

	strength, attr_points = SetAttribute(attr_points, "strength")
	speed, attr_points = SetAttribute(attr_points, "speed")
	resistance, attr_points = SetAttribute(attr_points, "resistance")

	while True: #Sets the predator attribute.
		predator = EvoSimDisplay.GetPredatorDisplay()
		if predator == 'Y' or predator == 'y':
			predator = True
			break
		elif predator == 'N' or predator == 'n':
			predator = False
			break
		else:
			EvoSimDisplay.GetPredatorErrorDisplay()

	posx, posy = RandomFreeBoardTile(board)


	player_species = EvoSimSpec.Species(specname, strength, speed, resistance, predator, posx, posy)
	board.ChangeTileState(posx, posy, 2) #Sets empty tile to be player tile.
	return player_species
########################################################################################		
######################BLOCK OF FUNCTIONS RESPONSIBLE FOR BOARD LOGIC####################
########################################################################################
def SetBoardSize():
	board_size_min = 7 #Determines (min size + 1) of a board. Can be changed. 
	board_size_max = 25 #Determines (max size - 1) of a board. Can be changed. 

	while True: #Loops player's input until integer number is given.
		user_input = EvoSimDisplay.GetBoardSizeDisplay()
		try: #Checks if the given number is an integer
			board_size = int(user_input)
		except ValueError:
			EvoSimDisplay.NonIntegerErrorDisplay()
			continue
		if board_size > board_size_min and board_size < board_size_max: #Checks if the given number fits the size requirements.
			return board_size
		else:
			EvoSimDisplay.WrongValueErrorDisplay()

def RandomFreeBoardTile(board): #This function finds random free tile on a board
	while True:
		posx = random.randint(0, (board.board_size - 1))
		posy = random.randint(0, (board.board_size - 1))
		if (board.CheckTile(posx, posy) == 0):
			return posx, posy

########################################################################################		
#################################CREATED FOR TEST PURPOSES##############################
########################################################################################
def main():
	pass

if __name__ == '__main__':
	main()
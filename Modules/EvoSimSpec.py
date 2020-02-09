#!/usr/bin/env python3

#This module contains class responsible for creating species.

import random

class Species():

	def __init__(self, name, strength, speed, resistance, predator, positionx, positiony):
		self.name = name #Quite obvious this one.
		
		self.strength = strength #Determines ability to fight. Individual with higher strength has higher change two win in fight occur.
		self.speed = speed #How many tiles individual moves per turn. If predator is set to false higher speed allows to escape.
		self.resistance = resistance #Multiplier of extra turns.
		self.predator = predator #Binary atribute. If enabled individual seeks fight also won't try to escape when attacked. Can feed on fallen enemy.
		
		self.positionx = positionx #Individual's position on the board.
		self.positiony = positiony
		self.prev_positionx = positionx #Individual's previous position on the board. Set the same as position when object is created.
		self.prev_positiony = positiony

		self.turns_left = 18 + (3 * resistance) #Determines how many turns until speciman dies.

	@staticmethod
	def ComputerSpeciesNameGen(): #This funtion generates random name for a computer species.
		name_len = random.randint(4, 8) #Sets name length
		specname = ''
		vows = ['a', 'e', 'i', 'o', 'u', 'y']
		cons = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z']


		letter = random.choice(cons)
		specname += letter.upper()
		for i in range(name_len):
			letter_type = random.randint(0, 2) #Determines from which collection next letter will be drawn.
			if letter_type == 1 and letter not in cons: #Disables two consonants in a row.
				letter = random.choice(cons)
				specname += letter
			else:
				letter = random.choice(vows)
				specname += letter

		return specname

########################################################################################		
#################################CREATED FOR TEST PURPOSES##############################
########################################################################################
def main():
	pass


if __name__ == '__main__':
	main()

#Version: Alpha 0.1

#Requirements:
	Python 3.7
	Python library: colorama
	Linux/MacOS

#Description:
	EvoSim is a small Python project with a goal to sharpen my programming skills and create fun simulation. It plays in terminal and creates board on which two species (one created by player and 2nd by computer) try to survive by eating food and replicating. When two specimen from different species happen to meet on the same tile, they will fight and only one will survive. Idea of this game came from "Game of Life" by british mathematician John Horton Conway and my fascination with sim-games.

#Running the program:
	Linux/MacOS users need to doubleclick Launcher icon or run as a scirpt with "./" commmand. (Might need to set permission with chmod +x Launcher)

#Future funciotnality:
	*Menu - Player will have an option to choose action. 
	*Different modes - There will be option to select game between two computers, hot seats or versus super builds.
	*Instruction - Basic instruction will help user to interact with a program.
	*File handling - Saving scores to files or config file with map size etc.
	*Better movement - In future I'm planning to modify movement so specimen go to adjacent food sources or attack enemy speciman if they are predators.
	*AI - Farfetched, but it would be neat to create AI that would test possible build and come up with the best one.
	*Perks - Perks would be fine idea. For example fertility would give a chance for bigger offsptring etc.

#Knowns bugs:
	*Computer specimen do not show on board sometimes. It looks like logic still works, but they are not displayed on a board
	*Combat occurs even if two species are set not to be predators.
	*Specimen sometimes dissapear and reappear moment later.
	*It seems like combat logic doesnt always work since specimen count sometimes doesn't decrease. It might indicate that are are errors in "if" logic responsible for combat.

#Lessons for the future:
	*Use more OOP. Species class should have subclass for computer and player. It would save alot of copying and pasting the same instructions. The same goes for Board class that should have Tile subclass. Also it would be great to add more methods to classed instead of bloating GameLogic module.

	*The if function has 120 lines which is far too more. Should have been think it through a little more. Another reason to use more classes instead putting everything into gamelogic.
	
	*Variables could be name a little better. For example user-objects should have different names from simple variables.

	*Putting project name into every module name seems pointless and made my just write much more. I think that only main module should be named as a projects and rest should be called after their function
	in a program.

	*Should have worked more on debugging. In early stage of creating program I've been using 'main' fucntion in modules to debug. Later when program started to work as a whole I was launching game normally and going through all the preperations to get to the problem. It can work fine for small projects but becomes tedious when program is getting bigger. Also Sublime is not a best environment for such undertaking. Definetely need to switch to actual IDE for Python.
	
	*This might be reaching far, but in a future it would be decent idea to use Python scripts for automated testing.

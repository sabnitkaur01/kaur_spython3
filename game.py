# import the random package so that we can generate a random choice
from random import randint
from gameFunctions import winlose, gameVars

choices = ["rock", "paper","scissors"]
computer = choices[randint (0, 2)]
while player is False:
	# set player to True
	print("**********************************")
	print("Computer lives: ", computer_lives, "/5\n")
	print("Player lives: " player_lives, "/5\n")
	print("Choose your weapon!\n")
	print("**********************************")

	player = input("choose rock, paper or scissors: ")
	player = player.lower()

	print("computer chose ", computer, "\n")
	print("player chose ", player, "\n")

	###this is where you would call compare
	

	### end compare stuff

	# handle all lives lost for player or AI
	if gameVars.player_lives is 0:
		winlose.winorlose("lost")

	elif gameVars.computer_lives is 0:
		winlose.winorlose("won")

	else:
		# need to check all of our conditions after checking for a tie
		player = False
		computer = choices[randint(0, 2)]	


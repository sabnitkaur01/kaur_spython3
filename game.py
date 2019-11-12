# import the random package so that we can generate a random choice
from random import randint
from gameFunctions import winlose, gameVar, compare

choices = ["rock", "paper", "scissors"]
computer = choices[randint (0, 2)]
while gameVar.player is False:

	# set player to True
	print("**********************************")
	print("Computer lives: ", gameVar.computer_lives, "/5\n")
	print("Player lives: ", gameVar.player_lives, "/5\n")
	print("Choose your weapon!\n")
	print("**********************************")

	player = input("choose rock, paper or scissors: ")
	player = player.lower()

	print("computer chose ", computer, "\n")
	print("player chose ", player, "\n")

	###this is where you would call compare
	compare.comparechoices(player,computer)

	### end compare stuff

	# handle all lives lost for player or AI
	if gameVar.player_lives is 0:
		winlose.winorlose("lost")

	elif gameVar.computer_lives is 0:
		winlose.winorlose("won")

	else:
		# need to check all of our conditions after checking for a tie
		print("********************************")

	gameVar.player = False
	computer = choices[randint(0, 2)]	



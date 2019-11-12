from gameFunctions import gameVar


# what are you trying to compare inside this function?
# you will need to pass those things in as arguments
# inside the round brackets
def comparechoices(player,computer):	
	if player == "quit":
		exit()
	elif computer == player:
		print("tie! no one wins, play again")

	elif player == "rock":
		if computer == "paper":
			print("You lose!", computer, "covers", player, "\n")
			gameVar.player_lives = gameVar.player_lives - 1
		else:
			print("You win!", player, "smashes", computer, "\n")
			gameVar.computer_lives = gameVar.computer_lives - 1

	elif player.lower() == "paper":
		if computer == "scissors":
			print("You lose!", computer, "cuts", player, "\n")
			gameVar.player_lives = gameVar.player_lives - 1
		else:
			print("You win!", player, "covers", computer, "\n")
			gameVar.computer_lives = gameVar.computer_lives - 1

	elif player.lower() == "scissors":
		if computer == "rock":
			print("You lose!", computer, "smashes", player, "\n")
			gameVar.player_lives = gameVar.player_lives - 1
		else:
			print("You win!", player, "cuts", computer, "\n")
			gameVar.computer_lives = gameVar.computer_lives - 1

	else:
		print("That's not a valid choice, try again")
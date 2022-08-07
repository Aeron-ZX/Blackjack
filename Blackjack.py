import random

class Player():
	pass

class Bank():
	pass

print("""Welcome to this Blacjack simulation game. Blackjack is a card game which you play against the banking or the machine. 
	A simplified set of rules of the game are as follow:
	 - The dealer deals two cards to each player.
	 - A card is shown in the table, this is the initial dealer hand. Another card is drawn to the dealer's hand, but remains face down.
	 - The goal of the game is to have the biggest hand without exceeding 21.
	 - Each card scores the number they represent. J, Q and K count as 10 points. Any Ace counts as 11, as long as that value wouldn't exceed 21 in the hand score; in which case it counts as 1. 
	 - Once the cards are shown, each player can decide to Hit or Stand. Hit means draw another card, Stand keeping the cards at hand.
	 - If the player selected Hit and exceeds 21, he loses. If the player is still in the game, the dealer reveals the second card. 
	 - If the dealer score is higher than those of the players, the bank wins. If it's the same is a draw. 
	 - If the score is lower to the player's score, the dealer can pick more cards until he wins, draws or break the 21 points.""")

n_players = input("How many players are going to play? Type 1 or 2 ")
while n_players not in ["1", "2"]:
	n_players = input("Please, select 1 or 2 players ")
	if n_players == "1" or n_players == "2":
		break

print("The selected number of players is: " + str(n_players))

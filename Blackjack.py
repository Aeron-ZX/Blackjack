import random

class Player():
	pass

class Bank():
	pass

class Card():
	pass

deck = {}
def generate_new_deck():
	for n in range(1, 53):
		if n < 14:
			deck[n] = ["Spades", n]
		elif n < 27:
			deck[n] = ["Hearts", n-13]
		elif n < 40:
			deck[n] = ["Clubs", n-26]
		elif n < 53:
			deck[n] = ["Diamonds", n-39]

	for n, card in deck.items():
		if card[1] == 1:
			deck[n][1] = "A"
		elif card[1] == 11:
			deck[n][1] = "J"
		elif card[1] == 12:
			deck[n][1] = "Q"
		elif card[1] == 13:
			deck[n][1] = "K"

def pick_card():
	shuffle_deck = []
	for n in deck.keys():
		shuffle_deck.append(n)
	selected_card = random.choice(shuffle_deck)
	return deck.pop(selected_card)

def calculate_score(*cards):
	score = 0
	for card in cards:
		if card[1] == "J" or card[1] == "Q" or card[1] == "K":
			score += 10
		elif card[1] == "A":
			if score+11 > 21:
				score += 1
			else: 
				score += 11
		else:
			score += card[1]
	return score

print("""Welcome to this Blackjack simulation game. Blackjack is a card game which you play against the banking or the machine.

	A simplified set of rules of the game are as follow:
	 - The dealer deals two cards to each player.
	 - A card is shown in the table, this is the initial dealer hand. Another card is drawn to the dealer's hand, but remains face down.
	 - The goal of the game is to have the biggest hand without exceeding 21.
	 - Each card scores the number they represent. J, Q and K count as 10 points. Any Ace counts as 11, as long as that value wouldn't exceed 21 in the hand score; in which case it counts as 1. 
	 - Once the cards are shown, each player can decide to Hit or Stand. Hit means draw another card, Stand keeping the cards at hand.
	 - If the player selected Hit and exceeds 21, he loses. If the player is still in the game, the dealer reveals the second card. 
	 - If the dealer score is higher than those of the players, the bank wins. If it's the same is a draw. 
	 - If the score is lower to the player's score, the dealer can pick more cards until he wins, draws or breaks the 21 points.""")

n_players = input("How many players are going to play? Type 1 or 2 ")
while n_players not in ["1", "2"]:
	n_players = input("Please, select 1 or 2 players ")
	if n_players == "1" or n_players == "2":
		break

print("The selected number of players is: " + str(n_players))
if n_players == "1":
	player1 = input("Introduce player's name: ")
	print("Welcome " + player1)
elif n_players == "2":
	player1 = input("Introduce the name of player 1: ")
	player2 = input("Introduce the name of player 2: ")
	print("Welcome " + player1 + " and " + player2 + "!")

input("Now we're gonna shuffle the cards. Press Enter to continue")
generate_new_deck()

if n_players == "1":
	card1 = pick_card()
	input("The first card for " + player1 + " is " + str(card1))
	card2 = pick_card()
	input("The second card for " + player1 + " is " + str(card2))
	score1 = calculate_score(card1, card2)
	print("Current score is " + str(score1))
	if score1 == 21:
		print("A Blackjack!! You win!")


elif n_players == "2":
	card1p1 = pick_card()
	card2p1 = pick_card()
	card1p2 = pick_card()
	card2p3 = pick_card()







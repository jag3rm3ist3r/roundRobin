# This is a test of the program that does combinations of players for a round robin.
# Test string:
# This Is A Test Of The Program That Does Combinations

import sys

# Player name input.
input = input("Paste player names: ")
players = input.split(" ")
if len(players) != len(set(players)):
	print("Duplicate player name.")
	sys.exit()

# Add bye for uneven player count.
if len(players) % 2: players.append("BYE")
maxRounds = len(players) - 1

# Circle method.
# Split list in two.
a = players[:len(players)//2]
b = players[len(players)//2:]

rounds = []
for round in range(maxRounds):
	rounds.append(list(zip(a, b)))
	# Rotate the pairings.
	# Move first of b behind front of a.
	a.insert(1, b.pop(0))
	# Move last of a to last of b.
	b.append(a.pop())

def prettyPrintPairing(pairing):
	print(pairing[0], " - vs - ", pairing[1])

def playerPairing(player):
	print("\nPlayer: ", player)
	roundNumber = 0
	for round in rounds:
		roundNumber += 1
		for pairing in round:
			if player not in pairing: continue
			print("Round ", roundNumber, ": ", end='', sep='')
			if player == pairing[0]:
				print(pairing[1])
			else:
				print(pairing[0])
			break

# Print pretty output.
for player in players:
	playerPairing(player)

roundNumber = 0
for round in rounds:
	roundNumber += 1
	print("\nRound ", roundNumber)
	for pairing in round:
		prettyPrintPairing(pairing)


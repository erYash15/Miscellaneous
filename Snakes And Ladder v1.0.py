#=======Yash Gupta Python Snake And Ladder version 1.0=========
'''This is basic coding without board or tkinter'''
import random

# Snakes and Ladders dictionary
SaL = {5: 17,
          14: 3,
          20: 15,
          24: 26,
          30: 44,
          39: 33,
          49: 62,
          66: 53,
          69: 58,
          79: 67,
          82: 86,
          84: 71,
          97: 36,}

# Player class
class Player:
	def __init__(self, inPlayerNum):#like a constractor
		self.playerPos = 1 # individual player data.
		self.playerNum = inPlayerNum #player 1,2,3,4.
	def updatePosition(self, inPos):
		self.playerPos = inPos
	def getPosition(self):
		return self.playerPos
	def getPlayerNum(self):
		return self.playerNum


# Function to handle the players turn
def gameon(ithPlayer):
    global winner
	# run dice rolls and movements
    if (winner == False):
        print("\n-Player ",ithPlayer.getPlayerNum()," Hit enter to roll-")
        input()
        roll = random.randint(1,6)
        print("You rolled: ", roll)
        movePlayer(ithPlayer, roll)
        checkSnL(ithPlayer)
    # check for game winner
    if (ithPlayer.getPosition() == 100):
        print("Player" , ithPlayer.getPlayerNum()  ," is the Winner! ")
        winner = True

# Handle player movements
def movePlayer(ithPlayer, roll):
	if (ithPlayer.getPosition() + roll <= 100):
		ithPlayer.updatePosition(ithPlayer.getPosition() + roll)
		print("You are at spot ",ithPlayer.getPosition() , ".")
	else:
		print("You Rolled Far.")

# Checks player landing position and adjusts if snake or ladder
def checkSnL(ithPlayer):
	for pos in SaL:
		if pos == ithPlayer.getPosition():
			if pos < SaL[pos]:
				print("You climbed Ladder to spot ", SaL[pos])
			else:
				print("You are bitten by a Snake to spot ", SaL[pos])
			ithPlayer.updatePosition(SaL[pos])

# Driver Program
#next 4 line             
for x in range(1, 101): # 1 - 100
    print ("%03d" % (101 - x,), end = " | ") # make all numbers 3 digits
    if x % 10 == 0: # every ten line output a new line
        print()
        
global winner
winner = False
numPlayers = int(input('Enter number of players: '))
playerList = []

for i in range(0,numPlayers):
	playerList.append(Player(i + 1))
	
while winner == False:
	for i in playerList:
		if winner == False:
			gameon(i)

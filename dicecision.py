from botmode import choosefile
import os
import random
import time

def diceRoll(diceRolled,player):
    if diceRolled == 1:
        total = random.randint(1,6)
        print("\nThe",player,"rolled",diceRolled,"dice.")
        print(player,"rolled values:",total)
        if total == 6:
            print("Triple value!")
            total = total * 3
        return total
    
    if diceRolled == 2:
        total = 0
        rollValues = []
        for i in range(2):
            randomRoll = random.randint(1,6)
            rollValues.append(randomRoll)
            total = total + randomRoll
        print("\nThe",player,"rolled",diceRolled,"dice.")
        print(player,"rolled values:",rollValues)
        return total

    if diceRolled == 3:
        total = 0
        rollValues = []
        for i in range(3):
            randomRoll = random.randint(1,6)
            rollValues.append(randomRoll)
            total = total + randomRoll
        #Subtract last value if its less than 4.
        if rollValues[2] > 4:
            total = total - (rollValues[2] * 2)
        print("\nThe",player,"rolled",diceRolled,"dice.")
        print(player,"rolled values:",rollValues)
        return total

opponentPos = 0
playerPos = 0

os.system('cls')
#INITIALIZE TILES
tileSize = int(input("How many tiles should the board have?: "))
while tileSize < 20:
    print("\nToo few tiles, minimum of 20.")
    tileSize = int(input("How many tiles should the board have?: "))

#THE GAME
while opponentPos < tileSize and playerPos < tileSize:
    print("\nYour position is:",playerPos)
    print("Your opponents position is:",opponentPos)

    #Get player's choice.
    rollAmount = int(input("""How many dice would you like to roll?:
- 1 (If it rolls a 6, value is tripled)
- 2 (Both dice are normal)
- 3 (If the 3rd dice is one of [5,6], 3rd value is SUBTRACTED from roll)

INPUT:
"""))

    #Validation.
    validDice = [1,2,3]
    if rollAmount not in validDice:
        print("Invalid input.")
        rollAmount = int(input("""\nHow many dice would you like to roll?:
- 1 Dice (If it rolls a 6, value is tripled)
- 2 Dice (Both dice always count)
- 3 Dice (If the 3rd dice is one of [5,6], 3rd value is SUBTRACTED from roll)

INPUT:
"""))

    #Opponent AI's choice.
    os.system('cls')
    opponentDice = random.randint(1,3)
    opponentPos = opponentPos + diceRoll(opponentDice,"Opponent")
    
    #Scenarios for different rollAmounts -------------->
    if rollAmount == 1:
        playerPos = playerPos + diceRoll(1,"Player")
        
    if rollAmount == 2:
        playerPos = playerPos + diceRoll(2,"Player")
        
    if rollAmount == 3:
        playerPos = playerPos + diceRoll(3,"Player")

#VICTORY HANDLING
if opponentPos > playerPos:
    print("\nOpponent wins with",opponentPos,"points. You lose with",playerPos,"points!")
elif playerPos > opponentPos:
    print("\nOpponent loses with",opponentPos,"points. You win with",playerPos,"points!!")
else:
    print("You both draw with",playerPos,"points!")

#MENU OR CONTINUE
choosefile("dicecision.py")

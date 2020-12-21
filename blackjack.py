from botmode import choosefile
import os
import random

os.system('cls')
def totalValue(cards):
    total = 0
    for i in range(len(cards)):
        total = total + cards[i]
    return total

dealerCards = []
playerCards = []
dealerCards.append(random.randint(1,11))
for i in range(2):
        playerCards.append(random.randint(1,11))

print("Dealers Numbers:",dealerCards)
print("Total value:",totalValue(dealerCards))

print("\nYour cards are:",playerCards)
print("Total value:",totalValue(playerCards))

#Player makes choice.
onGoing = 1
while (totalValue(dealerCards) < 21 and totalValue(playerCards) < 21) and onGoing == 1:
    print("""\n What now?:
    - Hit
    - Stand
    """)
    choice = str(input("INPUT: ")).lower()
    #Validate choice.
    while not(choice == "hit") and not(choice == "stand"):
        print("Invalid input.\n")
        choice = str(input("INPUT: ")).lower()

    #Player makes choice.
    if choice == "hit":
        playerCards.append(random.randint(1,11))
    if choice == "stand":
        while totalValue(dealerCards) < 17:
            dealerCards.append(random.randint(1,11))
        onGoing = 0      
            
    print("\nDealers Numbers:",dealerCards)
    print("Total value:",totalValue(dealerCards))
    print("Your cards are:",playerCards)
    print("Total value:",totalValue(playerCards))

#Evaluate game after standing/hitting. --------------------------------------------
if totalValue(dealerCards) > 21:
    print("\nDealer loses. You win!")
elif totalValue(playerCards) > 21:
    print("\nDealer wins. You lose.")

else:
    if totalValue(dealerCards) > totalValue(playerCards):
        print("\nDealer wins. You lose.")
    elif totalValue(dealerCards) < totalValue(playerCards):
        print("\nDealer loses. You win!")
    else:
        print("\nDraw.")

choosefile("blackjack.py")
    


    


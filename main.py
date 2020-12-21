import os
import time

os.system('cls')
print("""
.____     .__         .__ __________          __   
|    |    |__|  ______|__|\______   \  ____ _/  |_ 
|    |    |  | /  ___/|  | |    |  _/ /  _ \\   __\

|    |___ |  | \___ \ |  | |    |   \(  <_> )|  |  
|_______ \|__|/____  >|__| |______  / \____/ |__|
        \/         \/             \/
Version 0.1
Made by Lisianthus (https://github.com/lisianthus1228)
""")

botMode = str(input("""What would you like to do?
- Blackjack
- Spammer

Enter anything else to exit:
""")).lower()

if botMode == "blackjack":
    os.system("blackjack.py")
elif botMode == "spammer":
    os.system("spammer.py")



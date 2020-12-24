from botmode import choosefile
import os

os.system('cls')
textToSpam = str(input("What would you like to spam?: "))
repeatAmount = int(input("How many times?: "))

for i in range(repeatAmount):
    print(textToSpam)

choosefile("spammer.py")




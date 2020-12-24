import os
def choosefile(fileToOpen):
    botMode = str(input("""What now?:
- Continue
- Exit

INPUT: """)).lower()

    commands = ["continue","exit"]
    while botMode not in commands:
        print("Invalid input.")
        botMode = str(input("""\nWhat now?:
- Continue
- Exit

INPUT: """)).lower()

    if botMode == "continue":
        os.system(fileToOpen)
    elif botMode == "exit":
        os.system("main.py")
        

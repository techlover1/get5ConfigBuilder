import os
from userinput import userinput
from buildconfig import buildconfig

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def completed():
    print("Sucessfully created file: ", buildconfig.cfgname)
    print("Thanks for using my tool")
    print("GL,HF")
    print("Press enter to exit")
    a = input()

if __name__ == "__main__":
    cls() # Clear the screen
    userinput() # Get user's input (userinput.py)
    buildconfig() # Build the config file (buildconfig.py)
    cls() # Clear the screen
    completed() # Print completeion screen

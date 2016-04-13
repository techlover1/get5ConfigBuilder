import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    
class userinput():
    
    def __init__(self):
        self.matchid()
        self.match_title()
        self.maps_to_win()
        self.skipveto()
    
    
    def matchid(self):
        global matchid
        
        matchid = input("What is the matchid you wish to use? (No spaces): ")
        
        print("MatchID:", matchid, "\n")
        
        
    def match_title(self):
        global match_title
        
        match_title = input(
        "What is the title of this match?\
        \n( | Map {mapnumber} of {maxmaps} will be added automaticly): ")
        
        print("Match Title:", match_title, "\n")
        
        
    def maps_to_win(self):
        global maps_to_win
        
        maps_to_win = input(
        "How many maps are required to win the series (ex 2 in bo3, 3 in bo5): ")
        
        print("Maps To Win:", maps_to_win, "\n")
        
    
    def skipveto(self):
        global skipveto
        
        skipveto = input("Do you want to do the veto in game (y or n)?: ")
        
        if skipveto == 'y':
            print("Doing the veto in game\n")
        elif skipveto == 'n':
            print("Not doing the veto in game\n")
        elif skipveto != 'y' and skipveto != 'n':
            print("Answer 'y' or 'n'")
            self.skipveto()
        
        
userinput()
print(skipveto, 'outside')
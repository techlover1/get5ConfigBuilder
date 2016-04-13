class userinput():
    # Define variables
    matchid = 'default'
    match_title = 'default'
    maps_to_win = 0
    skipveto = 'n'
    sidetype = ''
    playersperteam = 0
    
    def __init__(self):
        self.matchidf()
        self.match_titlef()
        self.maps_to_winf()
        self.skipvetof()
        self.sidetypef()
        self.playersperteamf()


    def matchidf(self):

        userinput.matchid = input("What is the matchid you wish to use? (No spaces): ")
        
        print("MatchID:", userinput.matchid, "\n")


    def match_titlef(self):
        
        userinput.match_title = input(
        "What is the title of this match?\
        \n( | Map {mapnumber} of {maxmaps} will be added automaticly): ")
        
        print("Match Title:", userinput.match_title, "\n")


    def maps_to_winf(self):
        
        try:
            userinput.maps_to_win = int(input(
            "How many maps are required to win the series (ex 2 in bo3, 3 in bo5): "))
            print("Maps To Win:", userinput.maps_to_win, "\n")
        except:
            print("Enter a number")
            self.maps_to_winf()


    def skipvetof(self):

        userinput.skipveto = input("Do you want to do the veto in game (y or n)?: ")
        
        if userinput.skipveto == 'y':
            print("Doing the veto in game\n")
        elif userinput.skipveto == 'n':
            print("Not doing the veto in game\n")
        elif userinput.skipveto != 'y' and skipveto != 'n':
            print("Answer 'y' or 'n'")
            self.skipveto()


    def sidetypef(self):

        userinput.sidetype = input("How do you want to choose sides(1, 2, or 3)?\n\
        	1: Standard\n\
        	2: Always Knife\n\
        	3: Never Knife\n: ")
        	
        if userinput.sidetype == '1':
            print('\nSide type: standard\n')
            
        elif userinput.sidetype == '2':
            print('Side type: always_knife\n')
            
        elif userinput.sidetype == '3':
            print('Side type: never_knife\n')
            
        elif userinput.sidetype != '1'\
            and userinput.sidetype != '2' and userinput.sidetype != '3':
                
            print('Choose 1, 2, or 3')
            self.sidetype()


    def playersperteamf(self):

        try:
            userinput.playersperteam = int(input("How many players are on each roster? "))
            print("Players per team: ", userinput.playersperteam, '\n')
        except:
            print("Enter a number")
            self.playersperteamf()

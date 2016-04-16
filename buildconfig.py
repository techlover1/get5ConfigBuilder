from userinput import userinput

class buildconfig():
    cfgname = 'default'
    def __init__(self):
        self.createfile()
        self.matchsetup()
        self.spectators()
        self.mapsandsides()
        self.sidetype()
        self.teamblocks()
        self.closefile()


    def createfile(self):
        global fw
        
        buildconfig.cfgname = userinput.matchid + '.cfg'
        fw = open(buildconfig.cfgname, 'w')


    def matchsetup(self):
        fw.write('"Match"\n{\n')
        fw.write('\t"matchid"\t"' + userinput.matchid +
                 ' | Map {MAPNUMBER} of {MAXMAPS}' + '"\n')
        fw.write('\t"match_title"\t"' + userinput.match_title + '"\n')
        fw.write('\t"maps_to_win"\t"')
        fw.write(str(userinput.maps_to_win))
        fw.write('"\n')


    def spectators(self):
        adminfile = open('configs/admins.txt', 'r')
        admins = adminfile.read()
        fw.write('\t"spectators"\n\t{\n\t\t"players"\n')
        fw.write(admins)
        adminfile.close
        fw.write('\n\t}\n')


    def mapsandsides(self):
        if userinput.skipveto == "y":
            fw.write('\t"skip_veto"\t"0"\n')
        elif userinput.skipveto == "n":
            fw.write('\t"skip_veto"\t"1"\n')


    def sidetype(self):
        if userinput.sidetype == '1':
            fw.write('\t"side_type"\t"standard"\n')
        elif userinput.sidetype == '2':
            fw.write('\t"side_type"\t"always_knife"\n')
        elif userinput.sidetype == '3':
            fw.write('\t"side_type"\t"never_knife\n')
            
        fw.write('\t"maplist"\n')
        mapfile = open('configs/maps.txt', 'r')
        maplist = mapfile.read()
        fw.write(maplist)
        mapfile.close
        
        fw.write('\n\t"players_per_team"\t' + str(userinput.playersperteam))
        
        fw.write('\n\t"favored_percentage_team1"\t""\n\t"favored_percentage_text"\t""\n')


    def teamblocks(self):
        # Team 1
        team1filename = userinput.team1filename
        fw.write('\t"team1"\n')
        team1file = open("teams/"+team1filename+".txt")
        team1 = team1file.read()
        fw.write(team1)
        team1file.close
        
        # Team 2
        team2filename = userinput.team2filename
        fw.write('\n\t"team2"\n')
        team2file = open("teams/"+team2filename+".txt")
        team2 = team2file.read()
        fw.write(team2)
        team2file.close


    def closefile(self):
        # Cvars
        fw.write('\n\t"cvars"\n\t{\n\n\t}')
        
        # Close file
        fw.write('\n}')
        fw.close

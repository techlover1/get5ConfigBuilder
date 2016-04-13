import os


# Function for clearing console
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Get initial input
cls()

matchid = input("What is the matchid you wish to use? (No spaces): ")
print("MatchID:", matchid, "\n")

match_title = input(
    "What is the title of this match?\
    \n( | Map {mapnumber} of {maxmaps} will be added automaticly: ")
print("Match Title:", match_title, "\n")

maps_to_win = input(
    "How many maps are required to win the series (ex 2 in bo3, 3 in bo5): ")
print("Maps To Win:", maps_to_win, "\n")

skipveto = input("Do you want to do the veto in game (y or n)?: ")
if skipveto == 'y':
    print("Doing the veto in game\n")
elif skipveto == 'n':
    print("Not doing the veto in game\n")

sidetype = input("How do you want to chose sides(1, 2, or, 3)?\n\
	1: Standard\n\
	2: Always Knife\n\
	3: Never Knife\n")
if sidetype == '1':
    print('Side type: standard\n')
elif sidetype == '2':
    print('Side type: always_knife\n')
elif sidetype == '3':
    print('Side type: never_knife\n')

playersperteam = input("How many players are on each roster? ")
print("Players per team: ", playersperteam + '\n')

# Create config file
cfgname = matchid + '.cfg'
fw = open(cfgname, 'w')

# match setup block
fw.write('"Match"\n{\n')
fw.write('\t"matchid"\t"' + matchid +
         ' | Map {MAPNUMBER} of {MAXMAPS}' + '"\n')
fw.write('\t"match_title"\t"' + match_title + '"\n')
fw.write('\t"maps_to_win"\t"' + maps_to_win + '"\n')
fw.write('\n')

# spectators
adminfile = open('configs/admins.txt', 'r')
admins = adminfile.read()
fw.write('\t"spectators"\n\t{\n\t\t"players"\n')
fw.write(admins)
adminfile.close
fw.write('\n\t}\n')

# Maps and sides
if skipveto == "y":
    fw.write('\t"skip_veto"\t"0"\n')
elif skipveto == "n":
    fw.write('\t"skip_veto"\t"1"\n')

if sidetype == '1':
    fw.write('\t"side_type"\t"standard"\n')
elif sidetype == '2':
    fw.write('\t"side_type"\t"always_knife"\n')
elif sidetype == '3':
    fw.write('\t"side_type"\t"never_knife\n')

fw.write('\t"maplist"\n')
mapfile = open('configs/maps.txt', 'r')
maplist = mapfile.read()
fw.write(maplist)
mapfile.close

fw.write('\n\t"players_per_team"\t' + playersperteam)

fw.write('\n\t"favored_percentage_team1"\t""\n\
	"favored_percentage_text"\t""\n')

# Team blocks
# Team 1
team1filename = 'test.txt'
fw.write('\t"team1"\n')
team1file = open("teams/"+team1filename)
team1 = team1file.read()
fw.write(team1)
team1file.close

# Team 2
team2filename = 'test2.txt'
fw.write('\n\t"team2"\n')
team2file = open("teams/"+team2filename)
team2 = team2file.read()
fw.write(team2)
team2file.close

# Cvars
fw.write('\n\t"cvars"\n\t{\n\n\t}')

# Close file
fw.write('\n}')
fw.close


# Clear screen
cls()

# Print completeion
print("Sucessfully created file: ", cfgname)
print("Thanks for using my tool")
print("GL,HF")
print("Press enter to exit")
a = input()

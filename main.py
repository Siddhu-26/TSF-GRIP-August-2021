import pandas as pd
import numpy as np

# Storing the Dataset in local variables
deliveries = pd.read_csv("E:\TSF\T2 - Sports\deliveries.csv")
matches = pd.read_csv("E:\TSF\T2 - Sports\matches.csv")

# Teams
temp = np.array(matches.iloc[:,10])

# Storing it in dictionaries
teams = {}
for i in set(temp):
    teams[i] = np.count_nonzero( temp == i)

# Storing the Most Valuable Team in a local variable
mvt = ''
a = 0
for i in teams:
    if a == 0:
        mvt = i
        a = 1
    if int(teams[mvt]) < int(teams[i]):
        mvt = i

# Sorting Teams
sorted_teams = {}
team = ''
a = 0
for i in range(len(teams)-1):
    for j in teams:
        if a == 0:
            team = j
            a = 1
        if int(teams[team]) < int(teams[j]):
            team = j
    sorted_teams[team] = teams[team]
    teams.pop(team)
    team = ''
    a = 0

# Storing all the teams sorted by its value
teams_lst = list(sorted_teams.keys())
teams.clear()
#print(sorted_teams)


# Man Of the Match
temp = np.array(matches.iloc[:,13])

# Storing it in dictionary
moms = {}
for i in set(temp):
    moms[i] = np.count_nonzero(temp == i)

# Storing the Most Valuable Player in local variable
mvp = ''
a = 0

for i in moms:
    if a == 0:
        mvp = i
        a = 1
    if int(moms[mvp]) < int(moms[i]):
        mvp = i

# Sorting Moms
sorted_moms = {}
mom = ''
a = 0
for i in range(len(moms)-1):
    for j in moms:
        if a == 0:
            mom = j
            a = 1
        if int(moms[mom]) < int(moms[j]):
            mom = j
    sorted_moms[mom] = moms[mom]
    moms.pop(mom)
    mom = ''
    a = 0

# Storing all the players sorted by their MOMs
moms_list = list(sorted_moms.keys())
moms.clear()

# Players and Teams
temp1 = np.array(matches.iloc[:,10])
temp2 = np.array(matches.iloc[:,13])

pot = {} # This Dictionary has the Player Name and his Team's name

for i in range(len(temp1)):
    if temp2[i] in pot.keys():
        i += 1
    else:
        pot[temp2[i]] = temp1[i]

# User Interaction
name = input("Enter your Name:")

print("Welcome " + name)

while(True):
    x = int(input("MENU:\n1. Successful Team\n2. Successful Player\n3. Exit\nEnter any of the above: "))

    if x == 1:
        if len(teams_lst) == 0:
            print("No more teams left")
        else:
            print(str(teams_lst[0]) + " : " + str(sorted_teams[teams_lst[0]]) + " wins")
            print("Team's Successful Players: ")
            for i in moms_list:
                if pot[i] == teams_lst[0]:
                    print(i)
            teams_lst.pop(0)
    elif x == 2:
        if len(moms_list) == 0:
            print("No more players left")
        else:
            print(str(moms_list[0]) + " : " + str(sorted_moms[moms_list[0]]) + " MoMs " + "Team: " + str(pot[moms_list[0]]))
            moms_list.pop(0)
    elif x == 3:
        print("Have a Great Day " + name +"\n")
        break
    else:
        print("Wrong Choice")
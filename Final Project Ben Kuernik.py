##Ben Kupernik
##CSC 119 470 SP20
##Final Project/2edProject V 2.0 (Added txt file with hero info, Troll and Hero Health and Troll and Hero fight function)
##Takes the user through an text based adventure
##5/13/2020



import random
import time
import sys
from makeclass import info
from Combat import trollcombat


#Runs the function to make your charter class
name,strength,cleric,wizard,description = info()

#writes your info to a text file
heroHealth = 40
description = str(description)
stats = open("HeroInfo.txt","w+")
stats.write("Your name is ")
stats.write(name)
stats.write("\n")
stats.write("You are a ")
stats.write(description)
stats.write("\n")
stats.write("Your health is ")
stats.write(str(heroHealth))
stats.close()
print("Your character information and health can be found in HeroInfo.txt")
time.sleep(3)

#First choise Bob offers you an adventure programed so you really don't have much of a choise
print("Well ",name," I have a mission should you chose to accept it!")
choise1 = input("Do you accept it y/n")
while choise1 != 'y':
    if (choise1 == 'y'):
            print("excellent choice" ,name,)
    else:
            print("Ok I guess your sleepy. Come back again tomorrow when your well rested and try again.")
            time.sleep(3)
            print("You come back the next day. Bob Again asks if you want to go on an adventure")
            choise1 = input("Do you accept it y/n")
            if (choise1 == 'y'):
                print("Excellent choice" ,name,)

#Second choise how do you want to get to the dungen?
print("Bob hands you a treasure map. It appears to lead through a dungeon to a pile of treasure")
time.sleep(3)
choise2 = 'n'
while choise2 != 'y':
    choise2 = input("Do you follow it? y/n")
    if (choise2 == 'y'):
            print("You walk three steps to the right and two steps back as indicated by the map")
            time.sleep(3)
            print("You find an entrance to a dungeon")
    else:
            turns = 1
            while turns < 4 and choise2 != 'y':
                print("Ok.... who needs maps anyway?")
                time.sleep(2)
                print("You wander around aimlessly. You find nothing.")
                choise2 = input("do you want to look at the map now? y/n")
                turns = turns + 1
                if (turns == 4):
                    print("You walk three steps to the right and two steps back randomly just because.")
                    time.sleep(3)
                    print("You find an entrance to a dungeon, huh")
                    choise2 = 'y'
            if (choise2 =="y") and (turns!=4):
                turns = 4
                print("You walk three steps to the right and two steps back as indicated by the map")
                time.sleep(3)
                print("You find an entrance to a dungeon")

#Third choise dosn't really offer much I just wanted to drop kick stubborn players
choise3 = input("Do you go in? y/n")
if (choise3 == 'y'):
    print("you open the door. And walk down a dark hallway to a room.")
else:
    print("you look nervously at the dark hallway bellow. Not today you say and turn to leave")
    time.sleep(2)
    print("Too bad Sucker! Yells Bob as he drop kicks you in to the dungeon")

time.sleep(2)
print("You walk down the hallway. It's dark and damp and dungeon like")
time.sleep(2)
print("It leads to a Room.......")
time.sleep(2)
print("WITH A TROLL!!!!")
time.sleep(2)


trollHealth = 6

#This gives the player attack options, assigns dammage and tracks here and troll health. It is imposable for the hero to die due to math. 
while trollHealth > 0:
    print("It looks pissed do you....")
    if (strength == 'y'):
        print("Use your mighty triceps to punch the troll in its stupid troll face? (punch)")

    if (cleric == 'y'):
        print("Draw your mighty sword of religiosity and stab the troll in his stupid troll chest? (stab)")

    if (wizard =='y'):
        print("Cast a dope fireball using you mighty wizard powers? (fireball)")

    print("Use your might regular dude powers to.... talk to it I guess??(talk)")

    attack = input("")

    if (attack != 'talk'):
                print("It works! You ",attack," the troll in its stupid troll face.")

    else:
                print("Your scathing insults hurt the troll's feelings! Dealing physical damage to it somehow?")
    damage = int(random.randrange(1,7))
    trollHealth = trollHealth - damage
    if trollHealth <= 0:
        print("That does it! The troll falls over dead.")
        break
    else:
        print("That didn't quite do it. The troll punches you face.")
        time.sleep(2)
        print("Your current health can be viewed in the heroInfo.txt file")
        heroHealth = heroHealth - damage
        stats = open("HeroInfo.txt","a+")
        stats.write("\n")
        stats.write("Your health is now ")
        stats.write(str(heroHealth))
        stats.close()

print("Behind the troll is the treasure!")
print("Congratulations you win!")

   
    


    




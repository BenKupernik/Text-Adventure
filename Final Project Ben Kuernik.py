##Ben Kupernik
##CSC 119 470 SP20
##Final Project/2edProject V 2.0 (Added text file with hero info, Troll and Hero Health and Troll and Hero fight function)
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

#First choice Bob offers you an adventure programed so you really don't have much of a choice
print("Well ",name," I have a mission should you choose to accept it!")
choice1 = input("Do you accept it y/n")
while choice1 != 'y':
    if (choise1 == 'y'):
            print("excellent choice" ,name,)
    else:
            print("Ok I guess you're sleepy. Come back again tomorrow when your well rested and try again.")
            time.sleep(3)
            print("You come back the next day. Bob Again asks if you want to go on an adventure")
            choice1 = input("Do you accept it y/n")
            if (choise1 == 'y'):
                print("Excellent choice" ,name,)

#Second choice: how do you want to get to the dungeon?
print("Bob hands you a treasure map. It appears to lead through a dungeon to a pile of treasure")
time.sleep(3)
choice2  = 'n'
while choice2 != 'y':
    choice2 = input("Do you follow it? y/n")
    if (choice2 == 'y'):
            print("You walk three steps to the right and two steps back as indicated by the map")
            time.sleep(3)
            print("You find an entrance to a dungeon")
    else:
            turns = 1
            while turns < 4 and choice2 != 'y':
                print("Ok.... who needs maps anyway?")
                time.sleep(2)
                print("You wander around aimlessly. You find nothing.")
                choice2 = input("do you want to look at the map now? y/n")
                turns = turns + 1
                if (turns == 4):
                    print("You walk three steps to the right and two steps back randomly just because.")
                    time.sleep(3)
                    print("You find an entrance to a dungeon, huh")
                    choice2= 'y'
            if (choice2 =="y") and (turns!=4):
                turns = 4
                print("You walk three steps to the right and two steps back as indicated by the map")
                time.sleep(3)
                print("You find an entrance to a dungeon")

#Third choice doesn't really offer much I just wanted to drop kick stubborn players
choice3 = input("Do you go in? y/n")
if (choice3 == 'y'):
    print("you open the door. And walk down a dark hallway to a room.")
else:
    print("you look nervously at the dark hallway below. Not today you say and turn to leave")
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

#This gives the player attack options, assigns damage and tracks here and troll health. It is impossible for the hero to die due to math. 
while trollHealth > 0:
    print("It looks pissed do you....")
    if (strength == 'y'):
        print("Use your mighty triceps to punch the troll in its stupid troll face? (punch)")

    if (cleric == 'y'):
        print("Draw your mighty sword of religiosity and stab the troll in his stupid troll chest? (stab)")

    if (wizard =='y'):
        print("Cast a dope fireball using your mighty wizard powers? (fireball)")

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

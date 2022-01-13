
#this function collects information about the charter in the game and returns it to the main code.
def info():
    description = []
    import random
    import time
    import sys
    #exposition
    print("Welcome mighty hero! To the wonderful land of Yesteryear where thin English must be thusly spoken")
    time.sleep(2)
    print("I am Bob deliverer of exposition!")
    time.sleep(2)
    name = input("what's your name?")
    print("Well" ,name, "Come out from those shadows so I can get a look at you!")
    time.sleep(3)
    strength = input("you step from the shadows and look at your arms, are they buff y/n")
    if (strength == 'y'):
        print("You flex and strut to meet Bob Deliverer of Exposition.")
        description.append('riped ')
    else:
        print("You flex your arms. With recent advances in science it is now possible to detect a slight increase in size where your biceps should be.")
        time.sleep(2)
        print("You walk towards Bob Deliverer of Exposition hoping that you Charisma role will be high")

    time.sleep(2)

    print("As you walk towards Bob he whips out some sort of shiny thing from his pocket.")
    time.sleep(2)
    print("You recognize it as the sign of the Overly Religous Dude's Everyone Resents.")

    cleric = input("Do you feel inspired by this?y/n")
    if (cleric == 'y'):
        print("AH HA Bob says A fellow O.R.D.E.R member! Welcome Brother!!")
        description.append('overly religous ')
        time.sleep(2)
        print("You preform the secret handshake with the obligatory 360 spin fist bump.")
        time.sleep(2)
    else:
        print("Ah says Bob A heathen I see, He eyes you angrily")
        time.sleep(2)
    

    print("As you start to talk to Bob someone grabs something out of your pocket!")
    time.sleep(2)

    wizard = input("Was it a book of Spells? y/n")

    if (wizard == 'y'):
        print("You use your mind powers to grab it back from the thief.")
        description.append('wizard ')
    else:
        print("HA HA Sucker! He just stole your cursed book of unwanted truth. Guess who's examining their life choices tonight!")

    time.sleep(2)
        
    if (strength == 'n') and (cleric == 'n') and (wizard == 'n'):
        description = ('Regular dude I guess??')
    else:
        description.append('dude')
    if (strength == 'y') and (cleric == 'y') and (wizard == 'y'):
        description = ('Medievall Batman, like calm down bro it was ok to hit n you know.')
        
    print("You are a!!!???")
    time.sleep(2)
    print(*description, sep='')
    time.sleep(2)

    return[name,strength,cleric,wizard,description]



    


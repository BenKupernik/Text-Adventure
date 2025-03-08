
def trollcombat(attack,trollhealth,herohealth):

    import random
    import time
    import sys

    d = random.randrange(1,20)
    damage = random.randrange(1,6)


    if (attack != 'talk'):
        if (d >= 10):
            print("It works! You ",attack," the troll in its stupid troll face for",damage,"damage")
            trollhealth = trollhealth - damage
        else:
            print("It doesn't work! You miss")
        
        if (d == 1):
            print("In fact you" ,attack, "yourself in your own stupid face for ",damage," damage!")
            herohealth = herohealth - damage

    else:
        if (d == 20):
            print("Wow uhm it works???? The troll says hi and goes about it's business.")
            trollhealth = 0
        else:
            print("Yah the troll doesn't seem to want to talk. It eats your face off.")
            time.sleep(2)
            print("Better luck next time??")
            herohealth = 0


    return [trollhealth, herohealth]


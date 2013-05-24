#Author: Leugim Lim
#Date: 23/05/2013
#Version 1.0
#Description: 

import random
import time

def displayIntro():
    print('You wake up. The Sun hurts your eyes. You check your surroundings; you are in a forest. Something is odd, all the leaves have turned brown; it is still the middle of summer. Checking to see if you are')
    print('unharmed, you notice your skin is purple and viens are prominent. Something must have happened to you; but the only thing you can remember were parts of the war and then a blinding flash of light. You')
    print('make your way out of the forest and reach a road the branches towards a barren-looking wasteland and what seems to be an abandoned city. Which will you choose?: ')
    print

##### STARTING POINT - SELECT THE DESTINATION

def chooseArea():
    area = ''
    while area != 'wasteland' and area != 'city':
        print('Select your destination; type either wasteland or city:')
        area = raw_input()
    return area

def checkArea(chooseArea):
    if chooseArea == 'wasteland' or chooseArea == 'Wasteland':
        print('You chose to brave the empty, arid wasteland.')
        time.sleep(3)
        print('About an hour into the trek, you hear a rumbling towards the horizon...')
        time.sleep(3)
        print('Some mean-looking thugs are heading your; gunning for you on their motorbikes!...you have a choice to make --')
        time.sleep(2)
        
        nextScene = bikeGang()
        checkGang(nextScene)
        
    elif chooseArea == 'city' or chooseArea == 'City':
        print('You chose to travel to the gloomy city.')
        time.sleep(3)
        print('You hear some commotion in the distance, so you make your way through the desolate streets quietly. The sound is getting louder; seems it is coming from the corner of the housing complex...')
        time.sleep(3)
        print('You stumble upon a group of mutants; feeding on the flesh of children!...they spot you, you have a decision to make --')
        time.sleep(2)
        
        nextScene = crazedMutants()
        checkMutants(nextScene)
        
    else:
        print('You hunker down at the edge of the forest.....')
        time.sleep(3)
        print('from the sky, a meteor strikes your temple and your head instantly explodes')
        time.sleep(2)

### THE WASTELAND CHOICE SECTION - RUN INTO SAVAGE BIKER GANG

def bikeGang():
    engageGang = ''
    while engageGang != 'fight' and engageGang != 'flee':
        print('Type fight to try and hijack one of the bikes and engage against the biker gang or type flee to run away aimlessly:')
        engageGang = raw_input()
    return engageGang

def checkGang(bikeGang):
    if bikeGang == 'fight' or bikeGang == 'Fight':
        print('How daring! You chose to take on the gang. In an almost berserker fashion, with a boot to the face, you take out the closest biker around you, and went to work!')
        time.sleep(3)
        print('The biker gang was no match for your bloodlust and soon surrender to your might!')
        time.sleep(2)
        print('You are now proclaimed as the leader of the Arid Bandit -- the name of said biker gang...you and new minions were about to celebrate your coronation until...')
        time.sleep(3)
        print('A large group of military troops have ambushed your homebase, guns pointed towards you, carrying the Hawaiian flag!')
        time.sleep(3)
        print('...your choice is clear --')
        time.sleep(2)
        
        nextScene = militaryGuys()
        checkMilitary(nextScene)
        
    elif bikeGang == 'flee' or bikeGang == 'Flee':
        print('You chose the cowards way out. Running frantically like a maniac, you miraculously were able to lose the chasing gang...')
        time.sleep(3)
        print('strangely, you find yourself at the entrance of what seems like a closed-down mine.')
        time.sleep(2)
        print('Believing it be safer than standing out in the open, you head down the dark tunnel.')
        time.sleep(2)
        print('Deeper into the tunnel, hoping your eyes would adjust to the darkness, you happened upon an old gas lantern. You turn the switch...it WORKS!...')
        time.sleep(2)
        print('But...an ominous shadow is casted upon you...')
        time.sleep(2)
        print('You turn around...')
        time.sleep(3)
        print('A BEAR! A gargantuan, green BEAR!!!')
        time.sleep(2)
        print('You have little time to think! --')

        nextScene = bearCave()
        checkCave(nextScene)

    else:
        print('you are dead')

# CHOSE TO FIGHT THE GANG

def militaryGuys():
    engageMilitary = ''
    while engageMilitary != 'fight' and engageMilitary != 'reason':
        print('Type fight to order your men into combat or type reason to try and negotiate with the Hawaiian troops peacefully:')
        engageMilitary = raw_input()
    return engageMilitary

def checkMilitary(militaryGuys):
    if militaryGuys == 'fight' or militaryGuys == 'Fight':
        print('You chose to do battle against the military troop. Due to your mysterious, superb commanding skills, you and your gang of savages manage to not only defeat, but slaughter the opposing troops!')
        time.sleep(2)
        print('You kept a few alive and had them lead you to their bases. One by one, each of their bases fall; day-by-day, your personal army grows until their is none to conquer!')
        time.sleep(2)
        print('Congratulations! You are now king, and you decide to try and rebuild civilization, and to make it better than it once was...under your supreme rule!!!')
        time.sleep(5)
        
    elif militaryGuys == 'reason' or militaryGuys == 'Reason':
        print('You place your arms into to grab their attention and yield...')
        time.sleep(2)
        print('The Hawaiians let loose a barrage of bullets and rockets at you and your men! There was not a single speck of remains of either you or your gang!')
        time.sleep(3)
        print('Negotiations is for the weak!!')
        time.sleep(5)
        
    else:
        print('You chose nothing?! The Hawaiians subjugate you and your lot, and you spend all of your days as a footstool...until the Hawaiian monarch found an actual footstool and then condemned you to death.')
        time.sleep(5)

# CHOSE TO FLEE; FIND A CAVE

def bearCave():
    engageBear = ''
    while engageBear != 'fight' and engageBear != 'flee':
        print('Type fight to engage in an epic battle against this rabid, magnificent beast or type flee because its a BEAR:')
        engageBear = raw_input()
    return engageBear

def checkCave(bearCave):
    if bearCave == 'fight' or bearCave == 'Fight':
        print('Win or lose, you chose to do battle, and a be a legend!')
        time.sleep(2)
        print('Using crazy Bruce Lee kicks mixed with Chuck Norris karate chops, you begin to push back this might animal. You begin to feel hope and confidence that you might actually win...')
        time.sleep(2)
        print('Until the bear bites your head off and mauls your lifeless corpse. Nice try, but this mutated bear had no time to play with you!')
        time.sleep(5)
        
    elif bearCave == 'flee' or bearCave == 'Flee':
        print('ITS A BEAR!  Of course you chose to flee!')
        time.sleep(2)
        print('Running for dear life, you can see the exit; you can also feel the bear breath upon neck, urging you to run faster!')
        time.sleep(3)
        print('Your almost out, until...')
        time.sleep(3)
        print('The cave begins to collapse; which startles you...')
        time.sleep(3)
        print('Giving the bear the opportunity to catch-up and carves its gigantic claws into you, slicing you into pieces...the caves collapse; so there is a silver lining to all this.')
        time.sleep(5)
        
    else:
        print('Of course you died! There is a bear in your face, and you did nothing! Then again, it was BEAR! What could you have done that would have mattered?')

### THE CITY CHOICE SECTION - RUN INTO MUTANT CANNIBALS
    
def crazedMutants():
    engageMutants = ''
    while engageMutants != 'fight' and engageMutants != 'flee':
        print('Type fight to pick up a random, conveniently placed club pipe and fight your way thought these fiends or type flee to escape; climb a rusty fire escape, to the rooftop:')
        engageMutants = raw_input()
    return engageMutants

def checkMutants(crazedMutants):
    if crazedMutants == 'fight' or crazedMutants == 'Fight':
        print('Excellent! You are valiant in choosing to ward off these vile creatures!')
        time.sleep(2)
        print('You quickly picked up the pipe, and went to town on these ugly clowns')
        time.sleep(2)
        print('Covered in their green blood, you managed to ward them off, but not before you notice the bite and claws marks they have inflicted upon you...')
        time.sleep(3)
        print('This is not good...')
        time.sleep(3)
        print('Luckily, you find an hospital nearby that may have supplies that may treat your wounds; unluckiy, you head inside and find a swarm aliens; little grey men.....and they are pointing their weapons at you!')
        time.sleep(3)
        print('Decision time! --')

        nextScene = evilAliens()
        checkAliens(nextScene)
        
    elif crazedMutants == 'flee' or crazedMutants == 'Flee':
        print('You safely made it to the rooftop, and kick away the corroded escape ladder, letting it fall upon one of the mutant scum!')
        time.sleep(2)
        print('Several steps onto the rooftop, the floor beneath you cave in and fall six stories...')
        time.sleep(3)
        print('onto a wooden spike!')
        time,sleep(3)
        print('A piece of a broken stair railing is lodged through your chest, and you are bleeding...BADLY!')
        time.sleep(3)
        print('Your fall attracted the mutant horde in the surrounding area, and find yourself quickly surrounded!')
        time.sleep(2)
        print('Choose how you want to die --')

        nextScene = badRoof()
        checkSpike(nextScene)
        
    else:
        print('So you just let them eat you?! Because that is what happened...the mutants ate you...hope you are happy.')

# CHOSE TO FIGHT THE MUTANTS

def evilAliens():
    engageAliens = ''
    while engageAliens != 'fight' and engageAliens != 'surrender':
        print('Type fight to rid the building of these dastard aliens or surrender meekly:')
        engageAliens = raw_input()
    return engageAliens

def checkAliens(evilAliens):
    if checkAliens == 'fight' or checkAliens == 'Fight':
        print('You can feel the bite affecting you, might as well go out with a bang!')
        time.sleep(2)
        print('The aliens quickly open fire at you, but you barely feel the shots hit you...you feel yourself changing... ')
        time.sleep(2)
        print('You are increasingly becoming more worried as you believe you may be turning into one of those feral mutants, so you move fast, effortlessly murdering the foreign foes!')
        time.sleep(3)
        print('There were hundreds of them, but you cleared the building faster than you could have imagined...')
        time.sleep(3)
        print('and you still have your sentience! HOORAY!')
        time.sleep(3)
        print('Congratulations! You have become the ultimate being! You possess the alien ship parked ontop of the hospital, and you use it to try and find others of your kind...and everything that gets in your way!!')
        time.sleep(5)
        
    elif checkAliens == 'surrender' or checkAliens == 'Surrender':
        print('WHY?! What do you think is going to happen??')
        time.sleep(2)
        print('The alien capture you and inflicted unimaginable scientific experiments upon you!')
        time.sleep(3)
        print('You discover that the aliens were responsible for manufacturing the war that decimated the Earth!')
        time,sleep(3)
        print('And you also find out that it was these alien that experiment on your body, allowing it to survive and adapt to the mutant disease!')
        time.sleep(3)
        print('Once they have gather all the information they wanted, they eradicated your body, via disintegration.')
        time.sleep(5)
        
    else:
        print('Their ray-guns could not do any harm to you, but since you are doing nothing, the aliens climbed aboard their ship and obliterated you and the entire city into ashes with their main photonic cannon.')
        time.sleep(5)

# CHOSE TO FLEE; ONTO THE ROOFTOP

def badRoof():
    spikeChoice = ''
    while spikeChoice != 'fight' and spikeChoice != 'pull':
        print('Type fight to stand, with the spike in your chest, and brawl with the mutant horde or type pull to try and remove the spike as quickly as possible to try and escape:')
        spikeChoice = raw_input()
    return spikeChoice

def checkSpike(badRoof):
    if spikeChoice == 'fight' or spikeChoice == 'Fight':
        print('With the last of your strenght, you chose to fight; you have the soul of a warrior!')
        time.sleep(2)
        print('Your can feel how fleeting your life is...especially with the wooden spike through your chest, so...')
        time.sleep(2)
        print('With no regard for anything, you grabbed whatever you could or simply used your fist and legs and squared off with the ravenous horde!')
        time.sleep(3)
        print('It must have been a couple hours, by then, you have already removed the spike to use as a weapon, and slaughtered more than half of the mutant!')
        time.sleep(3)
        print('You are exhausted and they noticed it. They slowly creep up towards, until...')
        time.sleep(3)
        print('Several dozen armed mercenaries accidently came to your rescue...but it was too late, and you expired due to the shock of losing so much blood. The mercenaries leave...and took your body with them...')
        time.sleep(5)
        
    elif spikeChoice == 'pull' or spikeChoice == 'Pull':
        print('You try and pull the stake out from your chest...')
        time.sleep(2)
        print('You get eaten while doing so...')
        time.sleep(3)
        print('You could have die guns blazing, but noooooo')
        time.sleep(5)
        
    else:
        print('You just laid there, waiting for the inevitable end, when the earth shook around, and the ground collapse. The Molemen found you and the horde of mutants...and killed you all!')
        time.sleep(5)

##### MAIN FUNCTION - INTIALIZES THE PROGRAM AND REPLY INPUT

def main():
    playAgain = 'yes'
    while playAgain == 'yes' or playAgain =='y':
        displayIntro()
        areaChoice = chooseArea()
        checkArea(areaChoice)

        print('Do you want to play again? (yes or no)')
        playAgain = raw_input()

if __name__ == "__main__": main()

import sys
import pygame

width = 600
hight = 400 

class Game():
    def __init__(self):
        
        pygame.init(self)
        self.screen = pygame.display.set_mode((width, hight))
        

#allowed = ["left", 'right', 'forward', 'back', 'refund', 'exit']

def starting_cave():
    print(f"Welcome to Aborc caves, this is a dangerous place so be careful where you go and step. If you're not a big reader this is not for you and you can refund the game!")
    print('In the Aborc caves you choose where you go and what you do, if you type exit you will leave. No save system yet so dont expect as much')
    print("As you look up from the sign blocking the entrance into the cave, you notice 2 paths, do you choose left or right?")
    direction = input('With adventure in your heart you decide to go deeper, which direction do you choose: ')
    if direction == 'left':
        pass
    if direction == "right":
        first_right()
    else:
        print('please re-read your options and choose again.')
    
def first_right():
    print('You walk down a path thinking to yourself how safe an option you just made was, "When in doubt choose right" you think to your self and smirk.')
    print('You walk into a dimly lit chamber and there is nothing of intrest, much like in your head. Your smirk quickly fades as you realize your as plane as this chamber')
    print('After you rethink your deciscion you notice three paths out of this chamber that go deeper into the cave, you think, "Time for some change" and you decide to go deeper')
    direction = input('You can go left, right, or forward. What do you choose: ')
    if direction == "right":
        super_rare()
    elif direction =="left":
        pass
    else:
        pass

def guts_cave():
    print('You enter into a cave and notice a campfire in the middle, you slow down and strain your eyes to see deeper into the cave knowing someone is there.')
    print("you notice a man sitting against the wall with a large sword, it looks just like a large peice of iron, you cant tell if he is sleeping or awake.")
    print("you look beyond the man and notice 3 more branches in the cave, you can go exit the cave now or try and get past the mysterious man. What do you choose? left, right, forward, or exit?")

def pirates_tresure():
    print('You step into a cave and are blinded! toy step back in shock and fear. As your eyes adjust to the sudden burst of light you notice a beam of light shining down onto a large pile a treasure!')
    print("You run over to the pile of treasure and start stuffing your pockets (points +10), you fill your pockets till the wheight is felt in your knees.")
    print("As your greedy desires subside, you look around and notice 3 brances, what do you choose? left, right, forward, or exit?")
    
def super_rare():
    print('you enter into a cave and look around you notice a sign on the wall, you approach to read it.')
    print('You read the sign and look around, confused you go back to read the sign again. You think "I must have read that wrong"')
    print('You stare at the words on the sign a while longer, it says "Super Rare Cave", but all you where able to see in this cave is 3 more paths leading, left, right and forward.')
    direction = input('This is it, this time you change! What direction do you want to go? left, right, forward: ')    
    if direction == 'right':
        death_cave()
    elif direction == 'left':
        pass
    elif direction == 'forward':
        pass


def death_cave():
    print('As you walk down the path you hear a phrase being repeated. You cant quit make it out. You slow your pace and continue with caution.')
    print('you get to the mouth of the next chamber, and you can make out what is being said little bit better "and dey say". you walk in a little further to see who is reapeting this phrase.')
    print('You stand in the middle of the chamber and hear the same phrase over and over its maddening! As soon as you turn to leave you hear where its coming from!')
    print('You look up and see OverWatch one Doomfist! He slams onto the ground from a blanace spot in the cave, "ouch" you think to yourself as he chrages up his punch! He realeses it and you \nhit the wall dying with one hit')
    direction = input("Your journey is at an end, what would you like to do? exit or retry?: ")
    if direction == 'retry':
        starting_cave()
    if direction == 'exit':
        sys.exit

        





starting_cave()
#while True:
#    choice = input("What do you choose?: ")
    
#    allowed_choices = any(word in choice for word in allowed)

#    if allowed_choices != True:
#       print ("Please re-read your options and try again")
#    if choice == 'exit':
#        break
#    elif choice == 'refund':
#        print("die faggot")
#    elif choice == 'left':
#        guts_cave()
#    elif choice =="right":
#        super_rare()
#    break
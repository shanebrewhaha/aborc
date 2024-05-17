import random

allowed = ["left", 'right', 'forward', 'back', 'refund', 'exit']

def starting_cave():
    print(f"Welcome to Aborc caves, this is a dangerous place so be careful where you go and step. If you're not a big reader this is not for you and you can refund the game!")
    print('In the Aborc caves you choose where you go and what you do, if you type exit you will leave. No save system yet so dont expect as much')
    print("As you look up from the sign blocking the entrance into the cave you notice 2 brances, do you choose left or right?")

def guts_cave():
    print('You enter into a cave and notice a campfire in the middle, you slow down and strain your eyes to see deeper into the cave knowing someone is there.')
    print("you notice a man sitting against the wall with a large sword, it looks just like a large peice of iron, you cant tell if he is sleeping or awake.")
    print("you look beyond the man and notice 3 more branches in the cave, you can go exit the cave now or try and get past the mysterious man. What do you choose? left, right, forward, or exit?")

def pirates_tresure():
    print('You step into a cave and are blinded! toy step back in shock and fear. As your eyes adjust to the sudden burst of light you notice a beam of light shining down onto a large pile a treasure!')
    print("You run over to the pile of treasure and start stuffing your pockets (points +10), you fill your pockets till the wheight is felt in your knees.")
    print("As your greedy desires subside, you look around and notice 3 brances, what do you choose? left, right, forward, or exit?")

caves = [guts_cave(), pirates_tresure()]



starting_cave()
while True:
    choice = input("What do you choose?: ")
    
    allowed_choices = any(word in choice for word in allowed)

    if allowed_choices != True:
        print ("Please re-read your options and tpye one in")
    if choice == 'exit':
        break
    elif choice == 'refund':
        print("die faggot")
    else:
        random.choice(caves)


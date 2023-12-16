from sys import exit

def living_room():
    print("You are in the living room.")
    print("There is a comfortable couch and a TV.")
    print("What would you like to do?")
    choice = input("> ")

    if "couch" in choice:
        print("You sit on the couch and relax.")
        print("You feel refreshed. You win!")
        exit(0)
    elif "TV" in choice:
        print("You turn on the TV and watch your favorite show.")
        print("Time flies by. You win!")
        exit(0)
    else:
        print("You wander around the room.")
        print("There's nothing much to do here.")
        print("You decide to explore further.")
        kitchen()

def kitchen():
    print("You find yourself in the kitchen.")
    print("There's a fridge and a stove.")
    print("What do you want to do?")
    choice = input("> ")

    if "fridge" in choice:
        print("You open the fridge and find a delicious cake.")
        print("You enjoy the cake. You win!")
        exit(0)
    elif "stove" in choice:
        print("You start cooking a meal.")
        print("It smells delicious, but takes time.")
        print("You decide to explore elsewhere.")
        bedroom()
    else:
        print("You're not sure what to do here.")
        print("You decide to move on.")
        bedroom()

def bedroom():
    print("You enter the bedroom.")
    print("There's a comfy bed and a wardrobe.")
    print("What's your next move?")
    choice = input("> ")

    if "bed" in choice:
        print("You lie down on the bed and take a nap.")
        print("You wake up refreshed. You win!")
        exit(0)
    elif "wardrobe" in choice:
        print("You check the wardrobe and find some old clothes.")
        print("You try them on and have a good laugh.")
        print("You decide to explore more.")
        exit(0)
    else:
        print("You feel lost in this room.")
        print("Time to try something else.")
        living_room()

def start():
    print("Welcome! You are in a house.")
    print("There are rooms to explore.")
    print("Where would you like to start?")

    choice = input("> ")

    if "living room" in choice:
        living_room()
    else:
        print("You hesitate and choose another room.")
        bedroom()

start()

import time
import random
# lists that are use for random selection throughout the game.
famous_people = ["Matthew Mcconaughey", "Donald Trump", "Shakira",
                 "Joe Rogan", "Elon Musk"]
backpack_items = ["Camera", "Wallet", "PB&J Sandwich",
                  "Snickers Bar", "Knife", "Pair of Socks"]
animals = ["MAN BEAR PIG", "CHUPACABRA", "SAMSQUANCH",
           "GAME WARDEN", "GRIZZLY BEAR"]
# global variables
luck = 0
loot = []
person = ""


# this function is used to kick off the game.
def naked_and_afraid():
    intro()


# delayed print
def timed_print(message):
    print(message)
    time.sleep(2.5)


# used with user input to validate a correct response
def valid_choice(prompt, option1, option2):
    while True:
        choice = input(prompt).lower()
        if option1 in choice:
            break
        elif option2 in choice:
            break
        else:
            print("Please enter a valid response")
    return choice


# first function of the game
def intro():
    timed_print("\nYou find yourself awakening in the woods, naked and afraid")
    timed_print("You look around and realize you are completely alone...")
    timed_print("You hear something big rustling in the trees..."
                "Something is coming!")
    fight_or_flight()


# user faced with first decision to make, run or hide
def fight_or_flight():
    response = valid_choice("What should you do? Run away or stay where"
                            " you are and hide?\n", "run", "hide")
    if "run" in response:
        trip()
    else:
        hide()


# user option 1: hide and encounter randomly chosen character
# Luck variable changed depending on outcome from encounter
def hide():
    global luck
    creature = random.choice(animals)
    timed_print("You look around and find a dense bush to hide in...")
    timed_print("Franticlly peering through the branches, you watch "
                "as something emerges from the dark trees.")
    timed_print("Its a.... ")
    timed_print("Could it be?.... ")
    timed_print(f"Its a.... {creature}!!!")
    if creature == "MAN BEAR PIG":
        timed_print("Wierd, they exist outside South Park... "
                    "Looks like you should of ran away...  ")
        timed_print(f"The {creature} attacks you and eats you for lunch. ")
        outro()
    elif creature == "CHUPACABRA":
        timed_print("And you thought they were only in folk tales... "
                    "Looks like you should of ran away...  ")
        timed_print(f"The {creature} attacks you and eats you for lunch. ")
        outro()
    elif creature == "CHUPACABRA":
        timed_print("And you thought they were only in folk tales... "
                    "Looks like you should of ran away...  ")
        timed_print(f"The {creature} attacks you and eats you for lunch. ")
        outro()
    elif creature == "SAMSQUANCH":
        timed_print("I told you they were real Ricky! ... "
                    "Looks like you should of ran away...  ")
        timed_print(f"The {creature} attacks you and eats you for lunch. ")
        outro()
    elif creature == "GRIZZLY BEAR":
        timed_print("You are no Leonardo Dicaprio ... "
                    "Looks like you should of ran away...  ")
        timed_print(f"The {creature} attacks you and eats you for lunch. ")
        outro()
    elif creature == "GAME WARDEN":
        timed_print("You got lucky this time... "
                    "Good thing you didnt run away!!!  ")
        luck += 1
        outro()


# user trips and is faced with another decision to make
def trip():
    timed_print("You run as fast as you can through the dark forest.")
    timed_print("You trip over something...")
    timed_print("You realize its a backpack!")
    Backpack_option = valid_choice("Do you want to look inside or keep "
                                   "running without it?\n", "look", "run")
    if "run" in Backpack_option:
        meadow()
    else:
        inspect_backpack()


# 3 items from random are chosen from the global backpack_items list
# the items are placed in the global loot list
def inspect_backpack():
    global loot
    loot = random.sample(backpack_items, 3)
    timed_print("You open up the back pack and rummage around.")
    timed_print("You find the following items:")
    timed_print(loot[0])
    timed_print(loot[1])
    timed_print(loot[2])
    timed_print("\nYou take the back pack and keep running...")
    meadow()


# user encounters character randomly chosen from global famous_people list
def meadow():
    global person
    person = random.choice(famous_people)
    timed_print("In the distance you see something... "
                "its a break in the trees.")
    timed_print("Looks to be a meadow!")
    timed_print("You step into the meadow and see someone "
                "with their back to you.")
    timed_print("Curious and excited, you rush to the "
                "person and tap on their "
                f"shoulder. Around turns... {person}!?")
    # asks user if they would like to leave or stay in the game
    response = valid_choice(f"{person}: Well hello traveler... "
                            "Welcome to my neck of the woods."
                            " The look on your face tells me you "
                            "would like to leave. "
                            "Is that true?\n", "yes", "no")
    if "yes" in response:
        timed_print(f"{person}: Well that's completely understandable. "
                    "How about a trade?")
        trade()
    else:
        timed_print(f"{person}: Good because I wasnt going to "
                    "let you leave anyway!")
        knockout()


# asks the user if they have any food as a trade
def trade():
    global luck
    timed_print(f"{person}: I am pretty hungry. Unless you "
                "magically have some food hidden on you, i'm "
                "going to have to ask you a riddle before you can leave.")
    response = valid_choice(f"{person}: So do you have any "
                            "food?\n", "yes", "no")
    # if user obtained any food items from the backpack
    # they can hand it over and win
    if "yes" in response:
        if "PB&J Sandwich" in loot:
            timed_print(f"*Hands Sandwich from backpack to {person}*")
            timed_print(f"{person}: AHHH!! Thank you so much this will "
                        "do just fine! YOU WIN!")
            luck += 1
            outro()
        elif "Snickers Bar" in loot:
            timed_print(f"*Hands candy bar from backpack to {person}*")
            timed_print(f"{person}: AHHH!! Thank you so much this will "
                        "do just fine!")
            luck += 1
            outro()
        # if the user lies about having food, they loose
        else:
            timed_print(f"{person} snatches your backpack from you and dumps "
                        "out the items...")
            timed_print(f"{person}: You lie like a rug. You'll regret this!")
            knockout()
    # if the user does not have food, they must answer a riddle
    else:
        timed_print(f"{person}: no worries... riddle it is!")
        timed_print(f"{person}: Ok answer this riddle correctly "
                    "and you can leave...")
        riddle()


# user must answer a riddle to win the game
def riddle():
    global luck
    tries = 0
    luck = 0
    response = input(f"{person}: I have a head and a tail but no body. "
                     "What am I?   \n").lower()
    # user gets 5 tries before they are asked if they give up
    # if they answer the riddle correctly, the global luck variable = 1
    while True:
        if "coin" in response:
            timed_print(f"{person}: Very Good! You WIN!")
            luck = 1
            break
        else:
            tries += 1
            response = input(f"{person}: No sorry guess again...\n")
            if tries >= 5:
                give_up = valid_choice(f"{person}: Do you give "
                                       "up?\n", "yes", "no")
                # if they give up, they loose and the outro function runs
                if "yes" in give_up:
                    timed_print(f"{person}: Well that's too bad, YOU LOSE!!!")
                    luck = 0
                    break
                # if they choose not to give up, the riddle function runs again
                else:
                    luck = 2
                    break
    if luck == 0 or luck == 1:
        outro()
    else:
        riddle()


# user gets knocked out by the random character
def knockout():
    timed_print(f"{person} does a karate move and kicks you "
                "right in the head, knocking you out cold.")
    timed_print("ZZZZZ....")
    timed_print("ZZZZZ....")
    timed_print("ZZZZZ....")
    timed_print("ZZZZZ....")
    outro()


# game ending function. User is asked if they would like to play again
def outro():
    global luck
    if luck == 1:
        lucky_response = valid_choice("Would you like to play "
                                      "again?\n", "yes", "no")
        if "yes" in lucky_response:
            luck = 0
            intro()
        else:
            timed_print("THANK YOU FOR PLAYING!\n")
    else:
        timed_print("Sorry friend, you are the weakest link")
        unlucky_response = valid_choice("Would you like to play "
                                        "again?\n", "yes", "no")
        if "yes" in unlucky_response:
            luck = 0
            intro()
        else:
            timed_print("THANK YOU FOR PLAYING! \n")


naked_and_afraid()

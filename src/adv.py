from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item('rock', 'Just a rock'), Item('key', 'A strange shape looking key')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player("Pere", room["outside"])
gameOn = True
directions = ['n', 'e', 's', 'w']
# Write a loop that:
#
# print(player1.current_room.n_to, "<<<")
print(player1.current_room)
while gameOn:
    # * Prints the current room name
    # print(f"You have entered {player1.current_room.name}")
    # * Prints the current description (the textwrap module might be useful here).
    # print(player1.current_room.description)

    # * Waits for user input and decides what to do.
    action_input = input("Do you want to move or take an action? ").lower()
    if action_input == 'move':
        direction_input = input(
            "Which direction do you want to go (n/e/s,w)?: ")
        if direction_input == 'q':
            print("Thanks for playing. Bye.")
            gameOn = False
        elif direction_input not in directions:
            print("Please select a valid direction")
        else:
            direction_input += "_to"
            if getattr(player1.current_room, direction_input) == None:
                print(
                    f"There is no such direction as {direction_input}. Please try again")
                continue
            elif getattr(player1.current_room, direction_input):
                player1.current_room = getattr(
                    player1.current_room, direction_input)
                print(player1.current_room)

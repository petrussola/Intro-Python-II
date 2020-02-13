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
    # print items that the player has, for dev purposes
    player_items = ''
    player_items += f"Player {player1.name} has {len(player1.items)} items\n"
    for item in player1.items:
        player_items += f"{item.name}\n"
    print(player_items)

    # print how many items left in the room, for dev purposes
    room_items = ''
    room_items += f"Player {player1.current_room.name} has {len(player1.current_room.items)} items\n"
    for item in player1.current_room.items:
        room_items += f"{item.name}\n"
    print(room_items)

    action_input = input("What do you want to do?\n").lower()
    clean_input = action_input.split()
    if clean_input[0] == 'q':
        print("Thanks for playing. Bye.")
        gameOn = False
    elif clean_input[0] == 'move':
        if len(clean_input) == 1 or clean_input[1] not in directions:
            print("I didn't understand that. Please move n, e, s or w.")
        else:
            direction_input = f"{clean_input[1]}_to"
            if getattr(player1.current_room, direction_input) == None:
                print(
                    f"You cannot move in such direction. Try another one")
            elif getattr(player1.current_room, direction_input):
                player1.current_room = getattr(
                    player1.current_room, direction_input)
                print(player1.current_room)
    elif clean_input[0] == "pick":
        # print(player1, "<<< player items")
        # print(clean_input[1], "<<< object being picked")
        # print(getattr(
        #     player1.current_room.items["rock"], "description"), "<<< items in player class")
        for item in player1.current_room.items:
            if item.name == clean_input[1]:
                setattr(player1, "items", [*player1.items, item])
                player1.current_room.items.remove(item)
    else:
        print("Sorry, did not understand that. Do you want to move or pick up an item?")

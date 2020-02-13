from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item('rock', 'Just a rock'), Item('key', 'A strange shape looking key')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item('wallet', 'A wallet. Maybe there are EUR inside it?'), Item('shoe', 'A beautiful shoe')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item('umbrella', 'In case it rains'), Item('sunglasses', 'In case it is sunny')]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item('torch', 'Doesn\'t seem to have batteries'), Item('candle', 'A white one')]),

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

player1 = Player("Pere", room["outside"])
gameOn = True
directions = ['n', 'e', 's', 'w']

print(player1.current_room)


def missing_input():
    print(f"I didn't understand that. Can you elaborate?")


while gameOn:
    # print items that the player has, for dev purposes
    # player_items = ''
    # player_items += f"Player {player1.name} has {len(player1.items)} items\n"
    # for item in player1.items:
    #     player_items += f"{item.name}\n"
    # print(player_items)

    # # print how many items left in the room, for dev purposes
    # room_items = ''
    # room_items += f"Player {player1.current_room.name} has {len(player1.current_room.items)} items\n"
    # for item in player1.current_room.items:
    #     room_items += f"{item.name}\n"
    # print(room_items)

    action_input = input("What do you want to do?\n").lower()
    clean_input = action_input.split()
    if clean_input[0] == 'q':
        print("Thanks for playing. Bye.")
        gameOn = False
    elif clean_input[0] == 'move':
        if len(clean_input) == 1 or clean_input[1] not in directions:
            print("I didn't understand that. Please move n, e, s or w.")
        else:
            # shiny new instance method that seems to work! :)
            player1.move(clean_input[1])
            # direction_input = f"{clean_input[1]}_to"
            # if getattr(player1.current_room, direction_input) == None:
            #     print(
            #         f"You cannot move in such direction. Try another one")
            # elif getattr(player1.current_room, direction_input):
            #     player1.current_room = getattr(
            #         player1.current_room, direction_input)
            #     print(player1.current_room)
    elif clean_input[0] == "pick":
        # set up boolean variable that we will use to display message in case item is not found
        found_item = False
        # iterates over the items in the current room
        for item in player1.current_room.items:
            # if the element input by the user matches an element in the room
            if item.name == clean_input[1]:
                # add the item in the player's items list
                setattr(player1, "items", [*player1.items, item])
                # delete the item from the current_room's items list
                player1.current_room.items.remove(item)
                # set found_item to True
                found_item = True
                # call on_take method and print message
                item.on_take()
        # if found_item is False
        if not found_item:
            # print message
            print(f"There is no {clean_input[1]} in the room")
    # if user wishes to drop an object
    elif clean_input[0] == "drop":
        # if user doesn't have items
        if len(player1.items) == 0:
            # display message
            print("You don't have any items. What about picking up one first? :p")
        # if user didn't say what to drop
        elif len(clean_input) == 1:
            # print message
            missing_input()
        else:
            # we set the variable to false that will help us see if we found the item in player's pocket
            found_item = False
            # loop of items owned by player
            for item in player1.items:
                # if we find the item in player's pocket
                if item.name == clean_input[1]:
                    # return item to the room
                    setattr(player1.current_room, "items", [
                            *player1.current_room.items, item])
                    # remove item from player's pocket
                    player1.items.remove(item)
                    # set found item to True
                    found_item = True
                    # call on_drop method to print message
                    item.on_drop()
            # if we didn't find item in player's pocket
            if not found_item:
                # print a message
                print(f"You don't have a {clean_input[1]}")
    elif clean_input[0] == "i" or clean_input[0] == "inventory":
        if len(player1.items) == 0:
            print("You don't have items in your bag")
        else:
            output = ''
            output += f"You have {len(player1.items)} items in your bag: \n"
            for item in player1.items:
                output += f"{item.name}\n"
            print(output)
    else:
        print("Sorry, did not understand that. Do you want to move or pick up an item?")

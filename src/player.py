# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def __str__(self):
        if len(self.items) == 0:
            return f'{self.name} doesn\'t have any items.'
        else:
            output = 'The player has the following items:'
            for item in self.items:
                output += f'{item.name}\n'
            return output

    def move(self, direction):
        if getattr(self.current_room, f"{direction}_to") == None:
            print(f"You cannot move in such direction. Try another one")
        elif getattr(self.current_room, f"{direction}_to") != None:
            setattr(self, "current_room", getattr(
                self.current_room, f"{direction}_to"))
            self.current_room.explain()

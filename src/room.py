# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = items

    def __str__(self):
        output = ''
        output += f'You are in: {self.name}.\n{self.description}\n'
        count_item = 1
        if len(self.items) == 0:
            output += f'** There are no items to examine. **\n'
        else:
            output += f'There are the following items:\n'
            for item in self.items:
                output += f'[{count_item}] {item.name} - {item.description}\n'
                count_item += 1
        return output

    def explain(self):
        print(f"You are entering {self.name}.\n {self.description}")

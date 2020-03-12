# Implement a class to hold room information. This should have name and
# description attributes.
class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = []
    
    def display_info(self):
        print("\n\n---------------------")
        print(f"\nYou are in {self.name}. {self.description}")
        for item in self.items:
            item.display_info()
# return { boolean:false, message: "Must be direction north, south, east, or west"}
    def check_move(self, move):
        if move == "north":
            if self.n_to == None:
                return False, "There is nothing to the north"
            else:
                return True, self.n_to
        elif move == "south":
            if self.s_to == None:
                return False, "There is nothing to the south"
            else:
                return True, self.s_to
        elif move == "west":
            if self.w_to == None:
                return False, "There is nothing to the west"
            else:
                return True, self.w_to
        elif move == "east":
            if self.e_to == None:
                return False, "There is nothing to the east"
            else:
                return True, self.e_to
        else:
            return False, "Must be direction north, south, east, or west"  
    
    def check_for_item(self, name):
        item_list = list(filter(lambda item: item.name == name, self.items))
        if len(item_list) == 0:
            print(f"There is no item called {name}")
            return None
        else:
            return item_list[0]
        
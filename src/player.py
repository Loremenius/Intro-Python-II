# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, room):
        self.current_room = room
        self.items = []

    def player_action(self):
        self.current_room.display_info()
        action = input("\nWhich way will you go: ").lower().strip().split(" ")    
        if len(action) == 1:
            if action[0] == "q":
                exit()
            else:
                self.move_room(action[0])
        else:
            if action[0] == "grab":
                self.grab_item(self.current_room.check_for_item(action[1]))
            elif action[0] == "drop":
                self.drop_item(action[1])
            else:
                print("That is not a valid action")
                self.player_action()
    
    def move_room(self, move):
        move_check = self.current_room.check_move(move)
        if move_check[0] == False:
            print(f"\n{move_check[1]}")
            self.player_action()
        else:
            self.current_room = move_check[1]
            self.player_action()
    
    def grab_item(self, item):
        if item == None:
            self.player_action()
        else:
            self.items.append(item)
            self.current_room.items.remove(item)
            item.on_take()
            self.player_action()
    
    def drop_item(self, name):
        item_list = list(filter(lambda item: item.name == name, self.items))
        if item_list == None:
            print(f"There is no item called {name}")
            self.player_action()
        else:
            self.items.remove(item_list[0])
            self.current_room.items.append(item_list[0])
            self.player_action()

class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def display_info(self):
        print(f"\n{self.name}: {self.description}")
    
    def on_take(self):
        print(f"{self.name} has been picked up.")
    

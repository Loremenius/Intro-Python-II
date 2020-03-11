# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, room):
        self.current_room = room
    
    def move_room(self):
        self.current_room.display_info()
        move = input("\nWhich way will you go: ").lower().strip()
        if move == "q":
            exit()
        else:
            move_check = self.current_room.check_move(move)
        
        if move_check[0] == False:
            print(f"\n{move_check[1]}")
            self.move_room()
        else:
            self.current_room = move_check[1]
            self.move_room()

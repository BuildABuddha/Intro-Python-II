# Implement a class to hold room information. This should have name and
# description attributes.

class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

        self.item_list = []

    
    def items_to_string(self):
        if self.item_list:
            return "You see the following item(s) on the floor: " + ", ".join( [item.name for item in self.item_list] )
        else:
            return "There's nothing worth collecting here."

    
    def item_is_in_room(self, item_to_find):
        item_in_room = False

        for item in self.item_list:
            if item.name.lower() == item_to_find:
                item_in_room = True
                break

        return item_in_room

    def add_item(self, item_to_add):
        self.item_list.append(item_to_add)

    def remove_item(self, item_to_remove):
        for item in self.item_list.copy():
            if item.name.lower() == item_to_remove:
                self.item_list.remove(item)
                return item

    def get_item_description(self, item_to_find):
        for item in self.item_list:
            if item.name.lower() == item_to_find:
                return item.description

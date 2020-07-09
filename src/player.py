# Write a class to hold player information, e.g. what room they are in
# currently.

class Player(object):
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

        self.inventory = []

    def inventory_to_string(self):
        if self.inventory:
            return "You are carrying the following: " + ", ".join([item.name for item in self.inventory])
        else:
            return "You are not carrying any loot at the moment."

    def item_is_in_invetory(self, item_to_find):
        item_in_inventory = False

        for item in self.inventory:
            if item.name.lower() == item_to_find:
                item_in_inventory = True
                break

        return item_in_inventory

    def add_item(self, item_to_add):
        self.inventory.append(item_to_add)

    def remove_item(self, item_to_remove):
        for item in self.inventory.copy():
            if item.name.lower() == item_to_remove:
                self.inventory.remove(item)
                return item

    def get_item_description(self, item_to_find):
        for item in self.inventory:
            if item.name.lower() == item_to_find:
                return item.description

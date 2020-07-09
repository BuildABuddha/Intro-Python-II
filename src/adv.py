from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room(
        "Outside Cave Entrance",
        "North of you, the cave mount beckons."
        ),

    'foyer':    Room(
        "Foyer", 
        "Dim light filters in from the south. Dusty passages run north and east."
        ),

    'overlook': Room(
        "Grand Overlook", 
        "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light"
        "flickers in the distance, but there is no way across the chasm."
        ),

    'narrow':   Room(
        "Narrow Passage",
        "The narrow passage bends here from west to north. The smell of gold permeates the air."
        ),

    'treasure': Room(
        "Treasure Chamber",
        "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied "
        "by earlier adventurers. The only exit is to the south."
        ),
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

# Add items

room['foyer'].add_item(Item(
    "Rusty Sword",
    "An old, rusty sword from a long dead kingdom. Not very useful as a weapon, unless you want to give someone tetanus."
))
room['outside'].add_item(Item(
    "Torch",
    "A torch, already lit for your convencience. Probably helpful if you're planning on going somewhere dark."
))
room['treasure'].add_item(Item(
    "Gold Coin",
    "A small coin about the size of a penny made of gold. It's the only thing left after years of looting."
    "It'll make a nice souvenir for your first adventure, though."
))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Player Name", room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

player_input = ""

while player_input != "q":
    print("\nYou are at the", player.current_room.name)
    print(player.current_room.description)
    print(player.current_room.items_to_string())
    print("Where would you like to do next? (N, S, E, or W to move, or Q to quit and go home.)")
    player_input = input().lower().strip()

    # Movement commands:
    if player_input == 'n':
        if player.current_room.n_to is None:
            print("Unfortunately, you cannot go that way.")
        else:
            print("You move to the north.")
            player.current_room = player.current_room.n_to
    elif player_input == 's':
        if player.current_room.s_to is None:
            print("Unfortunately, you cannot go that way.")
        else:
            print("You move to the south.")
            player.current_room = player.current_room.s_to
    elif player_input == 'e':
        if player.current_room.e_to is None:
            print("Unfortunately, you cannot go that way.")
        else:
            print("You move to the east.")
            player.current_room = player.current_room.e_to
    elif player_input == 'w':
        if player.current_room.w_to is None:
            print("Unfortunately, you cannot go that way.")
        else:
            print("You move to the west.")
            player.current_room = player.current_room.w_to

    # Quit game command:
    elif player_input == 'q':
        print("You pack up all the loot you've collected so far and head home.")

    # Item pickup command:
    elif player_input.startswith("take ") or player_input.startswith("grab "):
        item_name = player_input[5:]
        if player.current_room.item_is_in_room(item_name):
            print(f"You take the {item_name}.")
            picked_up_item = player.current_room.remove_item(item_name)
            player.add_item(picked_up_item)
        else:
            print("You don't see that item in this room.")

    # Item drop command:
    elif player_input.startswith("drop "):
        item_name = player_input[5:]
        if player.item_is_in_invetory(item_name):
            print(f"You drop the {item_name} on the floor.")
            dropped_item = player.remove_item(item_name)
            player.current_room.add_item(dropped_item)
        else:
            print("You're not carrying one of those!")

    # Print inventory command:
    elif player_input == "i" or player_input == "inventory":
        print(player.inventory_to_string())

    # Examine item command:
    elif player_input.startswith("examine "):
        item_name = player_input[8:]
        print(item_name)
        if player.item_is_in_invetory(item_name):
            print(player.get_item_description(item_name))
        elif player.current_room.item_is_in_room(item_name):
            print(player.current_room.get_item_description(item_name))
        else:
            print("You don't see any items like that around.")

    # Unknown command:
    else:
        print("Sorry, I don't know that command.")

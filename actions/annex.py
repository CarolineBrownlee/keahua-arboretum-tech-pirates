import os
from environments import River

# cp Need to add proper imports
def annex_biome(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. River")
    print("2. Swamp")
    print("3. Coastline")
    print("4. Grassland")
    print("5. Mountain")
    print("6. Forest")
# cp Need to add mountain and forest to menu
    choice = input("Choose what you want to annex? > ")
# cp Need to change strings to display appropriately based on the README
    if choice == "1":
        river = River()
        arboretum.rivers.append(river)
    if choice == "2":
        pass
# cp Need to add functionality for append options
# cp Need to create files and classes for all missing biomes
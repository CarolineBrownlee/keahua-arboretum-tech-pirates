# Jb-Comment: Imports Go up TOP!!!
import sys
sys.path.append('../')
from animals.preyCritters import preyLists
from animals.river_dolphin import RiverDolphin
import os
# Define Calls for Each animal

# Jb-Comment: Based on the instructions seems like I will need to make a menu for when someone selects feed animal to display a list of the animals and allow them to be fed.

def animal_to_feed_menu(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Gold Dust Day Gecko")
    print("2. River Dolphin")
    print("3. Nene Goose")
    print("4. KiKakapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")
    
    choice = input("Pick a Friendly Critter! They Need Noms! >>>")
    
    if choice == "1":
        
    if choice == "2":
        pass
    if choice == "3":
        pass
    if choice == "4":
        pass
    if choice == "5":
        pass
    if choice == "6":
        pass
    if choice == "7":
        pass
    if choice == "8":
        pass
    count = 0
    animal_list = []
    
def animal_to_feed_menu(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Gold Dust Day Gecko")
    print("2. River Dolphin")
    print("3. Nene Goose")
    print("4. KiKakapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")
    
    # Setting up for loops to try and work with this and iterate through the biomes as they are altered.
    
    # for river in arboretum.rivers:
    #     print(f'River [{str(river.id)[0:8]}]')
    #     for animal in river.animals:
    #         animal_list.append(animal)
    #         count += 1
    #         print(f'     {count}. {animal.species} [{str(animal.id)[0:8]}]')
    
    # for swamp in arboretum.swamps:
    #     print(f'Swamp [{str(swamp.id)[0:8]}]')
    #     for animal in swamp.animals:
    #         animal_list.append(animal)
    #         count += 1
    #         print(f'    {count}. {animal.species} [{str(animal.id)[0:8]}]')

    # for mountain in arboretum.mountains:
    #     print(f'Mountain [{str(mountain.id)[0:8]}]')
    #     for animal in mountain.animals:
    #         animal_list.append(animal)
    #         count += 1
    #         print(f'    {count}. {animal.species} [{str(animal.id)[0:8]}]')

    # for grassland in arboretum.grasslands:
    #     print(f'Grassland [{str(grassland.id)[0:8]}]')
    #     for animal in grassland.animals:
    #         animal_list.append(animal)
    #         count += 1
    #         print(f'    {count}. {animal.species} [{str(animal.id)[0:8]}]')

    # for coastline in arboretum.coastlines:
    #     print(f'Coastline [{str(coastline.id)[0:8]}]')
    #     for animal in coastline.animals:
    #         animal_list.append(animal)
    #         count += 1
    #         print(f'    {count}. {animal.species} [{str(animal.id)[0:8]}]')

    # for forest in arboretum.forests:
    #     print(f'Forest [{str(forest.id)[0:8]}]')
    #     for animal in forest.animals:
    #         animal_list.append(animal)
    #         count += 1
    #         print(f'    {count}. {animal.species} [{str(animal.id)[0:8]}]')
    
    # If conditional for testing
    # if animal_list == []:
    #     input(
    #         'No soup for you. No soup for your animal. Pick a biome, add an animal and try again. Or hit enter to return to the main menu'
    #     )
    #     return
    
    # print("Select an animal to feed.")
    # choice = input("> ")
    
    # if int(choice) > len(animal_list):
    #     input(' You chose poorly..... Look out for crusaders with funny cups.')
    #     return
    
    # animal = animal_list[int(choice) - 1]
    
    # food_list = list(CritterVittles)
        
    # for index, food in enumerate(food_list):
    #     print(f'{index + 1}. {food}')
        
    # print("What are you feedint this critter?")
    # choice = input("> ")
    
    # try:
        
    #     if int(choice) > lent(food_list):
    #         input("Bad")
    #         return
    
    # except ValueError:
    #     input("Does not Compute Try again.")
    #     return
    
    # print(
    #     f'The {animal.species} ate a {food_list[int(choice) - 1]} for a nutritious snack'
    # )
    # choice = input('> ')
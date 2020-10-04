import json
import os

class LevelManager:
    def __init__(self , location):
        self.location = os.path.expanduser(location)
        self.level_i=""

    def set_name(self, current_name):
        self.level_i=current_name
        self.level_coordinate_dictionary = {"Levels":{self.level_i:{"Walls":[], "Players":[], "Enemies":[], "Treasure_Lives":[], "Treasure_Bullets":[], "Fences":[], "Safe_Area":[]}}}

    def append_walls_to_level(self, x, y):
        coordinate=(x, y)
        self.level_coordinate_dictionary["Levels"][self.level_i]["Walls"].append(coordinate)

    def append_players_to_level(self, x, y):
        coordinate=(x, y)
        self.level_coordinate_dictionary["Levels"][self.level_i]["Players"].append(coordinate)

    def append_enemies_to_level(self, x, y, count):
        coordinate=(x, y)
        enemy_dictionary = {"type":"Zombie", "name":str(count), "lives":3, "x_cor":x, "y_cor":y}
        self.level_coordinate_dictionary["Levels"][self.level_i]["Enemies"].append(enemy_dictionary)

    def append_treasure_lives_to_level(self, x, y):
        coordinate=(x, y)
        self.level_coordinate_dictionary["Levels"][self.level_i]["Treasure_Lives"].append(coordinate)

    def append_treasure_bullets_to_level(self, x, y):
        coordinate=(x, y)
        self.level_coordinate_dictionary["Levels"][self.level_i]["Treasure_Bullets"].append(coordinate)

    def append_fences_to_level(self, x, y):
        coordinate=(x, y)
        self.level_coordinate_dictionary["Levels"][self.level_i]["Fences"].append(coordinate)
        
    def append_safe_area_to_level(self, x, y):
        coordinate=(x, y)
        self.level_coordinate_dictionary["Levels"][self.level_i]["Safe_Area"].append(coordinate) 
        
    def saveMemoryVersionOfDatabaseToFile(self):
        json.dump(self.level_coordinate_dictionary , open(self.location, "w+"))

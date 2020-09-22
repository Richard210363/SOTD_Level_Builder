import Levels.Levels as levels_
import DataManagement.level_manager as level_manager_

level_manager=level_manager_.LevelManager("./SOTDLevelBuilderOutput.db")

#Level Builder

current_level=levels_.Levels.level_list[0]
current_map=current_level["map"]
current_name=current_level["Name"]
level_manager.set_name(current_name)
enemy_counter=0
for y in range(25):
    print(y)
    line=current_map[y]
    screen_y = 288 - (y * 24)
    for i in range(25):
        print(i)
        print(line[i])
        if line[i]=="X":
            print("found")
            screen_x = -288 + (i * 24)
            print("x: " + str(screen_x))
            print("y: " + str(screen_y))
            level_manager.append_walls_to_level(screen_x, screen_y)
        if line[i]=="P":
            print("found")
            screen_x = -288 + (i * 24)
            print("x: " + str(screen_x))
            print("y: " + str(screen_y))
            level_manager.append_players_to_level(screen_x, screen_y)
        if line[i]=="E":
            print("found")
            screen_x = -288 + (i * 24)
            print("x: " + str(screen_x))
            print("y: " + str(screen_y))
            level_manager.append_enemies_to_level(screen_x, screen_y, enemy_counter)
            enemy_counter=enemy_counter+1
        if line[i]=="L":
            print("found")
            screen_x = -288 + (i * 24)
            print("x: " + str(screen_x))
            print("y: " + str(screen_y))
            level_manager.append_treasure_lives_to_level(screen_x, screen_y)
        if line[i]=="T":
            print("found")
            screen_x = -288 + (i * 24)
            print("x: " + str(screen_x))
            print("y: " + str(screen_y))
            level_manager.append_treasure_bullets_to_level(screen_x, screen_y)
        if line[i]=="F":
            print("found")
            screen_x = -288 + (i * 24)
            print("x: " + str(screen_x))
            print("y: " + str(screen_y))
            level_manager.append_fences_to_level(screen_x, screen_y)

level_manager.saveMemoryVersionOfDatabaseToFile()
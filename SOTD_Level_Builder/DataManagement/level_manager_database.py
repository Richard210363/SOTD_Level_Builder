import DatabaseManagement.database_manager as db_manager

class level_manager_database(object):
    """Data access layer"""
    #def __init__(self):

    def set_level_attributes(self, current_name, current_level_number):
        db_manager.save_level_attributes(current_name, current_level_number)

    def set_player_attributes(self, player_name, player_lives, player_bullets, player_coordinates):
        db_manager.save_player_attributes(player_name, player_lives, player_bullets, player_coordinates)
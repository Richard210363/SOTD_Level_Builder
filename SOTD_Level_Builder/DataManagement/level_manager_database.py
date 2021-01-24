import DatabaseManagement.database_manager as db_manager

class level_manager_database(object):
    """Data access layer"""
    #def __init__(self):

    def set_level_attributes(self, current_name, current_level_number):
        db_manager.save_level_attributes(current_name, current_level_number)

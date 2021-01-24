import DatabaseManagement.database_manager as db_manager

class level_manager_database(object):
    """Data access layer"""
    #def __init__(self):

    def set_name(self, current_name):
        db_manager.save_level_name(current_name)

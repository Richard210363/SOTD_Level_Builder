import mysql.connector as mysql


db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "myrootpassword",
    database = "sotd"
)

cursor = db.cursor()

#print(db)

#cursor.execute("SHOW TABLES")

#tables = cursor.fetchall()

#for table in tables:
#    print(table)

def save_level_attributes(level_name, level_number):
    query = "INSERT INTO level_start_conditions (name, number, lives, bullets) VALUES (%s, %s, %s, %s)"
    values = (level_name, level_number, 5, 10)

    cursor.execute(query, values) #execute the command
    db.commit() # Tell the database to commit

    print(cursor.rowcount, "record inserted")

def save_player_attributes(player_name, player_lives, player_bullets, player_coordinates):
    query = "INSERT INTO player_start_conditions (name, lives, bullets, coordinate) VALUES (%s, %s, %s, %s)"
    values = (player_name, player_lives, player_bullets, GeomFromText('Point(39.0 55.0)'))

    cursor.execute(query, values) #execute the command
    db.commit() # Tell the database to commit

    print(cursor.rowcount, "record inserted")    
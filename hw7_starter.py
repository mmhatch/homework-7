# SI 201 HW7
# Your name:
# Your student id:
# Your email:
# Who or what you worked with on this homework (including generative AI like ChatGPT):
# If you worked with generative AI also add a statement for how you used it.
# e.g.:
# Asked ChatGPT for hints on debugging and for suggestions on overall code structure
#
# Did your use of GenAI on this assignment align with your goals and guidelines in your Gen AI contract? If not, why?

import unittest
import sqlite3
import json
import os


def read_data_from_file(filename):
    """
    Reads data from a file with the given filename.

    Parameters
    -----------------------
    filename: str
        The name of the file to read.

    Returns
    -----------------------
    dict:
        Parsed JSON data from the file.
    """
    full_path = os.path.join(os.path.dirname(__file__), filename)
    f = open(full_path)
    file_data = f.read()
    f.close()
    json_data = json.loads(file_data)
    return json_data


def set_up_database(db_name):
    """
    Sets up a SQLite database connection and cursor.

    Parameters
    -----------------------
    db_name: str
        The name of the SQLite database.

    Returns
    -----------------------
    Tuple (Cursor, Connection):
        A tuple containing the database cursor and connection objects.
    """
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + "/" + db_name)
    cur = conn.cursor()
    return cur, conn


def set_up_types_table(data, cur, conn):
    """
    Sets up the Types table in the database using the provided Pokemon data.

    Parameters
    -----------------------
    data: list
        List of Pokemon data in JSON format.

    cur: Cursor
        The database cursor object.

    conn: Connection
        The database connection object.

    Returns
    -----------------------
    None
    """
    type_list = []
    for pokemon in data:
        pokemon_type = pokemon["type"][0]
        if pokemon_type not in type_list:
            type_list.append(pokemon_type)
        if len(pokemon["type"]) > 1:
            pokemon_type = pokemon["type"][1]
            if pokemon_type not in type_list:
                type_list.append(pokemon_type)
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Types (id INTEGER PRIMARY KEY, type TEXT UNIQUE)"
    )
    for i in range(len(type_list)):
        cur.execute(
            "INSERT OR IGNORE INTO Types (id,type) VALUES (?,?)", (i,
                                                                   type_list[i])
        )
    conn.commit()

#############################################################################
####### START HERE, DO NOT CHANGE THE CODE FROM THE ABOVE FUNCTIONS ########
#############################################################################

def build_pokemon_table(data, cur, conn):
    """
    Parameters
    -----------------------
    data: str
        Stores pokemon.json, written in JSON format
    
    cur: 
        database cursor
    
    conn: 
        database connection

    Returns
    -----------------------
    Nothing
    """
    # Your code implementation here



def pokemon_in_defense_range(defense_min, defense_max, cur):
    """
    Parameters
    -----------------------
    defense_min: int

    defense_max: int
    
    cur: 
        database cursor

    Returns
    -----------------------
    list:
        list of tuples [(pokemon_id, name, defense),...]
    """
    # Your code implementation here



def balanced_pokemon_above_speed_min(speed_min, cur):
    """
    Parameters
    -----------------------
    speed_min: int
    
    cur: 
        database cursor

    Returns
    -----------------------
    list:
        list of tuples [(pokemon_id, name, defense, attack, speed),...]
    """
    # Your code implementation here



def pokemon_with_defense_difference(defense_difference, cur):
    """
    Parameters
    -----------------------
    defense_difference: int

    Returns
    -----------------------
    list:
        list of tuples [(name, defense, special_defense, difference),...]
    """
    # Your code implementation here


def pokemon_by_type_value(type_value, cur):
    """
    Parameters
    -----------------------
    type_value: str

    Returns
    -----------------------
    list:
        list of tuples [(pokemon_id, name, type1, type2),...]

    """
    # Your code implementation here



def pokemon_fastest_of_type(type, cur):
    # extra credit
    """
    Parameters
    -----------------------
    type: str

    cur:
        database cursor
    
    Parameters
    -----------------------
    list:
        list of tuples: [(name, type, speed), ...]
    """
    # Your code implementation here





### DO NOT CHANGE TEST CASES ###
class TestAllMethods(unittest.TestCase):
    def setUp(self):
        path = os.path.dirname(os.path.abspath(__file__))
        self.conn = sqlite3.connect(path + "/" + "pokemon.db")
        self.cur = self.conn.cursor()
        self.data = read_data_from_file("pokemon.json")


    def test_pokemon_table(self):
        self.cur.execute("SELECT * from Pokemon")
        pokemon_list = self.cur.fetchall()
        self.assertEqual(len(pokemon_list), 500)
        self.assertEqual(len(pokemon_list[0]), 10)
        self.assertIs(type(pokemon_list[0][0]), int)
        self.assertIs(type(pokemon_list[0][1]), str)
        self.assertIs(type(pokemon_list[0][2]), int)
        self.assertIs(type(pokemon_list[0][3]), int)
        self.assertTrue(pokemon_list[3][3] is None)
        self.assertIs(type(pokemon_list[0][4]), int)
        self.assertIs(type(pokemon_list[0][5]), int)
        self.assertIs(type(pokemon_list[0][6]), int)
        self.assertIs(type(pokemon_list[0][7]), int)
        self.assertIs(type(pokemon_list[0][8]), int)
        self.assertIs(type(pokemon_list[0][9]), int)


    def test_pokemon_in_defense_range(self):
        x = pokemon_in_defense_range(40, 55, self.cur)
        self.assertEqual(len(x), 131)
        self.assertEqual(len(x[0]), 3)
        self.assertEqual(x[0], (0, 'bulbasaur', 49))
        self.assertEqual(x[1], (3, 'charmander', 43))
        self.assertEqual(x[-1], (498, 'pignite', 55))

        y = pokemon_in_defense_range(100, 200, self.cur)
        self.assertEqual(len(y), 85)
        self.assertEqual(len(y[0]), 3)
        self.assertEqual(y[0], (8, 'blastoise', 100))
        self.assertEqual(y[1], (27, 'sandslash', 110))
        self.assertEqual(y[-1], (493, 'victini', 100))


    def test_balanced_pokemon_above_speed_min(self):
        x = balanced_pokemon_above_speed_min(40, self.cur)
        self.assertEqual(len(x), 181)
        self.assertEqual(len(x[0]), 5)
        self.assertEqual(x[0], (0, 'bulbasaur', 49, 49, 45))
        self.assertEqual(x[1], (1, 'ivysaur', 63, 62, 60))
        self.assertEqual(x[-1], (496, 'serperior', 95, 75, 113))

        y = balanced_pokemon_above_speed_min(95, self.cur)
        self.assertEqual(len(y), 26)
        self.assertEqual(len(y[0]), 5)
        self.assertEqual(y[0], (99, 'voltorb', 50, 30, 100))
        self.assertEqual(y[1], (100, 'electrode', 70, 50, 150))
        self.assertEqual(y[-1], (496, 'serperior', 95, 75, 113))


    def test_pokemon_with_defense_difference(self):
        x= pokemon_with_defense_difference(15, self.cur)
        self.assertEqual(len(x), 100)
        self.assertEqual(len(x[0]), 4)
        self.assertEqual(x[0], ('bulbasaur', 49, 65, 16))
        self.assertEqual(x[1], ('ivysaur', 63, 80, 17))
        self.assertEqual(x[-1], ('palkia', 100, 120, 20))

        y = pokemon_with_defense_difference(35, self.cur)
        self.assertEqual(len(y), 36)
        self.assertEqual(len(y[0]), 4)
        self.assertEqual(y[0], ('beedrill', 40, 80, 40))
        self.assertEqual(y[1], ('abra', 15, 55, 40))
        self.assertEqual(y[-1], ('gallade', 65, 115, 50))


    def test_pokemon_by_type_value(self):
        x = pokemon_by_type_value("grass", self.cur)
        self.assertEqual(len(x), 58)
        self.assertEqual(len(x[0]), 4)
        self.assertEqual(x[0], (0, "bulbasaur", "grass", "poison"))
        self.assertEqual(x[-1], (496, "serperior", "grass", None))

        y = pokemon_by_type_value("water", self.cur)
        self.assertEqual(len(y), 92)
        self.assertEqual(len(y[0]), 4)
        self.assertEqual(y[0], (6, "squirtle", "water", None))
        self.assertEqual(y[-1], (489, "manaphy", "water", None))


    ### UNCOMMENT TEST CASES BELOW FOR EXTRA CREDIT ###

    # def test_pokemon_fastest_of_type(self):
    #     x = pokemon_fastest_of_type("fire", self.cur)
    #     self.assertEqual(len(x), 1)
    #     self.assertEqual(len(x[0]), 3)
    #     self.assertEqual(x[0], ("infernape", "fire", 108))

    #     y = pokemon_fastest_of_type("water", self.cur)
    #     self.assertEqual(len(y), 2)
    #     self.assertEqual(len(y[0]), 3)
    #     self.assertEqual(y[0], ('floatzel', 'water', 115))
    #     self.assertEqual(y[1], ('starmie', 'water', 115))

    #     z = pokemon_fastest_of_type("ice", self.cur)
    #     self.assertEqual(len(z), 1)
    #     self.assertEqual(len(z[0]), 3)
    #     self.assertEqual(z[0], ('weavile', 'ice', 125))
        
    #     a = pokemon_fastest_of_type("dark", self.cur)
    #     self.assertEqual(len(a), 2)
    #     self.assertEqual(len(a[0]), 3)
    #     self.assertEqual(a[1], ('weavile', 'dark', 125))


def main():
    json_data = read_data_from_file("pokemon.json")
    cur, conn = set_up_database("pokemon.db")
    set_up_types_table(json_data, cur, conn)
    build_pokemon_table(json_data, cur, conn)
    conn.close()
    # FEEL FREE TO USE THIS SPACE TO TEST OUT YOUR FUNCTIONS


if __name__ == "__main__":
    main()
    unittest.main(verbosity=2)
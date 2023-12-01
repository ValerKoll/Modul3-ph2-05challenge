from lib.recipe import Recipe

class RecipeRepository:
    # Parameters #1: connection - object connection
    # Property #1: (same as above)
    # Actions: none
    def __init__(self, connection):
        self._connection = connection
        
    def all(self):
        # RETURN THE FULL LIST OF FOOD RECIPES
        # Parameters: none
        # Actions: calls connection and sends query, stores result in recipe's istances
        # Return: list of istances -list
        table_name = "recipes"
        query = f"SELECT * FROM {table_name};"
        rows = self._connection.execute(query)
        entries_list = []
        for row in rows:
            entries_list.append(Recipe(row['id'], row['name'], row['cook_time'], row['score']))
        return entries_list
    
    def find(self, id):
        # TAKE 1 PARAMETER AND send QUERY to the DATABASE
        # Parameters #1: id of the food receipe - int
        # Actions: ncalls connection and execute command
        # Return: instance of 1 recipe -string
        rows = self._connection.execute(
            'SELECT * FROM recipes WHERE id = %s', [id])
        row = rows[0]
        return Recipe(row['id'], row['name'], row['cook_time'], row['score'])
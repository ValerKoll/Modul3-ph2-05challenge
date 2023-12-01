class Recipe:
    # Parameters #3: recipe_name - string, cooking_time - int, recipe_score - int
    # Property #3: (same as above)
    # Actions: none
    def __init__(self, recipe_id, recipe_name, cooking_time, recipe_score):
        self.id = recipe_id
        self.name = recipe_name
        self.time = cooking_time
        self.score = recipe_score
    
    def __eq__(self, other):
        # COMPARE 2 OBJECTS DICTIONARY
        # Parameters #1: other - instance of class Recipe
        # Actions: none
        # Return: True if 2 __dict__ are same -boolean
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        # FORMAT PROPERTIES IN THIS INSTANCE
        # Parameters:  none
        # Actions: none
        # Return: f"Recipe: {name} Cooking time:{time} Score:{score}" -string
        return f"Recipe({self.name}, {self.time}, {self.score})"
    
a = Recipe(1, "Fried Food", 10, 2)
print(str(a))
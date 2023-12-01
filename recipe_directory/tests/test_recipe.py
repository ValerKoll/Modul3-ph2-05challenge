from lib.recipe import Recipe

"""
constructs with an id, name and genre
"""
def test_recipe_constructs():
    recipe_inst = Recipe(1, "Fried Food", 10, 2)
    result = recipe_inst.name
    expected = "Fried Food"
    assert result == expected
    result = recipe_inst.time
    expected = 10
    assert result == expected
    result = recipe_inst.score
    expected = 2
    assert result == expected

"""
We can format recipe to strings nicely __repr__
"""
def test_recipe_format_nicely():
    recipe_inst = Recipe(1, "Fried Food", 10, 2)
    assert str(recipe_inst) == "Recipe(Fried Food, 10, 2)" 
"""
We can compare two identical instance, And have them be equal __eq__
"""
def test_recipe_are_equal():
    recipe_inst = Recipe(1, "Fried Food", 10, 2)
    recipe_inst2 = ""
    assert recipe_inst == Recipe(1, "Fried Food", 10, 2)
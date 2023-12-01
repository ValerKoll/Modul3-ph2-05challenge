from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

# >>> remember to add conftest.py in tests/
"""
When we call Recipe Repository .all()
We get a list of objects reflecting the seed data.
"""
def test_get_all_records(db_connection):
    db_connection.seed("seeds/recipe_table.sql")
    repo_inst = RecipeRepository(db_connection)

    result = repo_inst.all()
    expected = [
        Recipe(1, 'Fried fun', 10, 2),
        Recipe(2, 'Stew beef', 19, 4),
        Recipe(3, 'Pork down', 20, 4),
        Recipe(4, 'Noodles up', 13, 3)
    ]
    assert result == expected
    
    
"""
When we call Recipe Repository .find()
We get a single object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/recipe_table.sql")
    repo_inst = RecipeRepository(db_connection)

    result = repo_inst.find(3)
    expected = Recipe(3, 'Pork down', 20, 4)
    
    assert result == expected
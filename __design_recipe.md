# == DESIGN RECIPE ==

## 1. Describe the Problem
```
As a food lover,
So I can stay organised and decide what to cook,
I'd like to keep a list of all my recipes with their names.

As a food lover,
So I can stay organised and decide what to cook,
I'd like to keep the average cooking time (in minutes) for each recipe.

As a food lover,
So I can stay organised and decide what to cook,
I'd like to give a rating to each of the recipes (from 1 to 5).
```

## 2. List actions/properties
```
Properties: food to cook, receipe names
Actions: store name in the list

Properties: time takes to cook, average - minutes
Actions: store time in the list

Properties: score for each recipes, 1- 5
Actions: store score in the list
```

## 3. Design the table

### Scheme
---
TABLE: `recipes`
| Record                | Properties | data type   |
| --------------------- | ---------- | ----------  |
| recipe                | id         | SERIAL      |
|                       | name       |  VARCHAR    |
|                       | cook_time  |  INT        |
|                       | score      |  INT        |


### SQL
------
#### recipe_table:
```sql
---use these SQL cmd as common header:
-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS ...;
DROP SEQUENCE IF EXISTS ..._id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS ..._id_seq;
[...]
----end common SQL----


--table1
CREATE TABLE recipes (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) 
  cook_time INTEGER,
  score INTEGER
);
```

### Create the table
----
```bash
(use createdb first if DB does not exist)
psql -h 127.0.0.1 recipe_directory_1 < recipe_table.sql
```


## 4. Design the Program Interface

> Main (app.py)   
>> Recipe  
>> Recipe Repository    
>> Database Connector 
>
>> Database on PostgresSQL 

## 5. TestDriving Classes
```python
class Recipe:
    # Parameters #3: recipe_name - string, cooking_time - int, recipe_score - int
    # Property #3: (same as above)
    # Actions: none

    # Methods #2:
        __eq__()
            # COMPARE 2 OBJECTS DICTIONARY
            # Parameters #1: other - instance of class Recipe
            # Actions: none
            # Return: True if 2 __dict__ are same -boolean
        __repr___()
            # FORMAT PROPERTIES IN THIS INSTANCE
            # Parameters:  none
            # Actions: none
            # Return: f"Recipe: {name} Cooking time:{time} Score:{score}" -string

class RecipeRepository:
    # Parameters #1: connection - object connection
    # Property #1: (same as above)
    # Actions: none

    # Methods #2:
        all()
            # RETURN THE FULL LIST OF FOOD RECIPES
            # Parameters: none
            # Actions: calls connection and sends query, stores result in recipe's istances
            # Return: list of istances -list
        find()
            # TAKE 1 PARAMETER AND send QUERY to the DATABASE
            # Parameters #1: id of the food receipe - int
            # Actions: ncalls connection and execute command
            # Return: instance of 1 recipe -string
```

## 6. Create Examples as Tests

#### TEST DATABASE
```python
"""
When I seed the database
I get some records back
"""
def test_database_connection(db_connection):

```
#### TEST CLASS RECIPE
``` python
"""
constructs with an id, name and genre
"""
def test_recipe_constructs():

"""
We can format recipe to strings nicely __repr__
"""
def test_recipe_format_nicely():

"""
We can compare two identical instance, And have them be equal __eq__
"""
def test_recipe_are_equal():

```
#### TEST CLASS RECIPEREPOSITORY
```python
>>>remember conftest.py
"""
When we call ArtistRepository#all
We get a list of Artist objects reflecting the seed data.
"""
def test_get_all_records(db_connection): 

"""
When we call ArtistRepository#find
We get a single Artist object reflecting the seed data.
"""
def test_get_single_record(db_connection):

```


## 7. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._



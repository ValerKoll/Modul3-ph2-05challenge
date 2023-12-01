-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255), 
  cook_time INTEGER,
  score INTEGER
);


INSERT INTO recipes (name, cook_time, score) VALUES ('Fried fun', 10, 2);
INSERT INTO recipes (name, cook_time, score) VALUES ('Stew beef', 19, 4);
INSERT INTO recipes (name, cook_time, score) VALUES ('Pork down', 20, 4);
INSERT INTO recipes (name, cook_time, score) VALUES ('Noodles up', 13, 3);
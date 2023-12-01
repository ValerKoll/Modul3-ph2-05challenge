# connetion establish using conftest.py

"""
When I seed the database
I get some records back
"""
def test_database_connection(db_connection):
    db_connection.seed("seeds/database_connection.sql")
    db_connection.execute("INSERT INTO test_table (name) VALUES ('Fried Toma');")
    result = db_connection.execute("SELECT * FROM test_table;")
    expected = [
        {'id':1, 'name':'first_record'},
        {'id':2, 'name':'Fried Toma'}
        ]
    assert result == expected
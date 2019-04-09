import psycopg2
con = psycopg2.connect(
    database  = "jopatech",
    user = "postgres",
    host = "localhost",
    password = "david",
    port ="5432"
)
cur = con.cursor()
con.autocommit = True
if con:
    print("successfull")
else:
    print("error")
def create_table_landlords():
    table = "CREATE TABLE IF NOT EXISTS {} (id serial PRIMARY KEY, district VARCHAR(30), division VARCHAR(30),typeOfHouse VARCHAR(100), numberOfRooms INTEGER, monthly_rent INTEGER, cman_name VARCHAR(30), cman_phone VARCHAR(12));".format('landlords')
    cur.execute(table)
def create_table_register():
    table = "CREATE TABLE IF NOT EXISTS {} (id serial PRIMARY KEY, fname VARCHAR(100), lname VARCHAR(30), username VARCHAR(30), date DATE , email VARCHAR(30), pword VARCHAR(30));".format('register')
    cur.execute(table)
def insert_landlords(district, division, typeofhouse, numofrooms, mrent, cman_name, cman_phone, table_name):
    inserted = "INSERT INTO {} (district, division, typeOfHouse, numberOfRooms, monthly_rent, cman_name, cman_phone) VALUES (%s, %s, %s, %s, %s, %s, %s);".format(table_name)
    values = (district, division, typeofhouse, numofrooms, mrent, cman_name, cman_phone)
    cur.execute(inserted, values)
def insert_registered(firstname, lastname, username, date, email, password, table_name):
    inserted = "INSERT INTO {} (fname, lname, username, date, email, pword) VALUES (%s, %s, %s, %s, %s, %s);".format(table_name)
    values = (firstname, lastname, username, date, email, password)
    cur.execute(inserted, values)
def update(username, password):
    updated = "UPDATE {} SET uname = %s, pword = %s WHERE id = id;".format('landlords')
    values = (username, password)
    cur.execute(updated, values)
def query_landlords():
    querried = "SELECT * FROM {};".format('landlords')
    cur.execute(querried)
    items = cur.fetchall()
    for item in items:
        print(item)
def query_login_registered():
    querried = "SELECT fname, pword FROM {} WHERE id = id;".format('register')
    cur.execute(querried)
    items = cur.fetchall()
    user_details = {}
    for fname, pword in items:
        user_details[fname] = '{}'.format(pword)
    return user_details
x = query_login_registered()
#query_landlords()
query_login_registered()
create_table_landlords()
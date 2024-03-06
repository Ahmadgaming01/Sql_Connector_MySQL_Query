import mysql.connector


#connect to the database

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'sakila',

)


cursor = db.cursor()
#write mysql query  -->

# cursor.execute('SELECT first_name , last_name FROM actor')


# cursor.execute('SHOW DATABASES') ------>>   show all databases

#-----------------------------------<<<>>>>------------------------------------------- ---

#result = cursor.fetchall()       ----->>>        fetch all data from the table
# for x in result:
#     print(x)

#-----------------------------------<<<>>>>----------------------------------------------
#result = cursor.fetchone() # ---->>               fetch one data from the table
# print(result)

#-----------------------------------<<<>>>>----------------------------------------------


# name = 'JOHN', #  %s  -->  use this to avoid sql injection

# cursor.execute('SELECT first_name , last_name FROM actor WHERE first_name = %s' , name)

# result = cursor.fetchall()
# for x in result:
#     print(x)

#-----------------------------------<<<>>>>----------------------------------------------

# #query to write mysql  query
# query = 'INSERT INTO actor (first_name , last_name) VALUES (%s , %s)'

# #values data to insert into database
# values = ('ahamd','khan')

# # to insert data in to database
# cursor.execute(query,values)

# #fetch all data from the table
# result = cursor.fetchall()

# #save the changes
# db.commit()

# #print the data
# print(cursor.rowcount, 'was inserted')



#-----------------------------------<<<>>>>----------------------------------------------

#to insert many data in to database



# #query to write mysql  query
# query = 'INSERT INTO actor (first_name , last_name) VALUES (%s , %s)'

# #values data to insert into database
# values = [('squery','khan'),
#         ('samar','qaea'),
#         ('hamad','khan'),
#         ('saead','jan'),]

# # to insert data in to database
# cursor.executemany(query,values)

# #save the changes
# db.commit()

# #print the data
# print(cursor.rowcount, 'was inserted')

#-----------------------------------<<<>>>>----------------------------------------------

#to update data in to database



#query to write mysql  query
# query = 'UPDATE actor SET first_name =%s , WHERE first_name = %s'

# #values data to insert into database
# values = ('squery','khan'),


# # to insert data in to database
# cursor.executemany(query,values)

# #save the changes
# db.commit()

# #print the data
# print(cursor.rowcount, 'was updated')


#-----------------------------------<<<>>>>----------------------------------------------

#to update data in to database



#query to write mysql  query
query = 'DELETE FROM actor WHERE first_name = %s'

#values data to insert into database
values = ('squery',)


# to insert data in to database
cursor.execute(query,values)

#save the changes
db.commit()

#print the data
print(cursor.rowcount, 'was deleted')
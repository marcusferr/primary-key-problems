import psycopg2
# connect to default database
conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
conn.set_session(autocommit=True)
cur = conn.cursor()

#create_table_queries
#songplay_table_create = "CREATE TABLE IF NOT EXISTS songplay_table (artist_id varchar, artist_latitude int, artist_longitude int, artist_location varchar, artist_name varchar, song_id varchar, title varchar, duration int, year int);"

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplay_table (
start_time timestamp,
userid int,
songplay_id text PRIMARY KEY NOT NULL,
level text,
song_id varchar,
artist_id varchar,
sessionid text,
location text,
userAgent text)""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS user_table (
userid int PRIMARY KEY NOT NULL,
first_name varchar,
last_name varchar,
gender varchar,
level varchar)""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS song_table (
song_id varchar PRIMARY KEY NOT NULL,
title varchar, 
artist_id varchar, 
year int, 
duration int)""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artist_table (
artist_id varchar PRIMARY KEY NOT NULL,
artist_name varchar, 
artist_location text, 
artist_latitude float, 
artist_longitude float)""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time_table (
start_time timestamp PRIMARY KEY NOT NULL,
hour int, 
day int,
month int,
year int,
weekday int,
week int)""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplay_table
(userId, 
songplay_id, 
level, 
song_id, 
artist_id, 
session_id, 
start_time
artist_location,
user_agent) \
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""")

user_table_insert = ("""INSERT INTO user_table
(userId, 
firstName,
lastName,
gender, 
level) \
VALUES (%s, %s, %s, %s, %s)""")

    
song_table_insert = ("""INSERT INTO song_table
song_id, 
title, 
artist_id, 
year, 
duration) \
VALUES (%s, %s, %s, %s, %s)""")
                     

artist_table_insert = ("""INSERT INTO artist_table
(artist_id, 
artist_name, 
artist_location, 
artist_latitude, 
artist_longitude) \
VALUES (%s, %s, %s, %s, %s)""")
                         
time_table_insert = ("""INSERT INTO time_table

hour, 
day,
month,
year,
weekday,
week) \
VALUES (%s, %s, %s, %s, %s, %s)""")

#drop_table_queries

songplay_table_drop =   "DROP table IF EXISTS songplay_table"  

user_table_drop =       "DROP table IF EXISTS user_table"

song_table_drop =       "DROP table IF EXISTS song_table"

artist_table_drop =     "DROP table IF EXISTS artist_table"

time_table_drop =       "DROP table IF EXISTS time_table"

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
insert_data_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
song_select_queries = []

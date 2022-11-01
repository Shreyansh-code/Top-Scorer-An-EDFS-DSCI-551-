import os
import mysql.connector
import pandas as pd

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shreyansh12"
)
cursor = db.cursor()

def goals(name,part,goal):
    cursor.execute('use dsci551')
    cursor.execute('select player_name from table_{0}_{1} where goals>{2};'.format(name,part,goal))
    print(cursor.fetchall())



def xG(name,part,xG1, xG2):
    cursor.execute('use dsci551')
    cursor.execute('select player_name from table_{0}_{1} where xG>{2} and xG<{3};'.format(name,part,xG1, xG2))
    print(cursor.fetchall())




def searchGoals(name,part,goal):
    cursor.execute('use dsci551')
    cursor.execute('select player_name from table_{0}_{1} where goals={2};'.format(name,part,goal))
    print(cursor.fetchall())

searchGoals('eeplss', 1, 13)
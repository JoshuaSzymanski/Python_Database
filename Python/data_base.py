 # -*- coding: utf-8 -*-

"""Creating a MySQL Database with Python"""

# import modules
import os
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, text

print(sqlalchemy.__version__)
print(os.getcwd())

# creates data 
datas = ['Weight', 'Hight', 'Calorie Count', 'Time', 'Meals', 'Miles Ran']
dates = [
    'input', 'input', 
    'input', 'input', 
    'input', 'input'
]
values = [0, 0, 0, 0, 0, 0]

# creates dataframe
data = pd.DataFrame(list(zip(names, dates, values)),
    columns =['symbol', 'date', 'price'])

# credentials for MYSQL
usr = ''
pwd = ''
host = '000.0.0.0'
port = 0000
dbName = 'testdb'
tableName = 'tableName'

# creates engine
engine = create_engine( f"mysql+mysqldb://{usr}:{pwd}@{host}:{port}/{dbName}", 
    echo=True, 
    future=True)

# creates table
data.to_sql(name=tableName, con=engine, if_exists='replace')

with engine.connect() as conn:
    result = conn.execute(text("tableName;"))
    for row in result:
        print(row)


with engine.connect() as conn:
    result = conn.execute(text("tableName"))
    for row in result:
        print(f"""
              index: {row.index}
              data: {row.datas} 
              date: {row.date} 
              values: {row.values}
              """)
              
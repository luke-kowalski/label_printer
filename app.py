import pyodbc
import settings

CONNECTION_STRING = 'DRIVER={};SERVER={};DATABASE={};UID={};PWD={}'.format(
    settings.sql_driver,
    settings.sql_server,
    settings.sql_database,
    settings.sql_username,
    settings.sql_password,
)

cnxn = pyodbc.connect(CONNECTION_STRING)
cursor = cnxn.cursor()

cursor.execute(settings.sql_query) 
rows = cursor.fetchall() 

for row in rows:
    print(str(row.NAME) + '-' + str(row.ID))
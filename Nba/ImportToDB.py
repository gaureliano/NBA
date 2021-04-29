import mysql.connector
import json
from mysql.connector import errorcode
# Obtain connection string information from the portal
config = {
  'host':'localhost',
  'user':'root',
  'password':'admin123',
  'database':'rest_with_asp_net_udemy'
}

# Construct connection string
try:
   conn = mysql.connector.connect(**config)
   print("Connection established")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with the user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor = conn.cursor()

# Drop previous table of same name if one exists
  cursor.execute("DROP TABLE IF EXISTS NBA;")
  print("Finished dropping table (if existed).")

  # Create table
  cursor.execute("CREATE TABLE NBA (id serial PRIMARY KEY, POS TINYINT(10), PLAYER varchar(80) NOT NULL, TEAM varchar(80) NOT NULL, TOTAL int(4) NOT NULL);")
  print("Finished creating table.")

  # Inserindo dados da NBA no DB
  arquivoJSON = open('NBA/ranking.json','r')
  data = json.loads(arquivoJSON.read())
  for n in range(0,10):
    POS=data['points'][n]['POS']
    PLAYER=data['points'][n]['PLAYER']
    TEAM=data['points'][n]['TEAM']
    TOTAL=data['points'][n]['TOTAL']
    print(POS, PLAYER, TEAM, TOTAL)
    cursor.execute("INSERT INTO NBA(POS, PLAYER, TEAM, TOTAL) VALUES ({}, '{}' ,'{}' ,{}) ;".format(POS,PLAYER,TEAM,TOTAL))
    # cursor.close()
 
  conn.commit()
  cursor.close()
  conn.close()
  print("Done.")
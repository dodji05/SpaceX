import requests
import json
import sqlite3

url = "https://api.spacexdata.com/v3/rockets"

data = requests.get(url)

rockets = json.loads(data.text)

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
print("Connexion réussie à SQLite")
for row in rockets:
    sql = "INSERT INTO Capsules_rockets (rocket_id, rocket_name,rocket_type,active,stages,boosters,cost_per_launch," \
          "success_rate_pct,country,company,wikipedia,description) " \
          "VALUES (1, 1,1, 1,1, 1,1, 1,1, 1,1,1)"

    # cur.execute("INSERT INTO Capsules_rockets (rocket_id, rocket_name,rocket_type,active,stages,boosters,"
    #             "cost_per_launch,success_rate_pct,country,company,wikipedia,description) VALUES (?, ?,?, ?,?, ?,?, ?,"
    #             "?, ?,?,?)",
    #                (row['rocket_id'], row['rocket_name'], row['rocket_type'], row['active'],
    #                 row['stages'], row['boosters'], row['cost_per_launch'],row['success_rate_pct'],row['country'],row['company'],row['wikipedia'],['description']))


    print(sql)
conn.commit()
cur.close()
conn.close()
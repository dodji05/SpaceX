import requests
import json
import sqlite3
import urllib.request

url = "https://api.spacexdata.com/v3/rockets"

data = requests.get(url)

rockets = json.loads(data.text)


liste = []

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

#
# liste.append(row['rocket_id'])
#     liste.append(row['rocket_name'])
#     liste.append(row['rocket_type'])
#     liste.append(row['active'])
#     liste.append(row['stages'])
#     liste.append(row['boosters'])
#     liste.append(row['cost_per_launch'])
#     liste.append(row['success_rate_pct'])
#     liste.append(row['country'])
#     liste.append(row['company'])
#     liste.append(row['wikipedia'])
#     liste.append(row['description'])
#
# print(liste)
#

# def insert_into(liste):
#     # try:
#     conn = sqlite3.connect('db.sqlite3')
#     cur = conn.cursor()
#     print("Connexion réussie à SQLite")
#
#     sql = "INSERT INTO Capsules_rockets (rocket_id, rocket_name,rocket_type,active,stages,boosters,cost_per_launch," \
#           "success_rate_pct,country,company,wikipedia,description) " \
#           "VALUES (?, ?,?, ?,?, ?,?, ?,?, ?,?,?)"
#
#     cur.executemany(sql, liste)
#     conn.commit()
#     cur.close()
#     conn.close()
#     print("Connexion SQLite est fermée")
#
#
# # except sqlite3.Error as error:
# #     print("Erreur lors de l'insertion dans la table person", error)
#
# #
# # liste = [('Alex', 'Paris'),
# #          ('Bob', 'Lille'),
# #          ('Emily', 'Nantes')]
#
# insert_into(liste)

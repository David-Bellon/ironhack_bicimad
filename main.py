import pandas as pd
import json

df = pd.read_csv("/home/david/Escritorio/pythonProjects/Caca/trips_23_02_February-csv/trips_23_02_February.csv", sep=";")
df = df.dropna().reset_index().drop(columns=["index"])
unlock_lat = []
unlock_lon = []
for d in df["geolocation_unlock"]:
    d = json.loads(d.replace("'", "\""))
    unlock_lat.append(d["coordinates"][1])
    unlock_lon.append(d["coordinates"][0])

lock_lat = []
lock_lon = []
for d in df["geolocation_lock"]:
    d = json.loads(d.replace("'", "\""))
    lock_lat.append(d["coordinates"][1])
    lock_lon.append(d["coordinates"][0])


df = df.drop(columns=["geolocation_unlock", "geolocation_lock"])

df["unlock_latitude"] = unlock_lat
df["unlock_longitude"] = unlock_lon

df["lock_latitude"] = lock_lat
df["lock_longitude"] = lock_lon

df["unlock_date"] = df["unlock_date"].apply(lambda x: x.replace("T", " "))
df["lock_date"] = df["lock_date"].apply(lambda x: x.replace("T", " "))

df.to_csv("good_data.csv", index=False)
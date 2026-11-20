import csv
import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()
key=os.getenv("API_KEY")
print("key loaded")

data=[]
with open("employees.csv","r")as f:
    reader=csv.DictReader(f)
    for row in reader:
        row["salary"]=int(row["salary"])
        data.append(row)
print("Rows read:",len(data))

# writing json
with open("employees.json","w")as f:
    json.dump(data,f,indent=2)

high=[]
for x in data:
    if x["salary"]>50000:
        high.append(x)
print("High earners:",len(high))

# high earners csv
with open("high_earners.csv","w",newline="")as f:
    w=csv.DictWriter(f,fieldnames=["name","salary","city"])
    w.writeheader()
    for x in high:
        w.writerow({"name":x["name"],"salary":x["salary"],"city":x["city"]})

# calling the api
try:
    r=requests.get("https://jsonplaceholder.typicode.com/users",timeout=5)
    users=r.json()
    for u in users[:3]:
        print(u["id"], "-", u["name"],"-", u["email"])
    first=users[0]
    city=first.get("address",{}).get("city","unknown")
    print("city:",city)

    with open("users.json","w")as f:
        json.dump(users,f,indent=2)
except requests.exceptions.Timeout:
    print("Timeout error")
except requests.exceptions.ConnectionError:
    print("Connection error")

# checking 404
try:
    r2=requests.get("https://jsonplaceholder.typicode.com/users/9999",timeout=5)
    if r2.status_code==404:
        print("/users/9999 -> 404 Not found")
    else:
        print(r2.status_code)
except requests.exceptions.Timeout:
    print("Timeout error")
except requests.exceptions.ConnectionError:
    print("Connection error")
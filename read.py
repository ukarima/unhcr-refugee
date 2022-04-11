import requests

count = []

loc = "http://localhost:3001/countries"
response = requests.get(loc)
res = response.json()
for i in range(len(res)):
    count.append(int(res[i]["refugees"]))


print(min(count), max(count))

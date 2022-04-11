import requests

countries = []
available_coa = []
coa = []


def available_country():
    response = requests.get(
        "https://api.unhcr.org/population/v1/countries/?limit=&page=3%C2%AEion=&unhcr_region="
    )
    res = response.json()["items"]
    for i in range(len(res)):
        coa.append(res[i]["code"])


available_country()
for country in coa:
    response = requests.get(
        "https://api.unhcr.org/population/v1/population/?limit=&page=&yearFrom=&yearTo=&year=2021&coa="
        + country
    )
    print(response.status_code)
    if response.status_code == 200:
        res = response.json()["items"]
        if len(res) != 0:
            available_coa.append(country)
        print(len(res))
    else:
        pass
print(available_coa)
print(len(available_coa))

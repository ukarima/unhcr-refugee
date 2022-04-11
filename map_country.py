import requests
import json

countries = []
coa = []


def available_country():
    response = requests.get(
        "https://api.unhcr.org/population/v1/countries/?limit=&page=3%C2%AEion=&unhcr_region="
    )

    res = response.json()["items"]
    for i in range(len(res)):
        if res[i]["code"] in coa:
            r_response = requests.get(
                "https://api.unhcr.org/population/v1/population/?limit=&page=&yearFrom=&yearTo=&year=2021&coa="
                + (res[i]["code"])
            )
            r_res = r_response.json()["items"]
            print(r_res[0]["refugees"])
            countries.append(
                {
                    "id": res[i]["id"],
                    "code": res[i]["code"],
                    "iso": res[i]["iso"],
                    "name": res[i]["name"],
                    "region": res[i]["region"],
                    "refugees": r_res[0]["refugees"],
                    "asylum_seekers": r_res[0]["asylum_seekers"],
                    "idps": r_res[0]["idps"],
                    "stateless": r_res[0]["stateless"],
                    "ooc": r_res[0]["ooc"],
                    "vda": r_res[0]["vda"],
                }
            )

    with open("db_1.json", "a") as json_file:
        json.dump(countries, json_file, indent=4, separators=(",", ": "))


available_country()

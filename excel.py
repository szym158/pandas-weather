import pandas as pd

products = [
    {
        "nazwa":"Pomidory",
        "cena": 20,
        "kraj": "PL"
    },
    {
        "nazwa":"Jabłka",
        "cena": 10,
        "kraj":"FR"
    }
]

def create_excel(data):

    df = pd.DataFrame(data)
    df["czas"] = "01-01-1970 12:12:12"
    filtered = df[ df["cena"] < 15 ]
    only_names = df["nazwa"]
    sorted = df.sort_values(by="cena",ascending=True)
    countries = df["kraj"].unique()
    group_by_country = df["kraj"].value_counts().reset_index()
    group_by_country.columns = ["Kraj","Liczba"]

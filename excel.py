import pandas as pd
import os

def append_to_excel(new_data):

    df_new = pd.DataFrame([new_data])

    if os.path.exists("dane_pogodowe.xlsx"):
        df_existing = pd.read_excel("dane_pogodowe.xlsx")
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_combined = df_new

    df_combined.to_excel("dane_pogodowe.xlsx", index=False)

def append_to_csv(new_data):
    df_new_csv = pd.DataFrame([new_data])
    if os.path.exists("dane_pogodowe.csv"):
        df_existing_csv = pd.read_csv("dane_pogodowe.csv")
        df_combined_csv = pd.concat([df_existing_csv, df_new_csv], ignore_index=True)
    else:
        df_combined_csv = df_new_csv
    df_combined_csv.to_csv("dane_pogodowe.csv", index = False)
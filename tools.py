def wind_speed(x):
    result = x * 3.6
    return round(result, 2)

def stopnie_celsjusza(k):
    result = k - 273.15
    return round(result, 2)

def append_to_csv(new_data):
    df_new_csv = pd.DataFrame([new_data])
    if os.path.exists("dane_pogodowe.csv"):
        df_existing_csv = pd.read_csv("dane_pogodowe.csv")
        df_combined_csv = pd.concat([df_existing_csv, df_new_csv], ignore_index=True)
    else:
        df_combined_csv = df_new_csv
    df_combined_csv.to_csv("dane_pogodowe.csv", index = False)

import pandas as pd
import string

df_main = pd.DataFrame()
url = 'https://en.wikipedia.org/wiki/List_of_airports_by_IATA_airport_code:_'
for i in list(string.ascii_uppercase):
    list_url = url+i
    df = pd.read_html(list_url)[0]
    df.columns = df.columns.droplevel(1)
    df_main = df_main.append(df)

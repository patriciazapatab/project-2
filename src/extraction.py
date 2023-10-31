import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_transform_table (url):
    res = requests.get(url).content
    soup = BeautifulSoup(res, "html.parser")
    table = soup.find("table")
    table_html = str(table)
    df_variable = pd.read_html(table_html)[0] 
    
    return df_variable


def combined_dataframe(url_list):
    combined_df = pd.DataFrame()
    for url in url_list:
        df_variable = get_transform_table(url)
        combined_df = pd.concat([combined_df, df_variable], ignore_index=True)
        combined_df = combined_df.drop(['Rank'], axis = 1) #We want to avoid the duplication of the Rank column on the merge

    return combined_df


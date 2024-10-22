import sqlite3
import pandas as pd
import os


base_path = f"{os.getcwd()}"

file_path = os.path.join(os.path.dirname(base_path), 'data/ctg-studies-tiny.csv')
df = pd.read_csv(file_path)


df.rename(columns={'Unnamed: 0': 'sequence'}, inplace=True)

conn = sqlite3.connect('../data/ctg-studies-tiny.db')

df.to_sql('tiny_dataset', conn, if_exists='replace', index=False)

conn.close()

if __name__ == "__main__":
    print("Sqlite Database Created")

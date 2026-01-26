import pandas as pd

df2_url = 'https://raw.githubusercontent.com/vishans/CSI4142-Datasets/refs/heads/main/Assignment%201/vgsales.csv'
df2 = pd.read_csv(df2_url)

print(df2.head())
import pandas as pd

# Normal CSV
df = pd.read_csv('pokemon_data.csv')
print(df.head(3))
print(df.tail(3))

# tab separated file
df_delimiter = pd.read_csv('pokemon_data.txt', delimiter='\t')
print(df.head(5))

# You are at 10:09! https://www.youtube.com/watch?v=vmEHCJofslg
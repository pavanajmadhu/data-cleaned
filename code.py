import pandas as pd 
import csv

df = pd.read_csv("merged_dataset.csv")
print(df.columns)
print(df.shape)
del df ["Luminosity"]
del df ["Star_name.1"]
del df ["Distance.1"]
del df ["Mass.1"]
del df ["Radius.1"]
del df ["Unnamed: 0"]
del df ["Unnamed: 6"]
print(df.columns)
df.to_csv("main.csv")
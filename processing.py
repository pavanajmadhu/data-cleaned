import pandas as pd
import csv

df=pd.read_csv("final.csv")

del df["luminosity"]
df=df[df["Distance"].notna()]
df=df[df["Mass"].notna()]
df=df[df["Radius"].notna()]
df.to_csv("stars-cleaned.csv")
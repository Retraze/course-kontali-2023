import pandas as pd
import numpy as np
from pathlib import Path

dirpath = Path("datasets/kontali")

people = [
    {"name": "bob", "age": 23},
    {"name": "alice", "age": 34}
]

df_people = pd.DataFrame(people)


df_ssb = pd.read_csv(dirpath / "ssb_export.csv",
                     encoding="latin-1",
                     delimiter=";",
                     index_col="ID"
                    )


# missing data

df_nan = pd.DataFrame(np.random.randn(10, 3), columns=list("xyz"))
df_nan.iloc[2:4, 0] = np.nan
df_nan.iloc[4:6, 1] = np.nan
df_nan.iloc[5:8, 2] = np.nan

# reindexing data
df_reindex = pd.DataFrame(
  {'A': [2, 2, 2], 'B': [3, 2, 2]},
  index=["x", "y", "z"]
)


# 
df_games = pd.DataFrame([
    {"name": "Mario", "level1": 3, "level2": 42},
    {"name": "Sonic", "level1": 7, "level2": 16}
]) 
df_games = df_games.set_index("name")


df_sort = pd.DataFrame(
    [[4,6,12], [8,6,7], [18, 14,74]], 
    columns=["B", "C", "A"], 
    index=[24,14,2]
)

# time series data
values = pd.date_range("1/1/2023", periods=500, freq="S")
ds_ts = pd.Series(np.random.randint(0, 250, len(values)), index=values)

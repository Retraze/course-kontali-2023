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
df_nan = pd.DataFrame(np.random.randn(10, 3), columns=list("ABC"))

df_nan.iloc[3:5, 0] = np.nan

df_nan.iloc[4:6, 1] = np.nan

df_nan.iloc[5:8, 2] = np.nan
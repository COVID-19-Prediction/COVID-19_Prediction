import pandas as pd
from typing import List

def timesplit(df: pd.DataFrame, t, vars: List[str]):
    assert t > 0, "Timeshift must be larger than 0"
    out_df = df.iloc[t:-2]
    for var in vars:
        out_df[f"{var}+1"] = df[var].shift(-1)
        for i in range(1, t+1):
            out_df[f"{var}-{i}"] = df[var].shift(i)
    return out_df

if __name__ == "__main__":
    df = pd.read_csv('us-counties.csv')
    pd.set_option('display.max_rows', df.shape[0]+1)
    data = df[(df.county == 'Cuyahoga') & (df.state == 'Ohio')]
    print(timesplit(data, 1, ["cases", "deaths"]))


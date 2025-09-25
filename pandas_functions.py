from main import df
import pandas as pd

print(df)

columns = df.columns

if len(columns) == 0:
    raise ValueError(f"No columns found. Length is {len(columns)}")

target_column = 'amount'

if not target_column in columns: #For my case I am targetting amount, be free to change this later on
    raise ValueError("The amount column was not found")


valid = (df['isUsed'] == True | df['transaction_ref'].notnull())
mean = df.loc[valid, target_column].mean()

# I am using query to set conditions for the rows I would like to target
total = df.loc[valid, target_column].sum()

print(f"The amount avarage is {mean}\nThe amount total is {total}")


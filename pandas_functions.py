from main import df
import pandas as pd

columns = df.columns

if len(columns) == 0:
    raise ValueError(f"No columns found. Length is {len(columns)}")

target_column = 'amount'

if not target_column in columns: #For my case I am targetting amount, be free to change this later on
    raise ValueError("The amount column was not found")


# I am using query to set conditions for the rows I would like to target
valid = (df['isUsed'] == True | df['transaction_ref'].notnull())
amount_data = df.loc[valid, target_column]
mean = amount_data.mean()

total = amount_data.sum()

meadian = amount_data.median()

'''
Broke the convention here as I needed more analysis.
I did not stick to the name hardcoded to the target_column variable and started exploring data as per interes
'''
all_time_customer = df.loc[valid, 'name'].value_counts().idxmax()

all_time_customer_valid_offer = (df['name'] == all_time_customer)

all_time_customer_favorite = df.loc[all_time_customer_valid_offer, target_column].mean()

print(f"The amount avarage is {mean}\nThe amount total is {total}\nThe median amount is {meadian}\nCustomer with most purchases is {all_time_customer}\n{all_time_customer} made an average purchase of {all_time_customer_favorite}")


import pandas as pd
database = 'Database.csv'

df = pd.read_csv(database)

index = df[df['Account Number'] == 4221571].index.values.astype(int)[0]
print(len(df))
print(index)

if df.iloc[index][3] != 1234:
    print('wong')
else:
    print("success")

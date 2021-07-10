import pandas as pd
df = pd.read_csv ('C:\\peter\\book\\dv\\project\\us-states-new.csv')
df = df[df['Total Cases']!=0]
df.to_csv ('C:\\peter\\book\\dv\\project\\us-states-new-2.csv', index=False)

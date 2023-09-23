import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('ggplot')
pd.options.display.max_columns = 200
df = pd.read_csv('coaster_db.csv')

df = df[['coaster_name','Capacity', 'Drop', 'height_value', 'height_unit', 'height_ft', 'year_introduced']].copy()

df = df.rename(columns={'coaster_name':'Name','Capacity':'Capacity',
                   'Drop':'Drop',
                   'height_value':'Height V',
                   'height_unit':'Height U',
                   'height_ft':'Height F',
                   'year_introduced':'Year'})

print(df.shape)
print(df.head(15))

df.drop(['Year','Drop','Year','Capacity'], axis=1, inplace=True)
print(df.columns)
print(df.head(15))

df.dropna(subset=['Height U'], inplace=True)
print(df.head(15))

df['Together'] = df['Height V'].astype(str) + ' ' + df['Height U']
print(df.head(15))

df.loc[df['Height U'] == "m", 'Height Feet'] = df['Height F']
df.loc[df['Height U'] != "m", 'Height Feet'] = df['Height V']
df.drop(['Height V','Height U','Height F','Together'], axis=1, inplace=True)
print(df.head(15))


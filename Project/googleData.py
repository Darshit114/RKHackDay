import pandas as pd
import numpy as np

    
df = pd.read_csv('googleplaystore.csv')

#Clean the data

to_drop = ['Reviews','Size','Price','Content Rating','Genres',
            'Last Updated','Current Ver','Android Ver']

df.drop(to_drop, inplace=True, axis=1)

#cwd = Category Wise Data
cwd = df[1:].pivot(columns='Category')

#gives Average Ratings of different Catagories
avg_ratings = cwd[['Rating']].mean()

print(avg_ratings)











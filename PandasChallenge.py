import numpy as np
import pandas as pd


df =pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv', usecols=[0,1,2,3,5])

columns = ['Manufacturer', 'Model', 'Type']

df[columns] =  df[columns].replace(np.nan, 'missing', regex = True)

df = df.set_index(columns, drop = False, verify_integrity= True)

df.index = [df.index.get_level_values(0)+'_'+df.index.get_level_values(1)+'_'+df.index.get_level_values(2)]

print df.head()
print df.index.is_unique
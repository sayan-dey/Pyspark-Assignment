
# Question 1
# Counted number of airports for COUNTRY = nan (i.e, null value) also

import pandas as pd
import sys

inputfile = 'airports.csv'
cpu_cnt=int(sys.argv[1]) #not req here
outputfile = open(sys.argv[2], "w")

df = pd.read_csv(inputfile)
#print(df)
uniq_countries=df['COUNTRY'].unique()
for i in uniq_countries:
    count=len(df[df['COUNTRY'] == i])
    if count > 0:
        outputfile.write('{},{}\n'.format(i, count))
    else: # for null values in 'COUNTRY'
        outputfile.write('{},{}\n'.format(i, df['COUNTRY'].isnull().sum()))
 
outputfile.close() 


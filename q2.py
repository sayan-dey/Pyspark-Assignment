
# Question 2
# Counted number of airports for COUNTRY = nan (i.e, null value) also

import pandas as pd
import sys

inputfile = 'airports.csv'
cpu_cnt=int(sys.argv[1]) # not req here
outputfile = open(sys.argv[2], "w")

mx=-1
res='none'

df = pd.read_csv(inputfile)
#print(df)
uniq_countries=df['COUNTRY'].unique()
for i in uniq_countries:
    count=len(df[df['COUNTRY'] == i])
    if count == 0: # for null values in 'COUNTRY'
        count=df['COUNTRY'].isnull().sum()
    if count>mx:
        mx=count
        res=i    

outputfile.write(res) 
outputfile.close() 



# Question 3
# Counted airports for NAME = nan (i.e, null value) also

import pandas as pd
import sys

inputfile = 'airports.csv'
cpu_cnt=int(sys.argv[1]) # not req here
outputfile = open(sys.argv[2], "w")

df = pd.read_csv(inputfile)
#print(df)

for ind in df.index:
    if (df['LATITUDE'][ind]>=10 and df['LATITUDE'][ind]<=90) and (df['LONGITUDE'][ind]>=-90 and df['LONGITUDE'][ind]<=-10):
        outputfile.write(df['NAME'][ind])
        outputfile.write('\n')
 
outputfile.close() 


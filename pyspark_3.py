import sys
import pyspark
from pyspark.sql import SparkSession
from pyspark.context import SparkContext
from pyspark.sql.functions import *
cpu_cnt=int(sys.argv[1])
inputfile= 'airports.csv'
outputfile=open(sys.argv[2],"w")

spa_cont=SparkSession.builder.appName("Q3")
spa_cont=spa_cont.getOrCreate()
data=spa_cont.read.csv(inputfile,header=True)
condition1=(data.LATITUDE>=10)&(data.LATITUDE<=90)
condition2=(data.LONGITUDE>=(-90))&(data.LONGITUDE<=(-10))
grouped=data.filter(condition1 & condition2)
repartitioned=grouped.repartition(cpu_cnt)
repartitioned.toPandas().to_csv(outputfile,index=False)
spa_cont.stop()
outputfile.close()

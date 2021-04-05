import sys
import pyspark
from pyspark.sql import SparkSession
from pyspark.context import SparkContext
from pyspark.sql.functions import *
cpu_cnt=int(sys.argv[1])
inputfile= 'airports.csv'
outputfile=open(sys.argv[2],"w")

spa_cont=SparkSession.builder.appName("Q1")
spa_cont=spa_cont.getOrCreate()
data=spa_cont.read.csv(inputfile,header=True)
group_BY=data.groupBy("COUNTRY")
group_BY=group_BY.count()
repartitioned=group_BY.repartition(cpu_cnt)
repartitioned.toPandas().to_csv(outputfile,index=False)
spa_cont.stop()
outputfile.close()

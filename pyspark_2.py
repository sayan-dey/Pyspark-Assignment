import sys
import pyspark
from pyspark.sql import SparkSession
from pyspark.context import SparkContext
from pyspark.sql.functions import *
cpu_cnt=int(sys.argv[1])
inputfile = 'airports.csv'
outputfile=open(sys.argv[2],"w")

spa_cont=SparkSession.builder.appName("Q2")
spa_cont=spa_cont.getOrCreate()
data=spa_cont.read.csv(inputfile,header=True)
repartitioned=data.repartition(cpu_cnt)
group_By=repartitioned.groupBy('COUNTRY')
group_By=group_By.count().sort(desc('count'))
select_country=group_By.select('COUNTRY').first()
highest=select_country[0]

outputfile.write(highest)
spa_cont.stop()
outputfile.close()

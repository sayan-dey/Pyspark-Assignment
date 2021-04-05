# Data Systems Assignment 5

* Format to run the programs: ```python3 program_name num_of_CPUs output_filename``` 
* For example, to run program 1: ```python3 pyspark_1.py 2 output.txt```
* Assumption: It is assumed that the input file name will be ```airports.csv``` and it will be present in the directory where codes will be present.

* For question 1: I have considered airports for COUNTRY = nan or NA(i.e, null value).
* For question 2: Here also, I have considered airports for COUNTRY = nan or NA(i.e, null value).
* For question 3: Now here, I have considered airports for NAME = nan or NA(i.e, null value) also.
* So simply speaking, I have not discared the null values.

* When a csv file is read using pandas, null value is considered as nan. But when a csv file is read using pyspark, null value is considered as NA.

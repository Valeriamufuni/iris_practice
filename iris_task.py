import csv
import pandas as pd


### Approach 1 - raw Python 

def approach_one():

	with open('iris.csv') as iris:
	    reader = csv.reader(iris)
	    for row in reader:
	        print (row)

# approach_one()

### Approach 2 - Pandas


def approach_two():

    df = pd.read_csv('iris.csv')
    df.head(50)
    print(df.head(50))
    #import pdb; pdb.set_trace();

#approach_two()

### Minimum value ###

def find_min():
	
	df = pd.read_csv('iris.csv')
	minvalue = df['PetalLength'].min()
	print(minvalue)

find_min()

# min(PetalWidth) = 0.1
# min(SepalLength) = 4.3
# min(SepalWidth) = 2.0
# min(PetalLength) = 1.0

#df = pd.read_csv('iris.csv')
#min_value = (df['PetalWidth'].min())
#print(min_value)

### Maximum value ###


def find_max():

	df = pd.read_csv('iris.csv')
	maxvalue = df['PetalWidth'].max()
	print(maxvalue)

#find_max()

# max(SepalLength) = 7.9
# max(SepalWidth) = 4.4
# max(PetalLength) = 6.9
# max(PetalWidth) = 2.5


### Mean value ###


def find_mean():

	df = pd.read_csv('iris.csv')
	meanvalue = df['PetalWidth'].mean()
	print(meanvalue)

#find_mean()

# mean(SepalLength) = 5.8
# mean(SepalWidth) = 3.05
# mean(PetalLength) = 3.8
# mean(PetalWidth) = 1.2

### Delete raws ###

def number_of_rows():

	df = pd.read_csv('iris.csv')
	total_rows = df['SepalLenth'].count
	print(total_rows) # 150 rows

#number_of_rows()

# Task: delete 10% from the begining and 10% from the end of the dataframe

def del_rows():

	df = pd.read_csv('iris.csv')
	deleterows = df.drop(labels=range(0,15), axis=0) #delete first 15 rows
	print(deleterows)

#del_rows()


#def del_rows(): # did not work

#	df = pd.read_csv('iris.csv')
#	deleterows = df.drop(labels=range(-1,-16), axis=0) #delete last 15 raws
#	print(deleterows)

#del_rows()

print("\n\n============\n\n")
def del_rows_2():              # method works

    df = pd.read_csv('iris.csv')
    deleterows = df.drop(labels=range(135,149), axis=0) #delete last 15 raws
    print(deleterows)

del_rows_2()






































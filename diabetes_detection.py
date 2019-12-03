import pandas 
import numpy
import math
import matplotlib.pyplot as plt
import csv


def euclidian_distance(a,b):
	sq_data=0
	for i in range(len(a)):
		sq_data=sq_data + (float(a[i])-float(b[i]))**2

	sq_root=math.sqrt(sq_data)
	return sq_root	

data=[]
with open ("./diabetes.csv",'rb') as f:
	reader=csv.reader(f)
	for row in reader:
		data.append(row)


for row in range(len(data)):
	if(row==0):
		continue
	data[row][0]=float(data[row][0])
	data[row][0]=data[row][0]*1.0
	data[row][0]=data[row][0]/0.2
	# print(data[row][0])

for row in range(len(data)):
	if(row==0):
		continue
	data[row][1]=float(data[row][1])
	data[row][1]=data[row][1]*1.0
	data[row][1]=data[row][1]/2
	# print(data[row][1])


for row in range(len(data)):
	if(row==0):
		continue
	data[row][2]=float(data[row][2])
	data[row][2]=data[row][2]*1.0
	data[row][2]=data[row][2]/1.3
	# print(data[row][2])

for row in range(len(data)):
	if(row==0):
		continue
	data[row][3]=float(data[row][3])
	data[row][3]=data[row][3]*1.0
	# print(data[row][2])

for row in range(len(data)):
	if(row==0):
		continue
	data[row][4]=float(data[row][4])
	data[row][4]=data[row][4]*1.0
	data[row][4]=data[row][4]/10
	# print(data[row][4])

for row in range(len(data)):
	if(row==0):
		continue
	data[row][5]=float(data[row][5])
	data[row][5]=data[row][5]*1.0
	# print(data[row][4])


for row in range(len(data)):
	if(row==0):
		continue
	data[row][6]=float(data[row][6])
	data[row][6]=data[row][6]*1.0
	data[row][6]=data[row][6]*20
	# print(data[row][6])

for row in range(len(data)):
	if(row==0):
		continue
	data[row][7]=float(data[row][7])
	data[row][7]=data[row][7]*1.0
	# print(data[row][6])

for row in range(len(data)):
	if(row==0):
		continue
	data[row][8]=float(data[row][8])
	data[row][8]=data[row][8]*1.0
	# print(data[row][6])


# print(data)	


testing_data=[]
training_data=[]

l=(len(data)*3)/4
training_data=data[1:l]
testing_data=data[l : ]



success=0
failure=0
accuracy_plot=[]
k_value=[]
for k in range(100):

	for point in range(len(testing_data)):

		unSortedList=[]
		label=-1
		for item in range(len(training_data)):
			dist=euclidian_distance(testing_data[point],training_data[item])
			classification=training_data[item][8]
			unSortedList.append((dist,classification))

		
		unSortedList=sorted(unSortedList)
		
		countTrue=0
		countFalse=0
		for i in range(k):
			if unSortedList[i][1]==1 :
				countTrue=countTrue+1
			else:
				countFalse=countFalse+1
		
		if countTrue>countFalse:
			label=1
		else :
			label=0
			

		if label ==testing_data[point][8] :
			success=success+1
		else :
			failure=failure +1

		

	# print(k)
	success=success*1.0
	failure=failure*1.0
	accuracy=((success/(success+failure))*100)
	# print(accuracy)

	k_value.append(k)
	accuracy_plot.append(accuracy)


for i in range(len(k_value)):
	plt.scatter(k_value[i],accuracy_plot[i],color='r',s=30)

plt.show()	

		
			







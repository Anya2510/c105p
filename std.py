import math
import csv

with open('data1.csv',newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)
data=file_data[0]
def mean(data):
    n=len(data)
    total=0
    for x in data:
        total=total+int(x)
    mean=total/n
    return mean
squareList=[]
for i in data:
    a=int(i)-mean(data)
    a=a**2
    squareList.append(a)
sum=0
for k in squareList:
    sum=sum+k
result=sum/(len(data)-1)
std_deviation=math.sqrt(result)
print(std_deviation)
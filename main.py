import math
import statistics
import csv

with open('data.csv') as f:
    reader = csv.reader(f)
    fileData = list(reader)

data = fileData[0]

def mean(data) :
  n=len(data)
  total=0

  for x in data :
    total+=int(x)
  
  mean=total/n
  return mean

sltd = []

for num in data :
  a = int(num)-mean(data)
  a = a**2
  sltd.append(a)

sum = 0

for i in sltd :
  sum+=i

result = sum/len(data)-1

standardDeviation = math.sqrt(result)

print("The standar deviation is ", standardDeviation)

print("The standar deviation is ", statistics.stdev(data))
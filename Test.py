# breast-cancer-wisconsin.data
import csv
import math
import random
import sys
#Get data points from file
trData = []
tstData = []
distances = []
k = 0

def getData(fileName, matrix):
	#error catch
	try:
		file = open(fileName, "r")
		file.close()
	except:
		print("Could not open file!")
		sys.exit(0)

	file = open(fileName, "r")
	for line in file:
		#parse data into lists
		point = line.split(",")
		#remove \n
		for x in point:
			if '\n' in x:
				point.append(x[:-1])
				point.remove(x)
		matrix.append(point)
	file.close()
	return matrix

#getting distance from list
def getDistance(list):
	return list[0]

#Finds nearest neighbor for each point
def getNearestNeighbor():
	#getting the distance of each point
	#Put distances in list with classifications, then put these in a larger list
	#Sort 
	for tstPoint in tstData:
		distances = []
		bCounter = 0
		mCounter = 0

		for trPoint in trData:
			#if a question mark is present, discard that distance calc
			distance1 = 0
			distance2 = 0
			distance3 = 0
			distance4 = 0
			distance5 = 0
			distance6 = 0
			distance7 = 0
			distance8 = 0
			distance9 = 0

			if tstPoint[1] != '?' and trPoint[1] != '?':
				distance1 = ((int(tstPoint[1]))-(int(trPoint[1])))**2
			if tstPoint[2] != '?' and trPoint[2] != '?':	
				distance2 = ((int(tstPoint[2]))-(int(trPoint[2])))**2
			if tstPoint[3] != '?' and trPoint[3] != '?':
				distance3 = ((int(tstPoint[3]))-(int(trPoint[3])))**2
			if tstPoint[4] != '?' and trPoint[4] != '?':
				distance4 = ((int(tstPoint[4]))-(int(trPoint[4])))**2
			if tstPoint[5] != '?' and trPoint[5] != '?':
				distance5 = ((int(tstPoint[5]))-(int(trPoint[5])))**2
			if tstPoint[6] != '?' and trPoint[6] != '?':
				distance6 = ((int(tstPoint[6]))-(int(trPoint[6])))**2
			if tstPoint[7] != '?' and trPoint[7] != '?':
				distance7 = ((int(tstPoint[7]))-(int(trPoint[7])))**2
			if tstPoint[8] != '?' and trPoint[8] != '?':
				distance8 = ((int(tstPoint[8]))-(int(trPoint[8])))**2
			if tstPoint[9] != '?' and trPoint[9] != '?':
				distance9 = ((int(tstPoint[9]))-(int(trPoint[9])))**2
			distance = math.sqrt(distance1+distance2+distance3+distance4+distance5+distance6+distance7+distance8+distance9)
			#storing distances and classifications
			pair = [distance, trPoint[10]]
			distances.append(pair)

		#sort distances and limit to k distances
		distances.sort(key=getDistance)
		kdistances = distances[:k]
		for line in kdistances:
			#benign
			if (int(line[1])) == 2:
				bCounter = bCounter+1
			#malignant
			if (int(line[1])) == 4:
				mCounter = mCounter+1
		if bCounter > mCounter:
			tstPoint[10] = 2
		if mCounter > bCounter:
			tstPoint[10] = 4
		if bCounter == mCounter:
			num = random.randint(1,2)
			if num == 1:
				tstPoint[10] = 2
			if num == 2:
				tstPoint[10] = 4

	return tstData


#Add points to new set
def newFile():
	path = input("Please enter a file path to write to: ")
	try:
		file = open(path, "a")
		file.close()
	except:
		print("Could not open file!")
		sys.exit(0)

	f = open(path, "a")
	for point in tstData:
		f.write("\n")
		for coordinate in point:
				f.write((str(coordinate)))
				if coordinate != point[10]:
					f.write(",")
	f.close()
		
#main
def main():
	getData("breast-cancer-wisconsin.data", trData)
	name = input("Please enter your file name: ")
	k = input("Please enter your k value: ")
	try:
		int(k)
	except:
		print("That's not a valid integer!")
		sys.exit(0)
	getData(name, tstData)
	getNearestNeighbor()
	newFile()

main()

import random
import numpy as np
import timeit

class BogoMap(): 

	def __init__(self): 
		self.data = []
		self.index = 0
	
	def indexOf(self, key):
		if not self.data:
			return -1

		r = len(self.data)-1
		l = 0
		while l < r: 
			m = (l+r)/2
			if self.data[m][0] < key:
				l = m+1
			else:
				r = m

		if self.data[l][0] == key:
			return l
		else: 
			return -1 #not in dictionary
	
	def __getitem__(self, key):
		i = self.indexOf(key)
		if i != -1:
			return self.data[i]

		return None

	def __setitem__(self, key, value):
		i = self.indexOf(key)
		if i != -1: 
			self.data[i] = (key, value)
		else:
			self.data.append((key,value))
			self.__bogoSort()

	def __isSorted(self):
		return all(self.data[i][0] <= self.data[i+1][0] for i in xrange(len(self.data)-1)) 

	def __bogoSort(self):
		while not self.__isSorted():
			#random.shuffle(self.data)
			np.random.shuffle(self.data)
	def __str__(self): 
		return str(self.data)

	def __len__(self):
		return len(self.data)

	def __iter__(self): 
		return self

	def next(self):
		if self.index >= len(self.data): 
			raise StopIteration
		else: 
			self.index += 1
			return self.data[self.index - 1]

time_arr = []
for i in range(10):
	startTime = timeit.default_timer()
	testMap = BogoMap()
	testMap[0] = 2
	testMap[1] = 3
	testMap[-3] = 5

	#print testMap.data

	testMap[-7] = 5
	testMap[-8] = 2
	testMap[5] = 4
	testMap[10] = 10
	testMap[0] = 100000
	testMap[11] = 4
	testMap[12] = 99

	testMap[-10] = 98
	#testMap[-15] = 9

	#print testMap.data
	print testMap
	endTime = timeit.default_timer()
	time_arr.append(endTime-startTime)

	# for i in testMap: 
	# 	print i
print time_arr
print sum(time_arr)/len(time_arr)


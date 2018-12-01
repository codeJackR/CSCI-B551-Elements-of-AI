import numpy as np
import sys

def throwOne(remaining1, remaining2):
	if(remaining1==remaining2):
		return remaining1+remaining2+(21-remaining1+25)/6
	return 3.5+remaining1+remaining2

def throwTwo(remaining):
	return remaining+((21*12)-2*remaining+25)/36

def whichToThrowAgain(initialOutput):
	maxExpected = sum(initialOutput)
	throw = np.zeros(3)
	if np.size(np.unique(initialOutput))==1:
		maxExpected = 25
	#rotate all 3
	if(maxExpected<10.5):
		maxExpected = 10.5
		throw = np.ones(3)
	for i in range(3):
		index1 = -2+i
		index2 = -1+i
		expectedValue = throwOne(initialOutput[index1], initialOutput[index2])
		if(expectedValue>maxExpected):
			maxExpected = expectedValue
			throw = np.zeros(3)
			throw[i]=1
			print()
		expectedValue = throwTwo(initialOutput[i])
		if(expectedValue>maxExpected):
			maxExpected = expectedValue
			throw = np.zeros(3)
			throw[index1]=1
			throw[index2]=1
	print(throw)

inputs = np.zeros(3)
for i in range(3):
	inputs[i] = float(sys.argv[i+1])

whichToThrowAgain(inputs)
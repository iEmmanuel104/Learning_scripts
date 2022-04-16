#practicing how to use the Big O notation and calculate time complexities, (iteration approach)
def FindBiggestNumber(sampleArray):           #function that find biggest number
	biggestNum = sampleArray[0]               # assign the first array value to variable, complexity O(1)
	for i in range(1,len(sampleArray)):       #loop through from the second array value 2d end, O(n)
		if sampleArray[index] > biggestNum:   #complexity O(1)
			biggestNum = sampleArray[index]   # ''
	print (biggestNum)                        # ''
'''
computing the iverall time complexity we see that 
code block line  5&6 O(1) + O(1) = O(1)
ADDING TO BLOCK 4
O(n) + O(1) = o(n)
NOW adding lines 2 and 7 to d result
O(1) + O(n) + O(1) = O(n)
THEREFORE  the time complexity is O(n)
'''

			#solving using recursive call approach
def FindMaxNum(samplearr, n):     			# M(n)
	if n == 1:								# base case for recursive call O(1)
		return samplearr[0]					#return first element of array, O(1) 
	return max(samplearr[n-1], FindMaxNum(samplearr, n-1)) 
	#return max of the current elemnet value with the value returnd from d same fuvtion with n-1 

'''
if a function calls iiself recursively in a function we assume that it takes and M(n)
the constant TC = O(1)
M(n) = O(1) + M(n-1) #if n=1, we have M(1) = O(1) 
substitute with a
M(n) = 1 + M(n-a)
Therefor for every value of a in d recursive call u get d time complexity eqn for that recursive call
for a = n-1
M(n) = n-1 + M(n-(n-1))
therefore we have O(n) as the time complexity 
'''

 			#MEASURING RECURSIVE ALGORITHM THAT MAKE MULTIPLE CALLS
def f(n):
	if n<=1:
		return 1
	return f(n-1) + f(n-1)
	'''
The nodes increases with every call
therefore the eqn is 2^n - 1 = O(2^n)'''

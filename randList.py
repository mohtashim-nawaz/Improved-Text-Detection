import numpy as np
import random

def getRandomList(num, start, end, step=1):
	if(num > end-start+1):
		return []
	lst=[]
	i=1
	while(i<=num):
		temp = random.randrange(start=start, stop=end, step=step)
		lst.append(temp)
		i = i+1

	return lst


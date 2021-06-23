# importing libraries
from scipy import random
import numpy as np

#setting the boundary of the integral
a = 0
b = 1 
N = 1000

#array of zeros of length N
ar = np.zeros(N)

for i in range (len(ar)):
	ar[i] = random.uniform(a,b)

# variable to store sum of the functions of different values of x
integral = 0.0

# function to calculate the sin of a particular value of x
def f(x):
	return np.sin(x)

#iterates and sums up values of different functions
for i in ar:
	integral += f(i)

#Monte Carlo estimator
Ihat = (b-a)/float(N)*integral

# prints the solution
print ("The value calculated by monte carlo integration is {}.".format(Ihat))
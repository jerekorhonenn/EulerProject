#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
import math

def compute():
	#Wanted number
	n = 600851475143
	tmp = 1
	while tmp < n:
		#tmp must be not pair as prime factors are
		tmp += 2
		#divide n by tmp 
		while n % tmp == 0:
			n /= tmp
	return tmp

if __name__ == "__main__":
	print(compute())
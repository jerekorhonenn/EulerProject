#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def compute():
	ans = 0
	x = 1  # Represents the current Fibonacci number being processed
	y = 2  # Represents the next Fibonacci number in the sequence
	while x <= 4000000:
		if x % 2 == 0:
			ans += x
		x, y = y, x + y
	return str(ans)

print(compute())
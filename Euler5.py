#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import time

def smallest(n):
    for i in range(1,1000000000):
        for j in range(1,n+1):
            if(i%j!=0):
                break
            if(j==n):
                return i
            
        

if __name__ == "__main__":
    #time the function in seconds
    start = time.time()
    print(smallest(10))
    print("Time: ", time.time()-start)
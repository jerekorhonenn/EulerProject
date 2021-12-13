#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def reversedt(n):
    r = 0
    while n > 0:
        r *= 10
        r += n % 10
        n /= 10
    return r
reversedt(9009)
suurin=0
suurinx=0
suuriny=0
for x in reversed(range(1000)):
    for y in reversed(range(1000)):
        palindrome=x*y
        pali=str(palindrome)
        if (pali[::-1]==pali):
            if(suurin<palindrome):
                suurin=palindrome
                suurinx=x
                suuriny=y
            
print(suurin,suurinx,suuriny)
x=12345
a=int(str(x)[::-1])
print(a)
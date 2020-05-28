import math
#Find the largest prime factor of the number 600851474143.
def getFactor(number):
    factors = []
    for potentialFactor in range(1, int(math.sqrt(number))+1):
        if number % potentialFactor == 0:
            factors.append(potentialFactor)
            factors.append(number/potentialFactor)
            #or else primes only have 1 factor while composite numbers have 2 or more factors
    return factors

def isPrime(number):
    return len(getFactor(number)) == 2

allFactors = getFactor(600851475143)
largestPrimeFactor = 0
for factor in allFactors:
    if isPrime(factor) and factor > largestPrimeFactor:
        largestPrimeFactor = factor

print(largestPrimeFactor)

def f(n):
    factors = []
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            x = True
            for j in range(2, int(math.sqrt(i))+1):
                if i%j == 0:
                    x = False
                    break
            if x:
                factors.append(i)
    return max(factors)

print(f(600851475143))
    

        
            
            
            

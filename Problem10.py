#Problem 10 - Summation of primes
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    
from NumberTests import isPrime
    
def sumofPrimes(summation):
    total = 0

    for n in range(2, summation):
        if isPrime(n):
            total += n
    return total

def main():
    result = sumofPrimes(2000000)
    print(result)

if __name__ == "__main__":
    main()







#Find the sum of all the primes below two million.


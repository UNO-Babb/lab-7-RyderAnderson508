#Problem 7 - 10001st prime
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

def main():
    
    def isPrime(n):
        if n < 2: 
            return False
        if n ==2:
            return True 
        if n % 2== 0:
            return False 

        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    def numPrime(n):
        numberofPrimes = 0
        prime = 1
        while numberofPrimes < n:
            prime += 1
            if isPrime(prime):
                numberofPrimes += 1
        return prime

    print(numPrime(10001))
   

  

  
   #What is the 10001st prime number?
    



  
  

if __name__ == '__main__':
  main()


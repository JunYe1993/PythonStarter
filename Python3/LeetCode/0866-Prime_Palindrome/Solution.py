class Solution:
    primes = [2]
    def primePalindrome(self, N: int) -> int:
        
        # Find palindrome number first, then check it is a prime number.
        
        # So elimiate special case 2 and 11.
        # 2's for N < 3 case, 11's explantion is below.
        if N < 3: return 2
        elif 7 < N <= 11: return 11

        # Record the number of digits.
        num, digitLen = N, 0
        while num > 0:
            num = num // 10
            digitLen += 1

        # If palindrome number is tens digit, thousands digit...(the number of digits is even),
        # it would be divided by 11. It will be non-prime number except for 11 itself.
        if digitLen % 2 == 0:
            return self.primePalindrome(10**(digitLen))
        else:
            halfDigitLen = digitLen//2
            # All one digit number is palindrome number
            if halfDigitLen == 0:
                for num in range(N, 10):
                    if self.isPrime(num):
                        return num
            # If number of digits is bigger than one.
            # Split the palindrome number into three part, left, middle, right
            # We need to find palindrome number in ascending way.
            # So first decide left side number then middle number.(right number don't matter if it's palindrome number)
            else:
                # first digit of left side number has to be 1, otherwise it would not be the same number of digits.
                # If 7 digits number => left side number is 100 ~ 999
                leftSideNum = 10**(halfDigitLen-1)
                while leftSideNum < 10**halfDigitLen:

                    # Caculate right side number
                    rightSideNum = 0
                    for digit in range(halfDigitLen):
                        rightSideNum += (leftSideNum%(10**(digit+1))//(10**digit))*(10**(halfDigitLen-digit-1))
                    
                    # middle number is 0 ~ 9
                    for middleNum in range(10):
                        num = rightSideNum + leftSideNum*(10**(halfDigitLen+1)) + middleNum*(10**halfDigitLen)
                        if num >= N:
                            if self.isPrime(num): 
                                return num

                    # If didn't find prime number than go next
                    # The while statement just to elimiate last digit is multiple of 2 or 5
                    # which definitely not the prime number.
                    leftSideNum += 1
                    firstNum = leftSideNum//(10**(halfDigitLen-1))
                    while firstNum % 2 == 0 or firstNum % 5 == 0:
                        leftSideNum += 10**(halfDigitLen-1)
                        firstNum = leftSideNum//(10**(halfDigitLen-1))

                # If it need to more digits number to find prime number,
                # then add 2 more digit to the number. 999 -> 10000 (3->5)
                return self.primePalindrome(10**(digitLen+1))

    def isPrime(self, x: int) -> bool:
        notEnoughPrime = True
        for prime in self.primes:
            if prime*prime > x: 
                notEnoughPrime = False
                break
            if x % prime == 0: 
                return False
            
        if notEnoughPrime:
            num = self.primes[-1] + 1
            while num*num <= x:
                if self.isPrime(num):
                    self.primes.append(num)
                num += 1
            for prime in self.primes:
                if x % prime == 0: 
                    return False
        return True

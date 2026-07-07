class Solution:
    def sumAndMultiply(self, n: int) -> int:
        rem = 0
        sum = 0

        while n !=0:
            mod = n%10
            if mod >0:

                rem = rem*10 + mod
                sum = sum+mod
            n = n//10

        x = 0
        while rem>0:
            x =x*10 + rem%10
            rem  //=10
        return x*sum
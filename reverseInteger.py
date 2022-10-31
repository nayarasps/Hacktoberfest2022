class Solution:
    def reverse(self, x: int) -> int:

        absolute_x = str(abs(x))
        
        reversed_x = int(absolute_x[::-1])
        
        if (reversed_x >= 2**31-1 or reversed_x <= -2**31):
            return 0
        
        if (x < 0) :
            return(reversed_x * -1)
        return reversed_x
        

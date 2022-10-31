class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        number = 0

        for i in range(len(s)-1):
            if (dic[s[i]] < dic[s[i+1]]):
                number -= dic[s[i]]
            else:
                number += dic[s[i]]
        number += dic[s[-1]]
        
        return number

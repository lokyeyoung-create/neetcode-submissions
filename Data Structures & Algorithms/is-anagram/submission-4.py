class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        countS = defaultdict(int)
        countT = defaultdict(int)
        for letter in s:
            countS[letter] += 1
        for letter in t:
            countT[letter] += 1

        if countS == countT:
            return True
        else:
            return False
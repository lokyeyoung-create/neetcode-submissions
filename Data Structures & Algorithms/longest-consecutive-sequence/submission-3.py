class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen = set(nums)
        res = 0 

        for num in nums:
            curMax = 0
            if num - 1 not in seen:
                i = 0
                while num + i in seen:
                    curMax += 1
                    i += 1 
                if curMax > res:
                    res = curMax
            else:
                continue
        
        return res
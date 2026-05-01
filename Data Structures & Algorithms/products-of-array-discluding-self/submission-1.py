class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # nums = [1,2,4,6]
        # prefix = [1, 1, 2, 8]
        # suffix = [48, 24, 6, 1]
        output = []
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        for i in range(len(nums)):
            output.append(prefix[i] * suffix[i])
        return output


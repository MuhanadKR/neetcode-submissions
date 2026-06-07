class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            left = nums[:i]
            right = nums[i+1:]
            prod = 1
            for x in left+right:
                prod*= x
            res.append(prod)

        return res
            
        
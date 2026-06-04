class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        for i in range(len(nums)):
            for j in range(i+1):
                if i!=j and nums[i] + nums[j] == target:
                    indices.append(j)
                    indices.append(i)

        return indices

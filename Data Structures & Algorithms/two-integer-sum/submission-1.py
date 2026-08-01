class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i , num in enumerate(nums):
            value = target-num
            if value in hash:
                return [hash[value], i]
            else:
                hash[num] = i
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = {}

        for i, n in enumerate(nums):
            diff = target - n 
            if diff in map:
                return [map[diff], i]
            map[n] = i

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, num in enumerate(nums):
            difference = target - num
            if difference in seen:
                return [i, seen[difference]]
            seen[num] = i

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        seen = {}  # {val: index}

        for i, val in enumerate(nums):

            compliment = target - val

            if compliment in seen:
                return [seen[compliment], i]

            seen[val] = i

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        ans = []

        for i in range(len(nums)):

            count = 0

            # loop
            for j in range(len(nums)):

                if nums[i] > nums[j]:
                    count += 1

            ans.append(count)

        return ans

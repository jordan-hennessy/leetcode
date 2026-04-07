class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        test = []
        ans = []

        for i in nums:

            if i in test:
                ans.append(i)
            else:
                test.append(i)

        counter = 1

        for i in range(len(nums)):
            if counter not in nums:
                ans.append(counter)
                break

            counter += 1

        return ans

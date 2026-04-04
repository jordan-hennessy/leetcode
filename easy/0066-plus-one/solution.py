class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        result = []

        total = 0

        for i in digits:

            total += i

        total += 1

        ################

        length = len(str(total))

        # 122 -> 3

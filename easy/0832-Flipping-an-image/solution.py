class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        temp = []
        result = []

        for n in image:
            n.reverse()
            temp.append(n)

        for row in temp:
            inverted = []
            for num in row:
                if num == 1:
                    inverted.append(0)
                else:
                    inverted.append(1)
            result.append(inverted)

        return result

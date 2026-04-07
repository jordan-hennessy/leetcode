class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        stack = []

        setTarget = set(target)

        for i in range(1, target[-1]):

            if i in setTarget:
                stack.append("Push")
            else:
                stack.append("Push")
                stack.append("Pop")

        stack.append("Push")

        return stack

class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Turn into a str
        x = str(x)
        temp = x[::-1]

        return x == temp

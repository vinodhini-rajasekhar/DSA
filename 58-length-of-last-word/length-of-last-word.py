class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = [i for i in s.split(" ") if i]
        return len(result[-1])
        
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack.__contains__(needle):
            result = haystack.find(needle)
            return result
        else:
            return -1
        
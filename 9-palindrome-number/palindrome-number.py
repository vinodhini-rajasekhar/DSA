class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original_num = x
        rev_num = 0

        while x > 0:
            last_num = x % 10
            rev_num = (rev_num * 10) + last_num
            x = x // 10 

        return original_num == rev_num


            
        
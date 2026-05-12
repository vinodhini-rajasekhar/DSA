class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            var3 = nums.index(target)
            return var3

        else:
            nums.append(target)
            nums.sort()
            var2 = nums.index(target)
            return var2


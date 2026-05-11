class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = max(set(nums), key=nums.count)
        return freq

        
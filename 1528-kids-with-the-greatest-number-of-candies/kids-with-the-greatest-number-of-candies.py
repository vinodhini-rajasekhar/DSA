class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        high_val = max(candies)
        res = []
        for i in candies:
            if i+extraCandies >= high_val:
                res.append(True)
            else:
                res.append(False)
        return res


        
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            temp = str(i)
            if len(temp) % 2 == 0:
                count += 1
        return count

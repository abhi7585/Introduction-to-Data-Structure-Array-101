class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = max = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                count = 0
            if count > max:
                max = count
        return max

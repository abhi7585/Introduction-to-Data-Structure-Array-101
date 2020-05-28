class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        sqArr = [i**2 for i in A]
        return sorted(sqArr)

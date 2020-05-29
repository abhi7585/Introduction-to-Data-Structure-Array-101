class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        increasing = True
        if len(A) < 3 or A[0] >= A[1]:
            return False
        for i in range(len(A) - 1):
            if A[i+1] <= A[i] and increasing:
                increasing = False
            if not increasing and A[i+1] >= A[i]:
                return False
        return True if not increasing else False

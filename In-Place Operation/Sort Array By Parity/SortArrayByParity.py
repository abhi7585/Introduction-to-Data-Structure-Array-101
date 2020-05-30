class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i = 0
        for j, n in enumerate(A):
            if not n % 2:
                A[i], A[j] = A[j], A[i]
                i += 1
        return A

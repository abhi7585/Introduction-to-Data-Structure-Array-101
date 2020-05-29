class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = -1
        for i in range(n):
            nums1[j] = nums2[i]
            j -= 1
        nums1.sort()

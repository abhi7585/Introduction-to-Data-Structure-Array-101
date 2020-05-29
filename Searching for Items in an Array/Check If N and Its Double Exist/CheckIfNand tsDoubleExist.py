class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(0, len(arr)):
            if arr[i] != 0:
                if 2*arr[i] in arr:
                    return True
            else:
                if arr == [0, 0]:
                    return True
        return False

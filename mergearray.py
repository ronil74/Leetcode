class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = len(nums1)-m

        for i in range(l):
            nums1.remove(0)

        for i in nums2:
            nums1.append(i)
            
        nums1.sort()
        

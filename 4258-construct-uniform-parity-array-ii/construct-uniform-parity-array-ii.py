class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min = nums1[0]
        hasOdd = False
        for v in nums1:
            if v < min:
                min = v
            if v & 1:
                hasOdd = True

        if min & 1:
            return True
        return not hasOdd



"""
#solo attempt#1
#class Solution(object):
#    def uniformArray(self, nums1, nums2):
#        for i in range(len(nums1)):
#           if nums2[i] == nums1[i]:
#               return bool true

#semi-solo attempt (ai-logic)

class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        min_val = min(nums1)

        if min_val % 2 != 0:
            return True
        else:
            return False

#ai help attempt

class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        min_val = min(nums1)

        if min_val % 2 != 0:
            return True
        
        return all(x % 2 == 0 for x in nums1)
"""
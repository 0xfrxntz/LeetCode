class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return[i,j]
        return[]

  


        #Logic
        #1: loop through each element in the array
        #2: for each element, loop through subsequent arary 
        #3: check if i + j = target
        #4: if condition is met return their index
        
        
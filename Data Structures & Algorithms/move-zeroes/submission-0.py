class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # the idea is to move zeroes all to the left.
        # two pointer. track position with l
        l = 0
        for r in range(len(nums)): # iterate through array with r pointer
            if nums[r] != 0: # if r is non-zero
                nums[l] = nums[r] # copy to nums[l]
                l += 1 #increment
        
        while l < len(nums):
            nums[l] = 0 # fill positions from l to end with 0
            l += 1
        
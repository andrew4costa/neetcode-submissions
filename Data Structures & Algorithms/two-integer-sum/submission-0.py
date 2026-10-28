class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for index, num in enumerate(nums):
            complement = target - num
            
            # If the complement exists, we found our pair
            if complement in seen:
                return [seen[complement], index]
                
            # Otherwise, record the current number and its index
            seen[num] = index
            
        return [] 

        
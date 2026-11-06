class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        return indices of 2 nums ([index1, index2]) = target 
        index1 < index2
        index1 != index2
        o(1) space
        """
        """
        # brute force
        # start loop at index 0
        for i in range(len(numbers)):
            # start loop at index 1, ensure not reusing numbers
            for j in range(i+1, len(numbers)):
                # if numbers sum to target
                if numbers[i] + numbers[j] == target:
                    # output 1-indexed indices
                    return [i + 1, j + 1]
        
        return []
        """
        """
        # two pointer
        l,r = 0, len(numbers) - 1
        while l < r:
            csum = numbers[l] + numbers[r]
            if csum > target:
                r -= 1
            elif csum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        
        return []
        """
        #hashmap
        mp = defaultdict(int)
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if mp[tmp]:
                return [mp[tmp], i+1]
            mp[numbers[i]] = i+1
        return []


            
        
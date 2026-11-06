from collections import Counter

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            # skip non-alphanumeric
            while l < r and not s[l].isalnum():
                l += 1
            # skip non-alphanumeric
            while r > l and not s[r].isalnum():
                r -= 1
            # if vals dont match, not palindrome    
            if s[l].lower() != s[r].lower():
                return False
            # move pointers as long as l < r   
            l, r = l+1, r-1
        return True
        
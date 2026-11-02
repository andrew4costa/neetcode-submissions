from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        anagram are two words with same num of characters
        so we need to check length of one as first pass, if it 
        doesnt match, return False
        if they do match, then calculate count of each char in word
        """
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)
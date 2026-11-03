class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chars = defaultdict(list)
        for s in strs:
            sorted_chars = "".join(sorted(s))
            chars[sorted_chars].append(s)
        return list(chars.values())
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chars = {}
        for word in strs:
            key = "".join(sorted(word))

            if key not in chars:
                chars[key] = []
            chars[key].append(word)
        return list(chars.values())
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splitlist = s.split()
        final = len(splitlist[-1])
        return final
    
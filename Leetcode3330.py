class Solution:
    def possibleStringCount(self, word: str) -> int:
        prev = '-'
        count = 0
        for i in range(len(word)):
            if word[i] == prev:
                count += 1
            prev = word[i]
        return count + 1
    
sol = Solution()
sol.possibleStringCount("abbcccc")
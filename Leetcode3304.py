class Solution:
    def kthCharacter(self, k: int) -> str:
        s = "a"
        while len(s) < k:
            new_s = ""
            for i in range(len(s)):
                new_s += chr(((ord(s[i]) - ord('a') + 1) % 26) + ord('a'))
            s = s + new_s
        return s[k-1]
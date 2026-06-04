class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new_s = [""]*len(s)
        new_t = [""]*len(t)
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                new_s.append(s[i])
                new_t.append(t[i])
            new_s.sort()
            new_t.sort()
            if new_s == new_t:
                return True
            else:
                return False

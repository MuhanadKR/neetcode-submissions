class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_s = ""
        longest_sub = 0
        for i in range(len(s)):
            while s[i] in current_s:
                current_s = current_s[1:]
            current_s+=s[i]

            longest_sub = max(longest_sub,len(current_s))
        return longest_sub

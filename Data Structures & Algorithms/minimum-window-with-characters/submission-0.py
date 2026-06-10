class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        # Step 1: Count characters in t
        t_count = {}
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1

        # Step 2: Initialize variables
        window = {}
        left = 0
        have = 0
        need = len(t_count)

        res = [-1, -1]
        res_len = float("inf")

        # Step 3: Expand window
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            # Step 4: Check if this char satisfies requirement
            if char in t_count and window[char] == t_count[char]:
                have += 1

            # Step 5: Shrink window when valid
            while have == need:
                
                # Step 6: Update result
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # Step 7: Remove from left
                window[s[left]] -= 1
                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    have -= 1

                left += 1

        # Step 8: Return result
        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""
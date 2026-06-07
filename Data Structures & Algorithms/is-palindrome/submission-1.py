class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        s = s.lower()
        s = s.replace(" ","")
        for i in s:
            if i not in alphabet and i not in nums:
                s = s.replace(i,"")
        if s == s[::-1]:
            return True
        else:
            return False
            
        
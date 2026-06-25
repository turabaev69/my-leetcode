class Solution(object):
    def isPalindrome(self, x):
        original = x
        reversed_num = 0
        
        while x > 0:
            last = x % 10
       
            reversed_num = reversed_num * 10 + last
            x = x // 10
      
        
        return original == reversed_num
        
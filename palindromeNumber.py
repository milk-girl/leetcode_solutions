def isPalindrome(x):
 if x >= 0:
     z = x
     y = 0
     while(z != 0):
         y = (y * 10)+ (z % 10) 
         z = z // 10
     return y == x
 return False

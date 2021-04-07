class Solution(object):
   def numberOfDays(self, y, m):
      leap = 0
      if y% 400 == 0:
         leap = 1
      elif y % 100 == 0:
         leap = 0
      elif y% 4 == 0:
         leap = 1
      if m==2:
         return 28 + leap
      list = [1,3,5,7,8,10,12]
      if m in list:
         return 31
      return 30
ob1 = Solution()

year = int(input("Introduceti anul: "))
month = int(input("Introduceti luna: "))

print(ob1.numberOfDays(year, month))
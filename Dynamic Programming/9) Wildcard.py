""" Wildcard Matching Pattern:
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

~> '?' Matches any single character.
~> '*' Matches any sequence of characters (including the empty sequence).
~> The matching should cover the entire input string (not partial).

Check if we can match pattern with string by implimenting wildcard pattern according to given rules.
"""

class Solution:
   # Match pattern with s one by one while checking
   def recur(self,s:str,p:str,i:int,j:int,dp) -> bool:
      if i<0 and j<0:
         return True
      if j<0:
         return False
   # Edge case: if entire pattern consist of *, then this fails
      if i<0:
         return all( p[k] == "*" for k in range(j+1) )
      
      #  Memoization
      if(dp[i][j] != -1):
         return dp[i][j]
      
   #   Case: character match, check furthur
      if s[i] == p[j]:
         dp[i][j] = self.recur(s,p,i-1,j-1,dp)
      elif p[j] == "?": # ? fill to match any character
         dp[i][j] = self.recur(s,p,i-1,j-1,dp)
   #   Case: character encounter *, just look at all possible fills
      elif p[j] == "*":
         # replace * with empty string
         fillempty = self.recur(s,p,i,j-1,dp)
         # replace * with another start and matching charter
         fillstarcharacter = self.recur(s,p,i-1,j,dp)
   # replace * with matching char and other case:-> covered in first two cases recursive calls
         dp[i][j] = fillempty or fillstarcharacter
   #   Case: character dont match, return false and end code
      else:
         dp[i][j] = False
      
      return dp[i][j]

   def isMatch(self, s: str, p: str) -> bool:
      dp = [[-1]*(len(p)+1) for _ in range(len(s)+1)]
      return self.recur(s,p,len(s)-1,len(p)-1,dp)

   # To convert this code to tabulation-> we need to use 1 based indexing
   def Tabulation(self,s:str,p:str)->bool:
      dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
      
      # Initialise
      dp[0][0] = True
      for j in range(1,1+len(p)):
         if p[j-1] == '*':
            dp[0][j] = dp[0][j-1]
      
      # Fill the DP table
      for i in range(1,1+len(s)):
         for j in range(1,1+len(p)):
            if s[i-1] == p[j-1] or p[j-1] == '?':
               dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
               dp[i][j] = dp[i-1][j] or dp[i][j-1]
            else:
               dp[i][j] = False
      
      return dp[len(s)][len(p)]
      
   # Space optimization
   def Optimal(self,s:str,p:str)->bool:
      curr = [False for _ in range(len(p)+1)]
      prev = [False for _ in range(len(p)+1)]
      
      # Initialise
      prev[0] = True
      for j in range(1,1+len(p)):
         if p[j-1] == '*':
            prev[j] = prev[j-1]
      
      # Fill the DP table
      for i in range(1,1+len(s)):
         curr[0] = False # Non-empty string can't match empty pattern
         for j in range(1,1+len(p)):
            if s[i-1] == p[j-1] or p[j-1] == '?':
               curr[j] = prev[j-1]
            elif p[j-1] == '*':
               curr[j] = prev[j] or curr[j-1]
            else:
               curr[j] = False
         prev = curr
      
      return curr[len(p)]
      

if __name__ == "__main__":
   sol = Solution()
   s = "adceb"
   p = "*a*b"
   
   S = "bbbababbabbbbabbbbaabaaabbbbabbbababbbbababaabbbab"
   P = "a******b*"
   ans = sol.isMatch(s,p)
   Ans = sol.Tabulation(S,P)
   Answer = sol.Optimal(s,p)
   
   print(ans,Ans,Answer)
   

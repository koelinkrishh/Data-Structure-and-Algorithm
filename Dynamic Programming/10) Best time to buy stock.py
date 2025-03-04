# Given an array prices for sotck at ith day, find maximum profit you can achieve
import sys
import math

''' 1) Given an integer array of price for a stock at ith day. 
   Find maximum profit if you can only buy stock once '''
def maxprofit(prices) -> int:
   Min = sys.maxsize
   profit = 0
   for i in prices:
      Min = min(Min,i)
      profit = max(profit,i-Min)
   
   return profit

# Optimal
def maxProfit(prices) -> int:
   Minima = sys.maxsize
   profit = 0
   for i in prices:
      if(i<Minima):
         Minima = i
      else:
         profit = max(profit,i-Minima)
   
   return profit


''' 2) Given prices of a stock, find maximum profit given you can buy stock multiple times '''
def recursion(index,prices,state,dp):
   # state can be buy/sell -> reference to Next move
   if(index==len(prices)):
      return 0
   
   profit = 0 # create a semi-local variable which is carried on recursive call
   
   if(dp[index][state] != -1):
      dp[index][state]
   
   if not state: # buyng
      buy = -prices[index] + recursion(index+1,prices,1,dp)
      SkipBuying = recursion(index+1,prices,0,dp)
      profit += max(buy,SkipBuying)
   elif state:  # selling
      sell = prices[index] + recursion(index+1,prices,0,dp)
      SkipSelling = recursion(index+1,prices,1,dp)
      profit += max(sell,SkipSelling)
   
   return profit
def MaxProfit(prices:list) -> int:
   dp = [[-1]*2] *len(prices)
   return recursion(0,prices,0,dp)


# Optimal logic: Greedy Approach-> We can buy and sell on same day which makes no difference to result,
# so we can setup buying at every last day and selling on any profit
def maximumprofit(prices:list) ->int:
   result=0
   prev = prices[0]
   
   for i in range(1,len(prices)):
      if prev<prices[i]:
         result += prices[i] - prev
      prev = prices[i]

   return result


''' 3) Given prices of a stock, find maximum profit given we can make two transistions. '''
def Twobuyprofit(prices)->int:
   firstbuy = float('inf')
   secondbuy = float('-inf')
   firstsell,secondsell = 0,0
   
   for price in prices:
      # Maximize the profit if we buy the first stock
      firstbuy = min(firstbuy,price)
      # Maximize the profit if we sell the first stock
      firstsell = max(firstsell,-firstbuy + price)
      # Maximize the profit if we buy the second stock after the first is sold
      secondbuy = max(secondbuy,firstsell - price)
      # Maximize the profit if we sell the second stock
      secondsell = max(secondsell,secondbuy + price)
   
   return secondsell
# OR
def twotransistionProfit(prices:list) ->int:
   n = len(prices)
   dp = [[0]*4 for _ in range(n + 1)]
   
   profit = 0
   
   for index in range(n-1,-1,-1):
      for state in range(4):
      # even-buy and odd-sell
         transistion = state % 2
         if transistion == 0: # buyng
            buy = -prices[index] + dp[index + 1][state + 1]
            SkipBuying = dp[index+1][state]
            dp[index][state] = max(buy,SkipBuying)
         elif transistion == 1: # selling
            sell = prices[index] + (dp[index + 1][state + 1] if state+1<4 else 0)
            SkipSelling = dp[index+1][state]
            dp[index][state] = max(sell,SkipSelling)
   
   return dp[0][0]
   
# State 0 represents the state of transistion

# Space optimization
def TwotransistionProfit(prices:list) ->int:
   n = len(prices)
   curr = [0]*4
   Next = [0]*4
   
   profit = 0
   
   for index in range(n-1,-1,-1):
      for state in range(4):
      # even-buy and odd-sell
         transistion = state % 2
         if transistion == 0: # buyng
            buy = -prices[index] + Next[state + 1]
            SkipBuying = Next[state]
            curr[state] = max(buy,SkipBuying)
         elif transistion == 1: # selling
            sell = prices[index] + (Next[state + 1] if state+1<4 else 0)
            SkipSelling = Next[state]
            curr[state] = max(sell,SkipSelling)
         curr = Next
   
   return curr[0]
   

''' 4) Given prices of a stock, find maximum profit given we can make k transistions. '''
def KtransistionProfit(prices:list,trans) ->int:
   n = len(prices)
   curr = [0]*(2*trans)
   Next = [0]*(2*trans)
   
   profit = 0
   
   for index in range(n-1,-1,-1):
      for state in range(2*trans):
      # even-buy and odd-sell
         transistion = state % 2
         if transistion == 0: # buyng
            buy = -prices[index] + Next[state + 1]
            SkipBuying = Next[state]
            curr[state] = max(buy,SkipBuying)
         elif transistion == 1: # selling
            sell = prices[index] + (Next[state + 1] if state+1<(2*trans) else 0)
            SkipSelling = Next[state]
            curr[state] = max(sell,SkipSelling)
         curr = Next
   
   return curr[0]

# Optimal code:
def KthoptimalProfit(k: int, prices: list[int]) -> int:
   # allowed transistion > possible transition -> problem reduce to Q.2)
   if k >= len(prices) // 2:
      sell = 0
      hold = -math.inf
      
      for price in prices:
         sell = max(sell, hold + price)
         hold = max(hold, sell - price)
      return sell
   else:
      sell = [0] * (k + 1)
      hold = [-math.inf] * (k + 1)

      for price in prices:
         for i in range(k, 0, -1):
            sell[i] = max(sell[i], hold[i] + price)
            hold[i] = max(hold[i], sell[i - 1] - price)

      return sell[k]

# OR more simple
def Kmaxprofit(prices,k) -> int:
   cost = [math.inf]*(k+1)
   profit = [0]*(k+1)
   
   for p in prices:
      for trans in range(1,k+1):
         cost[k] = min(cost[k],p - profit[k-1])
         profit[k] = max(profit[k],p - cost[k])
   
   return profit[-1]


''' 5) Given prices of a stock, find maximum profit given we can make any number of transistions 
but you have one day cooldown i.e., if you sell todaym you cant buy on today and the next day '''
def Recursion(index,prices,state,dp):
   # state can be buy/sell -> reference to Next move
   if(index>=len(prices)):
      return 0
   
   if(dp[index][state] != -1):
      dp[index][state]
      
   profit = 0 # create a semi-local variable which is carried on recursive call
   
   if not state: # buyng
      buy = -prices[index] + Recursion(index+1,prices,1,dp)
      SkipBuying = Recursion(index+1,prices,0,dp)
      profit += max(buy,SkipBuying)
   elif state:  # selling
      sell = prices[index] + Recursion(index+2,prices,0,dp)
      SkipSelling = Recursion(index+1,prices,1,dp)
      profit += max(sell,SkipSelling)
   
   dp[index][state] = profit
   return dp[index][state]
def NetProfitwithcooldown(prices:list)->int:
   dp = [[-1]*2 for _ in range(len(prices) + 1)]
   return Recursion(0,prices,0,dp)

def Profitcooldown(prices:list):
   profit = 0;prevbuy,prevsold = -math.inf,-math.inf
   
   for p in prices:
      temp = prevsold
      prevsold = prevbuy + p
      prevbuy = max(prevbuy, profit - p)
      profit = max(profit,temp)
   
   return max(profit,prevsold)



if __name__ == "__main__":
   prices = [7,1,5,3,6,4,3,8]
   Pric = [2,1,4,5,2,9,7]
   
   # Q.1) Single stock, single buy
   print("Single buy: ")
   print(maxprofit(prices),end = " ")
   print(maxProfit(prices))   
   
   # Q.2) Single stock, multiple buy
   print("Multiple buys: ")
   print(MaxProfit(prices),end = " ")
   print(maximumprofit(prices))
   
   # Q.3) Single stock, two buys
   print("Two buys: ")
   print(twotransistionProfit(prices),end = " ")
   print(Twobuyprofit(Pric),end = " ")
   print(TwotransistionProfit(Pric))
   
   # Q.4) Single stock, k buys
   k = 2; Prices = [3,2,6,5,0,3]
   print("k buys: ")
   print(KtransistionProfit(Prices,k),end = " ")
   print(KthoptimalProfit(k,Prices))
   
   # Q.5) Multiple buys with 1 day cooldown
   pp = [1,2,3,0,2]
   print("Buy with 1 day cooldown: ")
   print(NetProfitwithcooldown(pp),end = " ")
   print(Profitcooldown(pp))
   

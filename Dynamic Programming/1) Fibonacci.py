""" NOTE:
We can create an easy and automatic memoization using functool in python
"""
# Dynamic programming tutorial:

# 1) Brute force
def fib(n):
   if(n<=1):
      return n
   else:
      return fib(n-1)+fib(n-2)

# 2) Top down
def fibo_helper(n,ans):
   if(n<=1):
      return n
   
   # to check if output already exist
   if(ans[n] != -1):
      return ans[n]
   else:
      ans[n] = fibo_helper(n-1,ans) + fibo_helper(n-2,ans)
      return ans[n]

def Fib(n):
   ans = [-1]*(n+1)
#  initially with -1
   for i in range(0,n+1):
      ans[i] = -1

   return fibo_helper(n,ans)

# 3) Down Up
def fibo(n):
   res = [-1]*(n+1)

   res[0] = 0
   res[1] = 1

   for i in range(2,n+1):
      res[i] = res[i-1] + res[i-2]

   return res[n]

# 4) Optimization
def Fibo(n):
   current,last,yester = 0,1,1

   for i in range(2,n):
      current = last+yester
      yester = last
      last = current
   
   return current

# 5) Direct
def Fibonacci(n,temp = dict()):
   if(n in temp): 
      return temp[n]

   if(n<=1):
      return n
   
   temp[n] = Fibonacci(n-1,temp) + Fibonacci(n-2,temp)
   return temp[n]



print(fib(23))
print(Fib(22))
print(fibo(42))
print(Fibo(35))
print(Fibonacci(29))

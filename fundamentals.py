import os
import sys

def gcd(dividendo, divisor):
  print(dividendo, divisor)

  if(divisor > dividendo):
   temp = dividendo  
   dividendo = divisor
   divisor = temp
    
  if(dividendo % divisor != 0):
    return gcd(divisor, dividendo % divisor)
  else:
    return divisor

print(gcd(8, 12))

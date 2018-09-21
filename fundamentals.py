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


def binary_search(data_set, to_find_number, p, r):
 middle = (p + r) / 2

 if(p > r):
   return False
 
 if(data_set[middle] > to_find_number ):
   return binary_search(data_set, to_find_number, 0, middle - 1) 
 elif(data_set[middle] < to_find_number):
   return binary_search(data_set, to_find_number, middle + 1, r)
 else:
  return (to_find_number == data_set[middle]) 


data_set = [3, 5, 10 , 20]
print(binary_search(data_set, 20, 0, len(data_set)))









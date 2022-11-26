# Program to find 0 in a list
#L = [1, 2, 3, 0, 5, 6, 2, 9, 8, 7]
'''def check0(L):
  
  if (len(L)==0):
    return 0
  
  if(L[0]==0):
    return 1
  else:
    return check0(L[1:len(L)])

print (check0(L))'''

#program to sort a list recursively
'''L = [6, 7, 87, 45, 44, 76, 9]
def findMin(L):
  min = L[0]
  for i in L:
    if (i < min):
      min = i
  return min


def Sort(L):
  if (L == []) or (len(L) == 1):
     return L
  m = findMin(L)
  L.remove(m)
  return [m] + Sort(L)

print(Sort(L))'''

#obvious search
#L = [6, 7, 87, 45, 44, 76, 9]
'''def obvious_search(L,k):

  for i in L :
    if(L[i]==k):
      return 1
    else:
      return 0
      '''

#Binary search
#L=[6, 7, 87, 45, 44, 76, 9]
#import time
'''def binary_search(L,k):
  
  begin =0
  end =len(L)-1
  
  while(end-begin>1):
    
    mid =(begin+end)//2
    if(L[mid]==k):
      return 1
      
    if(L[mid]>k):
      end =mid-1
      
    if(L[mid]<k):
      begin =mid+1
      
  if((L[begin]==k) or (L[end]==k)):
    return 1
  else:
    return 0
'''
'''L=list(range(100*1000*100))
a= time.time()
print(binary_search(L,-1))
b= time.time()
print(b-a)

c= time.time()
print(obvious_search(L,-1))
d= time.time()
print(d-c)'''


# Binary search recursion

def binary_search_recursion(L,k,begin,end):
  if (begin==end):
    if(begin==k):
      return 1
    else:
      return 0
  if(end-begin ==1):
    if(begin==k) or (end==k):
      return 1
    else:
      return 0
  if(end-begin>1):
    mid =(begin+end)//2
    if(k>L[mid]):
      begin =mid+1
    if(k<L[mid]):
      end=mid-1
    if(L[mid]==k):
      return 1  
  return binary_search_recursion(L,k,begin,end)
  
L=list(range(100*100*100))
print(binary_search_recursion(L,66999,0,len(L)-1))

  
      
    
      
    
      
    
    
    
    
  
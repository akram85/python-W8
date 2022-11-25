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
L = [6, 7, 87, 45, 44, 76, 9]
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

print(Sort(L))

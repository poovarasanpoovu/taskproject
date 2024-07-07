
def func(n):
    k=30
    for i in range(0,n):# iterator 0
      for j in range(0,k): #iterator space 0 to 29
          print(end= " ")
      k=k-1 #value change as 29
      for j in range(0,i+1): #iterator
          print("*",end=" ")
      print("")

func(6)
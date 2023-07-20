R=int(input())
for i in range(1,R+1):
  for j in range(1,i):
    print(" ",end="")
  for j in range(i,R+1):
    if j==R:
      print("*",end="")
    else:
      print("*",end=" ")
  print()

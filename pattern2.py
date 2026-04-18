"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

# n=int(input("enter N :"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i , end=" ")
#     print()

#     #enter any number and output will be its corresponding pattern


"""
5 4 3 2 1
4 3 2 1
3 2 1 
2 1
1

"""

# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j, end=" ")
#     print()



"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

"""
# n=int(input("Enter n:")) # put n =5 for desired output
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i, end=" ")
#     print()

"""
*****
****
***
**
*
"""
# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print("*", end="")
#     print()


"""
12345
1234
123
12
1
"""
# for i in range(5,0,-1):
#     for j in range(1, i+1):
#         print(j, end="")
#     print()


"""
    *
   ***
  *****
 *******
"""


# for i in range(0,5):
#     space= 5-i
#     star=2*i-1
#     print(" "* space + "*"*star)


"""
*********
 *******
  *****
   ***
    *
"""

n=int(input("enter n"))
for i in range(0,n+1):
    star= 2*n - (2*i-1)
    space= i
    print(" " * space + "*"* star)
    print()
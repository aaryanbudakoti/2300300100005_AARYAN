    # *****
    # *****
    # *****
    # *****
    # *****

# for i in range(5):
#     for j in range(2,7):
#         print("*", end="")
#     print()



"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""

# for i in range(0,4):
#     for j in range(0,4):
#         print("*" ,end=" ")
#     print()


"""
*
* *
* * *
* * * *
* * * * *
"""
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*" , end=" ")
#     print()


"""
* * * *
* * *
* *
*
"""




# give input for pattern

print("Enter n : ") # enter n =4 for desired output
n= int(input())
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print("*" , end=" ")
    print()
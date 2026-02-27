input=36

s=0
e=input
while(s<e):
        mid=s+(e-s)//2
        if mid*mid==e:
            print(f"Square root of {e} is ")
        elif mid*mid<e:
            e=mid-1
        elif mid*mid>e:
            s=mid+1


print(f"Square root of {e} is {mid}")
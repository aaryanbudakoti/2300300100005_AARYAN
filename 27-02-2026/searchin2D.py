arr = [
        [2,4,6,8],
        [10,12,14,16],
        [18,20,22,24]
        ]

target=10
found=False
for i in range(len(arr)):

    for j in range(len(arr)):

        if arr[i][j]==target:
            print(f"Target found at {i+1}th row and {j+1}th column")
            found=True
        

if not found:
    print("Target element not found")
            #THIS IS THE BRUTE FORCE APPROACH TO SEARCH IN A 2D MATRIX
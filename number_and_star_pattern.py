# * 
# * 1
# * 1 *
# * 1 * 3
# * 1 * 3 *
# * 1 * 3 * 5


n=int(input("Enter a number:"))

for i in range(0,n+1):
    for j in range(0,i+1):
        if(j%2==0):
            print("*",end=" ")
        else:
            print(j,end=" ")
    print()
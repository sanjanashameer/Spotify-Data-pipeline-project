# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def linear_search(l,tar):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(low+high)//2
        if l[mid]==tar:
            return mid
        elif l[mid]<tar:
            low=mid+1
        else:
            high=mid-1
    return -1
l=list(map(int,input().split()))
tar=int(input())
res=linear_search(l,tar)
if res==-1:
    print('not found')
else:
    print('found at:',res+1)
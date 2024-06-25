#Given a list of n-1 integers and these integers are in the range of 1 to n. 
#There are no duplicates in list. One of the integers is missing in the list. Write an efficient code to find the missing integer. 
#timecomplexity O(logn)
def search(a):
    if a[0]==0:
        return ("Invalid")
    if a[0]!=1:
        a.insert(0,1)
        return 1
    if a[len(a)-1]==len(a):
        return a[len(a)-1]+1
    else:
        low = 0
        high = len(a)-1
        while low<=high:
            mid = low+(high-low)//2
            if a[mid]==mid+1 and a[mid+1]==mid+3:
                return a[mid]+1
            if mid+2==a[mid]:
                high=mid-1
            else:
                low=mid+1
                       
b=search([1])
print(b)
b=search([1,2,3,4,5])
print(b)
b=search([2,3,4,5])
print(b)
b=search([0])
print(b)


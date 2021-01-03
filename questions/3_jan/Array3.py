def kthSmallest(arr, k):
    '''
    arr : given array
    l : starting index of the array i.e 0
    r : ending index of the array i.e size-1
    k : find kth smallest element and return using this function
    '''
    sort = sorted(arr)
    return sort[k-1]

if __name__ == '__main__':
    no = input()
    
    for i in no:
        arr = list(map(int,input().strip().split()))
        k = int(input())
        print(kthSmallest(arr,k))
    
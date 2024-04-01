if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    newarr = list(set(arr))
    
    newarr.sort(reverse = True)
    
    print(newarr[1])
        
    

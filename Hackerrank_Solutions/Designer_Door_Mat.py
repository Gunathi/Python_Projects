
def print_door_mat(n, m):
    pattern = [('.|.' * (2 * i + 1)).center(m, '-') for i in range(n // 2)]
    welcome = 'WELCOME'.center(m, '-')
    
    for line in pattern:
        print(line)
        
    print(welcome)

    for line in reversed(pattern):
        print(line)

if __name__ == "__main__":
    n, m = map(int, input().split())
    
    print_door_mat(n, m)

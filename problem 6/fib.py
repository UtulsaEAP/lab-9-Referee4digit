def fibonacci(start_num):
    if start_num < 0:
        return -1
    elif start_num == 0:
        return 0
    elif start_num == 1:
        return 1
    
    x, y = 0, 1
    for _ in range(2, start_num + 1):
        x, y = y, x + y
    return y

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')
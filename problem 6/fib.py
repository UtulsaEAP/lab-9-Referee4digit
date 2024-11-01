def fibonacci(n):
    
    #write your code here
    x=0
    y=1
    while start_num>0:
        z=y-x
        x=x+z
        y=y+z
        start_num-=1
    return (x+y)


if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')
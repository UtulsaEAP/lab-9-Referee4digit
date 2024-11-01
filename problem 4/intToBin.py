def int_to_reverse_binary(num1):
    binary_val = ''
    #write your while loop here
    while num1>0:
        x=num1 % 2
        binary_val=binary_val+str(x)
    return binary_val


def string_reverse(input_string): 
    reverse_input = ''
    length=len(int_to_reverse_binary(num1))
    john=length-1
    empty=[0]*length
    for i in int_to_reverse_binary(num1):
        empty[john]=i
        john-=1
    reverse_input=''.join(empty)
    return reverse_input

if __name__ == '__main__':
    print("Enter the number: ")
    num1 = int(input())
    
    binary_string = str(int_to_reverse_binary(num1))
    binary_string = str(string_reverse(binary_string))
    
    print(binary_string)
def int_to_reverse_binary(num1):
    binary_val = ''
    #write your while loop here
    if num1 == 0:
        return "0"
    binary_val = ""
    while num1>0:
        binary_val+=str(num1 % 2)
        num1//=2
    return binary_val
    

def string_reverse(input_string): 
    return input_string[::-1]

if __name__ == '__main__':
    print("Enter the number: ")
    num1 = int(input())
    
    binary_string = str(int_to_reverse_binary(num1))
    binary_string = str(string_reverse(binary_string))
    
    print(binary_string)
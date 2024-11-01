def feet_to_steps(user_feet):
   #write your code here
   return int((user_feet/2.5))

if __name__ == '__main__':
    #take input feet steps here
    print("Enter your steps: ")
    user_feet=float(input())
    #store it into the function
    print(feet_to_steps(user_feet))
    
    #print your steps here
    feet_to_steps(5280)

sum = 0
while (True):
    num = input("Enter the price or press q to quit:👉 ")
    if(num != 'q'):
        sum = sum + int(num)
        print(f"Order total so far: {sum}💸")
    else:
        
        print(f"Your total bill is {sum}💸")
        print("Thanks for using our calculator!🙂")
        break
        
    
    
    
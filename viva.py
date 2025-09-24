def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 ==0:
        print("fizz")
    elif num % 5 ==0:
        print("buzz")
    else:
        print(num)

def main():
    num= input("input a number: ")
    
    if num.isdigit():
        fizzbuzz(int(num))
        
    else:
        print("invalid input, exiting")
        return
    
if __name__ =="__main__":
    main()
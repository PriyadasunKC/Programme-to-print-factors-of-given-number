def factors(num):
    cal = 1
    while(cal != num+1):
        if(num % cal == 0):
            print(cal,end=" ")
        cal += 1

number = int(input("Enter Integer : "))
factors(number)

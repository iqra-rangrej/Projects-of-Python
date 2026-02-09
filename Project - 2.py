# Pattern Generator and Number Anayzer 

print("Welcome to the Pattern Generator and Number Analyzer !")
print()
while True:
    print("Select an option :")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")
    choice=int(input("Enter your choice :"))
    if choice==1:
       rows=int(input("Enter the number of rows for the pattern :"))
       if rows<=0:
        print("Invalid Input! Rows must be positive. ")
       else:
        print("Pattern :")
        for i in range (1,rows+1):
            for j in range (i):
                print("*",end=" ")
            print()
    elif choice==2:
      start=int(input("Enter the start range :"))
      end=int(input("Enter the end range :"))
      if end<start:
        print("Invalid Input! End must be greater than start.")
      else:
       total_sum=0
      for num in range(start,end+1):
        if num%2==0:
            print(f"Number {num} is Even")
        else:
            print(f"Number {num} is Odd")
            total_sum+=num
      print(f"Sum of all numbers from {start} to {end} is : {total_sum}")
    elif choice==3:
       print(f"Exiting the program. Goodbye!")
       break
    else:
      print("Invalid choice!Please select 1,2 or 3.")

# Project 4 - Data Analyzer and Transformer Program :

dataset=[]
total_elements=0
overall_mean=0
def input_data():
    """Takes user input and stores numbers into a global dataset list."""
    global dataset 
    print("Step 1: Input Data ")
    data=input("Enter data for 1D Array (seperated by spaces) :")
    dataset=list(map(int,data.split()))
    print("Data has been stored successfully !")
def display_summary():
    """Display summary using built-in functions."""
    global total_elements,overall_mean
    print("Step 2 : Display Data Summary (Built-in Functions)")
    total_elements=len(dataset)
    minimum=min(dataset)
    maximum=max(dataset)
    total_sum=sum(dataset)
    overall_mean=total_sum/total_elements
    print("Data Summary : ")
    print("Total Elements : ",total_elements)
    print("Minimum value : ",minimum)
    print("Maximum value : ",maximum)
    print("Sum of all values : ",total_sum)
    print("Average value : ",round(overall_mean, 2))
def factorial (n):
    """Recursive function to calculate factorial of a number"""
    if n==0 or n==1 :
        return 1
    else :
        return n*factorial(n-1)
def calculate_factorial():
    print("Step # : Calculate Factorial (Recursion)")
    num=int(input("Enter a number to calculate its factorial : "))
    print("Factorial of" , num, "is : ",factorial(num))
def filter_data():
    """Uses lambda function to filter data above a threshold."""
    print("Step 4 : Filter Data by Threshold (Lambda Function)")
    threshold=int(input("Enter a threshold value : "))
    filtered=list(filter(lambda x : x>= threshold, dataset))
    print("Filtered Data(values>=", threshold, ") : ")
    print(filtered)
def sort_data():
    """Sort Data in ascending or descending order."""
    print("Step 5 : Sort Data")
    print("1. Ascending")
    print("2. Descending")
    choice=input("Choose sorting option : ")
    if choice=="1":
        sorted_data=sorted(dataset)
        print("Sorted Data in Ascending Order : ")
        print(sorted_data)
    elif choice=="2":
        sorted_data=sorted(dataset,reverse=True)
        print("Sorted Data in Descending Order : ")
        print(sorted_data)
    else:
        print("Invalid choice!")
def dataset_statistics():
    """Returns multiple statistics values."""
    minimum=min(dataset)
    maximum=max(dataset)
    total_sum=sum(dataset)
    average=total_sum/len(dataset)
    return minimum,maximum,total_sum,average
def display_statistics():
    print("Step 6 : Display Dataset Statistics (Return Multiple Values)")
    min_val , max_val , total_sum , avg=dataset_statistics()
    print("Dataset Statistics : ")
    print("Minimun value : " , min_val)
    print("Maximun value : ", max_val)
    print("Sum of all values : ", total_sum)
    print("Average value : ", round(avg, 2))
def show_args(*args):
    print("Using *args :")
    for value in args:
        print(value)
def show_kwargs(**kwargs):
    print("Using **kwargs :")
    for key, value in kwargs.items():
        print(key, ":", value)
def main_menu():
    """Main menu of the program."""
    while True:
      print("==============================================")
      print("Welcome to the Data Analyzer and Transformer Program")
      print("==============================================")
      print("1. Input Data")
      print("2. Display Data Summary (Built-in Fuctions)")
      print("3. Calculate Factorial (Recursion)")
      print("4. Filter Data by Threshold (Lambda Function)")
      print("5. Sort Data")
      print("6. Diplay Dataset Statistics (Return Multiple Values)")
      print("7. Exit Program")
      choice=input("Enter your choice : ")
      if choice=="1":
          input_data()
      elif choice=="2":
          display_summary()
      elif choice=="3":
          calculate_factorial()
      elif choice=="4":
          filter_data()
      elif choice=="5":
          sort_data()
      elif choice=="6":
          display_statistics()
      elif choice=="7":
          print("Thank you! Exiting program...")
          break
      else:
          print("Invalid choice. Please try again.")
main_menu()      
          
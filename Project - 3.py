# Project - 3 : Student Data Organizer 
print()
print("Welcome to the Student Data Organizer !")
students=[]
print()
while True:
   print("Select an option :")
   print("1. Add Student")
   print("2. Display All Students")
   print("3. Update Student Information")
   print("4. Delete Student")
   print("5. Display Subjects Offered")
   print("6. Exit")   
   choice=int(input("Enter you choice : "))
   print()
   if choice==1:
      sid=int(input("Enter Student ID : "))
      name=input("Name : ")
      age=int(input("Age : "))
      grade=input("Grade : ")
      dob=(input("Date of Birth (YYYY-MM-DD) : "))
      sub=input("Subjects (comma-seperated): ")
      subjects=set(sub.split(" , "))
      id_dob=(sid,dob)
      student={
         "id_dob" : id_dob,
         "name" : name,
         "age" : age,
         "grade" : grade,
         "subjects" : subjects
      }
      students.append(student)
      print()
      print("Student added successfully!")
      print("-"*50)
   elif choice==2:
      print("-------Display All Students-------")
      if not students :
         print("No students added yet!")
      for s in students:
         print(f"Student ID : {s['id_dob'][0]} |"
               f" Name : {s['name']} |"
               f" Age : {s['age']} |"
               f" Grade : {s['grade']} |"
               f" Subjects : {' , '.join(s['subjects'])}")
         print("-"*50)
   elif choice==3:
      sid=int(input("Enter Students ID to Update :"))
      for s in students :
         if s["id_dob"][0]==sid:
            new_age=int(input("Enter new age :"))
            s["age"]=new_age
            print()
            print("Age Updated!")
            print("-"*50)
            break
   elif choice==4:
      sid=int(input("Enter student ID to delete :"))
      for i in range (len(students)):
         if students [i]["id_dob"][0]==sid:
            del students[i]
            print()
            print("Students Deleted!")
            print("-"*50)
            break
         else:
            print("Student not found!")
            print("-"*50)
   elif choice==5:
      all_sub=set()
      for s in students:
          all_sub.update(s["subjects"])
      if not all_sub:
          print("No subjects available.")
      else:
          print("Subjects Offered :")
          for sub in all_sub:
             print("-%s"%sub)
             print("-"*50)
   elif choice==6:
      print("Thank you for using the program!")
      print("-"*50)
      break
   else:
      print("Invalid choice!")
      print("-"*50)
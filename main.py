


def main():
    user_id = input("Enter student's ID: ")
    test1 = float(input("Enter student's test1 score: "))
    test2 = float(input("Enter student's test2 score: "))
    test3 = float(input("Enter student's test3 score: "))
    interim_test = float(input("Enter student's IA score: "))
    exam_score = float(input("Enter student's exam score: "))

    student_details = { user_id: {
    "test1": test1,
    "test2": test2,
    "test3": test3,
    "interim_test": interim_test,
    "exam_score": exam_score
    }}
        
    with open("Student-details.txt", "w") as file:
        file.write(f"\n Student_ID:  {user_id}\n Test1_score:  {test1}\n Test2_score:  {test2}\n Test3_score:  {test3}\n Interim_test_score:  {interim_test}\n Exam_score:  {exam_score}\n")
    

    def add_student_details():
        user_id = input("Enter student's ID: ")
        test1 = float(input("Enter student's test1 score: "))
        test2 = float(input("Enter student's test2 score: "))
        test3 = float(input("Enter student's test3 score: "))
        interim_test = float(input("Enter student's IA score: "))
        exam_score = float(input("Enter student's exam score: "))

     
        student_details.update({user_id: {
        "test1": test1,
        "tes2": test2,
        "test3": test3,
        "interim_test": interim_test,
        "exam_score": exam_score
        }})
        

        with open("Student-details.txt", "a") as file:
            file.write(f"\n Student_ID:  {user_id}\n Test1_score:  {test1}\n Test2_score:  {test2}\n Test3_score:  {test3}\n Interim_test_score:  {interim_test}\n Exam_score:  {exam_score}\n")


    def read_details():
        with open("Student-details.txt", "r") as file:
            data = file.read().splitlines()
            for line in data:
                print(line)
            print("\n")    

    def search_student_score():
        
        id = input('Enter target student ID: ')
        if id in student_details:
            for key, value in student_details[id].items():
                print(key," : ", value)
    
    def update_student_details():
        user_id= input('Enter target student ID: ')
        if user_id in student_details:
            test1=float(input("Enter test one score: "))
            test2=float(input("Enter test two score: "))
            test3=float(input("Enter test three score: "))
            interim_test=float(input("Enter IA score: "))
            exam_score=float(input("Enter examination score: "))
            with open("Student-details.txt", "w") as file:
                file.write(f"\n Student_ID:  {user_id}\n Test1_score:  {test1}\n Test2_score:  {test2}\n Test3_score:  {test3}\n Interim_test_score:  {interim_test}\n Exam_score:  {exam_score}\n")

    
  

    def options():
            print("1: View all students details \n2: Add the details of a student \n3: Add a new book to the database \n4: Update student details\n5: Close program")
            opt = int(input("Choose your option: "))
            while opt != 5:
                if opt == 1:
                    read_details()
                    return options()
                elif opt == 2:
                    add_student_details()
                    return options()
                elif opt == 3:
                    search_student_score()
                    return options()
                elif opt == 4:
                    update_student_details()
                    return options()
                elif opt == 5:
                    break    
                else:
                    print("Invalid Input \nEnter 1-4")
                    return options()
    options()                
    with open("Student-details.txt", "w") as file:
        file.write(f"\n Student_ID:  {user_id}\n Test1_score:  {test1}\n Test2_score:  {test2}\n Test3_score:  {test3}\n Interim_test_score:  {interim_test}\n Exam_score:  {exam_score}\n")
    
    
main()            
                

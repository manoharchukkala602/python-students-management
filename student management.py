students =[]
def grade_student(avg):
    if avg <= 80:
        return "A grade"
    if avg <= 60:
        return " B grade"
    elif avg <= 40:
        return " C grade"
    else:
        print("fail")
    return
        

def add_student():
    try:
        pin =int(input("enter student id:"))
        name =input("enter student name:")
        m1 =float(input("enter your marks in m1:"))
        m2 =float(input("enter your marks in m2:"))
        m3 = float(input("enter your marks in m3:"))

        if m1 > 100 or m2 > 100 or m3 >100:
            print("its grater than 100 its not returned")

        total = m1+m2+m3
        average =total/3
        grade = grade_student(average)
        print("grade",grade)
        print(f"total:{total}")
        print(f"average:{average}")
        

        student ={
            "name":name,
            "pin":pin,
            "marks":total,
            "average":average,
            "grade": grade,
            }
        students.append(student)
    except ValueError:
        print("invalid")
    return

def list_student():
    if not students:
        print("students are not found:")
        return
    for s in students :
        print("name",s["name"])
        print("id",s["pin"])
        print("marks",s["marks"])
        print("average",s["average"])
        print("grade",s["grade"])
    else:
        print("sorry your name is not found in this ")

def search_students():
    po =int(input("Enter your pin:"))
    for stu in students:
        if po == stu["pin"]:
            print("name",stu["name"])
            
        else:
           print("your not in list")
           return


while True:
    print("Enter the student menu:")
    print("1.grade student")
    print("2.add student")
    print("3.list student")
    print("4.search student")
    
    choice =input("enter your choose:")
    if choice == "1":
        grade_student()
    if choice == "2":
        add_student()
    if choice == "3":
        list_student()
    elif choice =="4":
        search_students()
        break
    else:
        print("sorry unfindble")
        

        
        

    
        
    

        
            
            
    

    
            
            

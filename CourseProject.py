import getpass

from Students import Students1

def main():

    print("Welcome in Humber College")
    password = getpass.getpass(prompt="Please enter the password : ")
    upper = [l for l in password if l.isupper()]
    num = [n for n in password if n.isnumeric()]
    sp = '[@_!#$%^&*()<>?/\|}{~:]'
    spe = [s for s in password if s in sp]
    student_names = []
    combined_data = []
    accepted_count = 0
    notaccepted_count = 0
    Schools_data = [['School of Engineering',0],['School of Business',0],['Law School',0],['Not Accepted',0]]

    print(password)

    if len(password) < 10:
        print("Password invalid due to length.")
    elif upper == []:
        print("Password invalid, no uppercase alphabet found.")
    elif len(num)<2 or len(num)>3:
        print("Password invalid, it does not have right number of numeric values.")
    elif len(spe)!=1:
        print("Password invalid, incorrect number of special characters.")
    else:
        print("Password is valid.")

    for i in range(0,3):
        number_of_students = int(input("Please enter valid number of students : "))
        if (number_of_students<=0 or number_of_students>50) and i==2:
            print("You have exceeded the available number of attempts. Please run the program again.")
            break
        if number_of_students>0 and number_of_students<=50:
            break
        else:
            continue
    
    for j in range(1,number_of_students+1):
        name = input(f"Enter the name of {j}th student : ")
        student_names.append(name)


    std=[]
    GPA_list = []
    for i in range (number_of_students):
        Ma = int(input("Enter your marks in Maths: "))
        Sc = int(input("Enter your marks in Science: "))
        La = int(input("Enter your marks in Language: "))
        Dr = int(input("Enter your marks in Drama: "))
        Mu = int(input("Enter your marks in Music: "))
        Bi = int(input("Enter your marks in Biology: "))
        std.append(Students1(Ma,Sc,La,Dr,Mu,Bi))
    for i in range (len(std)):
       GPA_list.append(std[i].getGPA())

    for i in range(0,len(student_names)):
        combined_data.append([student_names[i],GPA_list[i],[]])

    for i in range(0,len(combined_data)):
        if combined_data[i][1] >= 90 and combined_data[i][1] <= 100:
            combined_data[i][2] = 'School of Engineering'
            Schools_data[0][1] = Schools_data[0][1] + 1
        elif combined_data[i][1] >= 80 and combined_data[i][1] < 90:
            combined_data[i][2] = 'School of Business'
            Schools_data[1][1] = Schools_data[1][1] + 1
        elif combined_data[i][1] >= 70 and combined_data[i][1] < 80:
            combined_data[i][2] = 'Law School'
            Schools_data[2][1] = Schools_data[2][1] + 1
        else:
            combined_data[i][2] = 'Not Accepted'
            Schools_data[3][1] = Schools_data[3][1] + 1

    print(combined_data)


    for i in range(0,len(combined_data)):
        if combined_data[i][2] == 'Not Accepted':
            notaccepted_count = notaccepted_count+1
        else:
            accepted_count = accepted_count+1

    print(f"Number of students accepted in Humber College is {accepted_count}")
    print(f"Number of students not accepted in Humber College is {notaccepted_count}")

    print(Schools_data)

main()

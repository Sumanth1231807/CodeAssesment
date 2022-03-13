import sqlite3 as sql
from prettytable import PrettyTable

connection = sql.connect("Employe.db")




while True:
    print("1. Add Employee :")
    print("2. View Employees :")
    print("3. Search Employee using Partial name :")
    print("4. Update employee using employee code :")
    print("5. Delete an employee using employee code:")
    print("6. Display all the details of employees whose salary is greater than 50000 :")
    print("7. Display  the count of no of employees :")
    print("8.: display employee details in alphatical order ,within the specific salary range")
    print("9. display data,salary is less than avg salary  :")
    print("10. EXIT")

    choice=int(input("Enter choice :"))

    if choice == 1:
        getEmpcode = input("Enter Empcode :")
        getName = input("Enter name :")
        getPhone = input("Enter phone :")
        getEmail = input("Enter email:")
        getDes = input("Enter designation :")
        getSal = input("Enter salary:")
        getCom = input("Enter company name:")

        connection.execute("insert into employee(empCode,name,phone,email ,designation,salary,companyname)\
                               values(" + getEmpcode + ",'" + getName + "'," + getPhone + ",'" + getEmail + "','" + getDes + "'," + getSal + ",'" + getCom + "')")
        connection.commit()
        print("Employee Data Added Successfully.")

    elif choice == 2:
        result = connection.execute("select * from employee")
        table = PrettyTable(["empcode", "empname", "phone", "email", "designation", "salary", "companyname"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6]])
        print(table)


    elif choice == 3:
        getName = input("Search the Partial Name Which you want:")

        result = connection.execute("select * from employee where Name like '%" + getName + "%'")
        table = PrettyTable(["empcode", "empname", "phone", "email", "designation", "salary", "companyname"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6]])
        print(table)



    elif choice == 4:
        getEmpcode = input("Enter the employee code to get Update :")

        getName = input("Enter name :")
        getPhone = input("Enter phone :")
        getEmail = input("Enter email:")
        getDes = input("Enter designation :")
        getSal = input("Enter salary:")
        getCom = input("Enter company name:")
        connection.execute(
            "update employee set Name='" + getName + "',phone=" + getPhone + ",email='" + getEmail + "',designation='" + getDes + "',salary=" + getSal + ",companyname='" + getCom + "' where empCode=" + getEmpcode + "")
        connection.commit()
        print("Updated Successfully.")



    elif choice == 5:
        getEmpcode = input("Enter the Employee code to get Delete :")
        connection.execute("delete from employee where empCode=" + getEmpcode + "")
        connection.commit()
        print("Data Deleted Successfully.")



    elif choice == 6:
        result = connection.execute("select * from employee where salary>50000")
        table = PrettyTable(["empcode", "empname", "phone", "email", "designation", "salary", "companyname"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6]])
        print(table)


    elif choice == 7:
        result = connection.execute("select count(*) from employee")
        for i in result:
            print("Total employee Count :", i[0])





    elif choice == 8:
        lowrange = input("Enter lowest range of salary to sort")
        highrange = input("Enter higher range of salary to sort")
        result = connection.execute(
            "select * from employee where salary between " + lowrange + " and " + highrange + " order by name asc")
        table = PrettyTable(["empcode", "empname", "phone", "email", "designation", "salary", "companyname"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6]])
        print(table)




    elif choice == 9:

        result = connection.execute("select * from employee where salary < (select avg(salary) from employee)")
        table = PrettyTable(["empcode", "empname", "phone", "email", "designation", "salary", "companyname"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6]])
        print(table)



    elif choice == 10:
        break

    else:
        print("invalid")







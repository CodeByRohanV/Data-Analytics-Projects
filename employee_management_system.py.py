def menu():
    while True:
        print("\nWelcome to Employee Management Record")
        print("Press:")
        print("1 to Add Employee")
        print("2 to Remove Employee")
        print("3 to Promote Employee")
        print("4 to Display Employees")
        print("5 to Exit")
        
        # Taking choice from user
        ch = input("Enter your Choice: ")

        if ch == '1':
            addData()
        elif ch == '2':
            removeData()
        elif ch == '3':
            incSalary()
        elif ch == '4':
            display_employees()
        elif ch == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid Choice! Please try again.")

import mysql.connector
con = mysql.connector.connect(username='root', password='Rohan@123', host='localhost', database='emp')

def checkNum(empID):
    sql = 'select * from empDetails where personID=%s'

    cursor = con.cursor(buffered=True)
    data = (empID,)
    cursor.execute(sql,data)
    employee = cursor.fetchone()
    cursor.close()
    return employee is not None
    

# adding data 

def addData():
    id = input("Enter the id of emp")
    # check if id is there in table 
    if(checkNum(id)):
        print(f"Employee{id} is already added")
        return
    else:
        name = input("Enter the name ")
        post = input("Enter the post ")
        salary = input("Enter the salary")
        sql = 'insert into empDetails (personID,name,post,salary) values (%s,%s,%s,%s)'
        data = (id,name, post ,salary)
        cursor = con.cursor(buffered=True)

        #since we are adding data to table exception handling is required 
        try:
            cursor.execute(sql,data) # This will add data to table 
            con.commit() # permentaly saved in sql 
            print("Data added successfully")
        except mysql.connector.Error as err:
            print(f"Error = {err}")
            con.rollback() 
        finally:
            cursor.close()

# to remove data 
def removeData():
    id = input("Enter the id to delete")
    if not checkNum(id):
        print(f"Employee {id} is not there in the list")
        return
    else:
        
        sql = 'delete from empDetails where personID=%s'
        data = (id,)
        cursor = con.cursor()
        try:
            cursor.execute(sql,data)
            print("HE is remove from table")
            con.commit()
        except mysql.connector.Error as err:
            print(f"Error = {err}")
            con.rollback()
        finally:
            cursor.close()


# increaing salary

def incSalary():
    amount = int(input("Enter the amount to be updated"))

    id = input("Enter the id to be updated")
    if not checkNum(id):
        print("Enter the correct id ")
        return
    else:
        try:
            sql = 'select salary from empDetails where personID=%s'
            data = (id,)
            cursor = con.cursor()
            cursor.execute(sql,data)
            current_salary = cursor.fetchone()[0]
            update_salary = current_salary + amount

            updQurery = 'update empDetails set salary=%s where PersonID=%s'
            newdata= (update_salary,id)
            cursor.execute(updQurery,newdata)
            con.commit()
            print("Salary increased successfullly")
        except(ValueError,mysql.connector.Error)as err:
            print(f"Error = {err} ")
            con.rollback()
        finally:
            cursor.close()

#display 
def display_employees():
    try:
        # Query to select all rows from the employees table
        sql = 'SELECT * FROM empDetails'
        cursor = con.cursor()

        # Executing the SQL Query
        cursor.execute(sql)

        # Fetching all details of all the Employees
        employees = cursor.fetchall()
        for employee in employees:
            print("Employee Id : ", employee[0])
            print("Employee Name : ", employee[1])
            print("Employee Post : ", employee[2])
            print("Employee Salary : ", employee[3])
            print("------------------------------------")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Closing the cursor
        cursor.close()

menu()
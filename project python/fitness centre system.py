import mysql.connector as sql
conn=sql.connect(host="localhost", user="root", passwd="1234", database="fitness")
mycursor=conn.cursor()
if conn.is_connected():
    print("Conection With Database Establised Successfully")
else:
    print("Conection With Database Failed XXX")

print("************************Welcome to RK FITNESS CENTRE************************")
c1=conn.cursor()
choice = 0
while choice != 3:
    print("1.CREATE YOUR ACCOUNT")
    print("2.LOG IN")
    print("3.EXIT")
    choice=int(input("ENTER YOUR CHOICE:"))
    
    if choice ==1:
     cust_name=input("Enter your name :")
     account_no=int(input("enter your User ID :"))
     password=int(input("Enter your Passpharse :"))
     SQL_insert="insert into Log_in values ('"+cust_name+"',"+str(account_no)+","+str (password)+")"
     c1.execute(SQL_insert)
     conn.commit()
     print("ACCOUNT CREATED")

    if choice==2:
     print('')
     print('Enter your Credentials')
     cust_name=input('Enter your name : ')
     print('')
     account_no=int(input('Enter your User ID : '))
     print(' ')
     password=int(input('Enter your Passpharse : '))
     print(' ')
     c1=conn.cursor()
     c1.execute('select * from Log_in')
     data=c1.fetchall()
     count=c1.rowcount
     c2 = 0
     for row in data:
      if (cust_name in row) and (account_no in row) and (password in row):
            print(' ')
            print(' ')
            print("************************WELCOME TO RK FITNESS CENTRE************************")
            print(' ')
            print(' ')
            print('TO SEE EMPLOYEES DETAILS,press                :1')
            print(' ')
            print('TO UPDATE DETAILS,press                       :2')
            print(' ')
            print('TO SEE Details of all the customer,press      :3')
            print(' ')
            print('TO pay the bill,press                         :4')
            print(' ')
            print('TO EXIT,press                                 :5')
            print(' ')
            print('WANT TO RATE US,press                         :6')
            print(' ')
            c2=int(input("Enter your choice : "))
            if (c2==1):
                c1=conn.cursor()
                c1.execute('select * from log_in')
                data=c1.fetchall()
                count=c1.rowcount
                print('Details of all employees is',count)
                print("Details of all employees are arranged as Name/User ID/Passpharse")
                for row in data:
                    print(row)
                conn.commit()    
                print("VISIT AGAIN")
            elif (c2==2):
                print('')
                print('TO UPDATE FILL THIS')
                print('')
                empName = input("Enter name:")
                update = input("Enter new name:")
                sqlFormula = "UPDATE log_in SET cust_name=%s WHERE cust_name = %s"
                c1.execute(sqlFormula,(update,empName))
                print('YOUR DETAILS ARE SUCESSFULLY UPDATED')

            elif(c2==3):
                  c1=conn.cursor()
                  c1.execute('select * from customer_table ')
                  data=c1.fetchall()
                  count=c1.rowcount
                  print('Details of all the Customers',count)
                  for row in data:
                     print(row)
                  print("VISIT AGAIN")

            elif(c2==4):
                 f_name=input("Enter the your name : ")
                 price=int(input("Enter the amount to be paid : "))
                 wieght=int(input("enter your customer weight : "))
                 cust_name=input("enter Customer Name : ")
                 phone_no=int(input("Enter Customer phone no : "))
                 SQL_insert="insert into customer_table values("+"'"+ f_name+"'"+","+"'"+str(price)+"'"+",'"+str(wieght)+"',"+"'"+cust_name+"'"+","+str(phone_no)+")"
                 c1.execute(SQL_insert)
                 conn.commit()
                 print("Bill Recorded")

            elif (c2==5):
                  print('THANK YOU FOR VISITING')
            

            elif (c2==6):
                print('RATE US FOR SERVICE')
                rating=int(input("On the Scale of 10 how would you like to rate us:"))
                print('THANK FOR RATING')
            else:
                print("Oops, something went wrong.....")
                cl.close

        
     if choice==3:
      print("THANK YOU FOR VISITING")
      cl.close
               
                 
            

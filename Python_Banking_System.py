from random import randint
import mysql.connector
my_db = mysql.connector.connect(host='localhost', user='root', password='15042000',
                                auth_plugin='mysql_native_password', database='BANKING_SYSTEM')
x = my_db.cursor()


def open_account():
    fullname = input("Enter your Name : ")
    aadhar_number = int(input("Enter your Aadhar number : "))
    address = input("Enter your Address : ")
    pincode = int(input("Enter your Pincode : "))
    phone_number = int(input("Enter your Phone number : "))
    balance = int(input("Enter your Opening_Balance : "))
    account_number = ''.join(["{}".format(randint(1, 9)) for _ in range(6)])
    print("Your Account number is : ", account_number)
    sql1 = "INSERT INTO PERSON_DATAS(fullname, aadhar_number, address, pincode, " \
           "phone_number, balance, account_number)" \
           " VALUES(%s, %s, %s, %s, %s, %s, %s)",\
           (fullname, aadhar_number, address, pincode, phone_number, balance, account_number)

    data1 = (fullname, aadhar_number, address, pincode, phone_number, balance, account_number)

    sql2 = "INSERT INTO AMOUNT_DETAILS(fullname, account_number, balance)  VALUES(%s, %s, %s)",\
           (fullname, account_number, balance)

    data2 = (fullname, account_number, balance)

    # noinspection PyTypeChecker
    x.execute(*sql1, data1)
    # noinspection PyTypeChecker
    x.execute(*sql2, data2)
    my_db.commit()

    bank_function()


def deposit_amount():
    fullname = input("Enter your Name : ")
    account_number = int(input("Enter your Account number : "))
    amount = int(input("Enter the Amount you want to Deposit : "))

    sql3 = "UPDATE PERSON_DATAS SET balance = balance + (%s)" \
           " WHERE fullname = %s AND account_number = %s", \
           [amount, fullname, account_number]

    sql4 = "UPDATE AMOUNT_DETAILS SET balance = balance + (%s)" \
           " WHERE fullname = %s AND account_number = %s",\
           [amount, fullname, account_number]
    data3 = (amount, fullname, account_number)
    # noinspection PyTypeChecker
    x.execute(*sql3, data3)
    # noinspection PyTypeChecker
    x.execute(*sql4, data3)
    my_db.commit()

    bank_function()


def withdraw_amount():
    fullname = input("Enter your Name : ")
    amount = int(input("Enter the Amount you want to Withdraw : "))
    account_number = int(input("Enter your Account number : "))

    sql5 = "UPDATE PERSON_DATAS SET balance = balance - (%s)" \
           " WHERE fullname = %s AND account_number = %s", \
           [amount, fullname, account_number]

    sql6 = "UPDATE AMOUNT_DETAILS SET balance = balance - (%s)" \
           " WHERE fullname = %s AND account_number = %s",\
           [amount, fullname, account_number]
    data4 = (amount, fullname, account_number)
    # noinspection PyTypeChecker
    x.execute(*sql5, data4)
    # noinspection PyTypeChecker
    x.execute(*sql6, data4)
    my_db.commit()

    bank_function()


def balance_enquiry():
    account_number = int(input("Enter your Account number : "))

    sql7 = "SELECT balance FROM AMOUNT_DETAILS WHERE account_number IN (%s)", [account_number]

    data5 = account_number

    # noinspection PyTypeChecker
    x.execute(*sql7, data5)
    result = x.fetchone()
    print("Your Current Balance : ", result[0])
    my_db.commit()

    bank_function()


def display_account():
    account_number = int(input("Enter your Account number : "))

    sql8 = "SELECT * FROM PERSON_DATAS WHERE account_number IN (%s)", [account_number]

    data6 = account_number

    # noinspection PyTypeChecker
    x.execute(*sql8, data6)
    result = x.fetchone()
    for i in result:
        print(i, end="\n ")
    my_db.commit()

    bank_function()


def loan_details():
    with open("Loan_Details", 'r') as myfile:
        print(myfile.read())

    bank_function()


def write_your_queries():
    fullname = input("Enter your Name : ")
    account_number = int(input("Enter your Account number : "))
    customer_query = input("Enter your queries : ")

    sql9 = "insert into CUSTOMER_QUERIES (fullname, account_number, customer_query) VALUES(%s, %s, %s)",\
           (fullname, account_number, customer_query)

    data7 = (fullname, account_number, customer_query)

    # noinspection PyTypeChecker
    x.execute(*sql9, data7)
    my_db.commit()
    print("Dear Customer, Thank you for writing your queries. \n We will look into this and get back to you soon !")

    bank_function()


def close_account():
    account_number = int(input("Enter your Account number : "))

    sql10 = "DELETE FROM PERSON_DATAS WHERE account_number IN (%s)", [account_number]
    sql11 = "DELETE FROM AMOUNT_DETAILS WHERE account_number IN (%s)", [account_number]

    data8 = account_number

    # noinspection PyTypeChecker
    x.execute(*sql10, data8)
    # noinspection PyTypeChecker
    x.execute(*sql11, data8)
    my_db.commit()

    bank_function()


def bank_function():
    print("Dear Customer, Welcome To  DKB BANK\nPLEASE SELECT AN OPTION")
    print("1. Open Account\n2. Deposit Amount\n3. Withdraw Amount\n4. Balance_Enquiry"
          "\n5. Display Account Details\n6. Check Loan Details\n7. Write your Queries\n8. Close Account")
    option = int(input("Please enter an option : "))
    if option == 1:
        open_account()
    elif option == 2:
        deposit_amount()
    elif option == 3:
        withdraw_amount()
    elif option == 4:
        balance_enquiry()
    elif option == 5:
        display_account()
    elif option == 6:
        loan_details()
    elif option == 7:
        write_your_queries()
    else:
        close_account()


bank_function()

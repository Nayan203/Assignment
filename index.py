import mysql.connector as db
import pandas as pd

class GiBots(object):


    def login(self):
        con = db.connect(user='root', password='', host='localhost', database='gibots')
        cursor = con.cursor()
        username = input('Enter the Username: ')
        password = input('Enter the Password: ')
        query = '''Select Username, Password from userinfo where userName = '%s' and Password = '%s' '''
        data = (username, password)
        cursor.execute(query% data)
        data = cursor.fetchall()
        lendata = len(data)
        if lendata > 0:
            print('Login Successfully')
        else:
            print('Incorrect Password')

# ------------------------------------------------------------------------------------

    def getRegister(self):
        con = db.connect(user='root', password='', host='localhost', database='gibots')
        cursor = con.cursor()
        username = input('Enter the User Name: ')
        password = input('Enter the Password: ')
        firstname = input('Enter the First Name: ')
        lastname = input('Enter the Last Name: ')
        email = input('Enter the Email: ')
        phoneno = int(input('Enter the Number: '))
        phonelen = len(str(phoneno))
        address = input('Enter the Address: ')
        if phonelen == 10:
            query = '''select Email from userinfo where Email = '%s' '''
            cursor.execute(query % email)
            data = cursor.fetchall()
            lendata = len(data)
            if lendata > 0:
                print('Email Already Exist.')
            else:
                query = '''insert into userinfo values ('%s', '%s', '%s', '%s', '%s', '%s', '%s') '''
                d1 = (username, password, firstname, lastname, email, phoneno, address)
                cursor.execute(query % d1)
                print("You have registered Successfully.")
                con.close
        else:
            print('Phone number should be 10 digit number. Try Again. ')
    # ------------------------------------------------------------------------------------

    def getUpdate(self):
        con = db.connect(user='root', password='', host='localhost', database='gibots')
        cursor = con.cursor()
        username = input('Enter the Username: ')
        password = input('Enter the Password: ')
        query = '''Select Username, Password from userinfo where userName = '%s' and Password = '%s' '''
        data = (username, password)
        cursor.execute(query % data)
        data = cursor.fetchall()
        lendata = len(data)
        if lendata > 0:
            print('Login Successfully')
            firstname = input('Enter the First Name: ')
            lastname = input('Enter the Last Name: ')
            number = int(input('Enter the Mobile No: '))
            address = input('Enter the Address: ')
            query = '''update userinfo set FirstName = '%s', LastName = '%s', PhoneNo = '%s', Address = '%s' 
                       where Username = '%s' '''
            data = (firstname, lastname, number, address, username)
            cursor.execute(query% data)
            con.commit()
            print('Data Updated.')
            con.close
        else:
            print('Incorrect Username or Password')

# ------------------------------------------------------------------------------------

    def searchDetail(self):
        con = db.connect(user='root', password='', host='localhost', database='gibots')
        cursor = con.cursor()
        firstname = input('Enter the First Name: ')
        lastname = input('Enter the Last Name: ')
        number = int(input('Enter the Phone No: '))
        address = input('Enter the Address: ')
        query = '''Select * from userinfo where FirstName = '%s' and LastName = '%s' and PhoneNo = '%s'and Address = '%s' '''
        data = (firstname, lastname, number, address)
        cursor.execute(query% data)
        alldata = cursor.fetchall()
        for i in alldata:
            print('\nUsername is:', i[0])
            print('Password is:', i[1])
            print('First Name is:', i[2])
            print('last Name is:', i[3])
            print('Email is:', i[4])
            print('Phone Number is:', i[5])
            print('Address is:', i[6])
        con.close

# ------------------------------------------------------------------------------------

    def getAllDetails(self):
        con = db.connect(user='root', password='', host='localhost', database='gibots')
        cursor = con.cursor()
        query = '''select * from userinfo'''
        cursor.execute(query)
        fulldata = cursor.fetchall()
        username = []
        password = []
        firstname = []
        lastname = []
        email = []
        phoneno = []
        address = []
        for i in fulldata:
            username.append(i[0])
        for i in fulldata:
            password.append(i[1])
        for i in fulldata:
            firstname.append(i[2])
        for i in fulldata:
            lastname.append(i[3])
        for i in fulldata:
            email.append(i[4])
        for i in fulldata:
            phoneno.append(i[5])
        for i in fulldata:
            address.append(i[6])

        frame = {'Username': username , 'Password': password, 'FirstName': firstname, 'LastName': lastname, 'Email': email,
                 'Phone No': phoneno, 'Address': address}

        dataframe = pd.DataFrame(data=frame)

        # setting to display all column in DataFrame
        pd.set_option("display.max_column", None)
        pd.set_option("display.max_rows", None)
        pd.set_option("display.width", None)
        pd.set_option("display.max_colwidth", None)

        print(dataframe)
# ------------------------------------------------------------------------------------
g1 = GiBots()
print('********************************')
print('     Welcome to GiBots     ')
print('********************************')
print('Press 1 if you want to login.')
print('Press 2 if you want to register.')
print('Press 3 if you want to Update Details.')
print('Press 4 if you want to Search the detail')  # detail of any particular user.
print('Press 5 if you want to get details of all the Users.\n')

choice = int(input('Enter your choice: '))
if choice == 1:
    g1.login()
elif choice == 2:
    g1.getRegister()
elif choice == 3:
    g1.getUpdate()
elif choice == 4:
    g1.searchDetail()
elif choice == 5:
    g1.getAllDetails()
else:
    print('Entered Wrong Choice.. Try Again!!')

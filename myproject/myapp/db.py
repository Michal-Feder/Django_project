
import mysql.connector
from django.db import Error
from mysql.connector import errorcode
from myapp import models

def selectEmployerJson():

    try:
        cnx = mysql.connector.connect(user='root', password='password',
                                      host='localhost',
                                      database="smarti_Test")
        selectEmployersql = """select * from EMPLOYER"""
        cursor = cnx.cursor()
        cursor.execute(selectEmployersql)
        records = cursor.fetchall()
        print("Total number of rows in EMPLOYER is: ", cursor.rowcount," ",records)

        print("\nPrinting each EMPLOYER record")
        result = []
        for row in records:
            employer = models.EMPLOYER(id=row[0],name= row[1],phone=row[2],email=row[3],contacs=selectContant(row[0]))
            contacts = ''
            print("Id = ", row[0], )
            print("Name = ", row[1])
            print("Phone  = ", row[2])
            print("Email  = ", row[3])
            for contact in employer.contacts:
                contacts += contact.toString()
            print("Contact  = ", contacts, "\n")
            result.append(employer.ParseToDicionary())
        return result

    except Error as e:
        print("Error reading data from MySQL table", e)
        return False
    finally:
        if (cnx.is_connected()):
            cnx.close()
            cursor.close()
            print("MySQL connection is closed")




def selectEmployer():

    try:
        cnx = mysql.connector.connect(user='root', password='password',
                                      host='localhost',
                                      database="smarti_Test")
        selectEmployersql = """select * from EMPLOYER"""
        cursor = cnx.cursor()
        cursor.execute(selectEmployersql)
        records = cursor.fetchall()
        print("Total number of rows in EMPLOYER is: ", cursor.rowcount," ",records)

        print("\nPrinting each EMPLOYER record")
        result = []
        for row in records:
            employer = models.EMPLOYER(id=row[0],name= row[1],phone=row[2],email=row[3],contacs=selectContant(row[0]))
            contacts = ''
            print("Id = ", row[0], )
            print("Name = ", row[1])
            print("Phone  = ", row[2])
            print("Email  = ", row[3])
            result.append(employer)
        return result

    except Error as e:
        print("Error reading data from MySQL table", e)
        return False
    finally:
        if (cnx.is_connected()):
            cnx.close()
            cursor.close()
            print("MySQL connection is closed")

def selectContant(id_employer):

    try:
        cnx = mysql.connector.connect(user='root', password='password',
                                      host='localhost',
                                      database="smarti_Test")
        selectContactsql = """select * from Contact where Identifier_employer=%s"""
        cursor = cnx.cursor()
        cursor.execute(selectContactsql,(id_employer,))
        records = cursor.fetchall()
        print("Total number of rows in CONTACT is: ", cursor.rowcount," ",records)

        print("\nPrinting each CONTACT record")
        result = []
        for row in records:
            contact = models.Contact(id=row[0],first_name=row[1],last_name=row[2],phone=row[3],email=row[4],id_employer=row[5])
            print("Id = ", row[0], )
            print("First_Name = ", row[1])
            print("Last_Name  = ", row[2])
            print("Phone  = ", row[3])
            print("Email  = ", row[4], "\n")
            result.append(contact)
        return result

    except Error as e:
        print("Error reading data from MySQL table", e)
        return False
    finally:
        if (cnx.is_connected()):
            cnx.close()
            cursor.close()
            print("MySQL connection is closed")



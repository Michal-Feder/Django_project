from django.db import models


# Create your models here.

class EMPLOYER:
    def __init__(self,id,name,phone,email,contacs=[]):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.contacts = contacs

    def ParseToDicionary(self):
        str = []
        for contact in self.contacts:
            print(len(self.contacts))
            str.append(contact.ParseToDicionary())
        return {
        'id': self.id,
        'name': self.name,
        'phone': self.phone,
        'email': self.email,
        'contacts':str
         }

    def toString(self):
        return "id: " + self.id + " name: " + self.name + " phone: " + self.phone + " email: " + self.email + " contacs: "




class Contact:
    def __init__(self,id,first_name,last_name,phone,email,id_employer):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.id_employer=id_employer

    def ParseToDicionary(self):
        return {
        'id': self.id,
        'first_name': self.first_name,
        'last_name': self.last_name,
        'phone': self.phone,
        'email':self.email,
        'id_employer':self.id_employer
         }


    def toString(self):
        return  "first name: "+self.first_name+" last name: "+self.last_name

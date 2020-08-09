create database smarti_Test
use smarti_Test; 
create table EMPLOYER (Identifier int NOT NULL AUTO_INCREMENT,Name nvarchar(20) NOT NULL , Phone VARCHAR(11),Email VARCHAR(35),
       PRIMARY KEY (Identifier));
create table Contact (Identifier int NOT NULL AUTO_INCREMENT,First_Name nvarchar(20) , Last_Name VARCHAR(20),Phone VARCHAR(11) ,Email VARCHAR(35),Identifier_employer int NOT NULL,
       PRIMARY KEY (Identifier), FOREIGN KEY (Identifier_employer)
        REFERENCES EMPLOYER(Identifier));
        
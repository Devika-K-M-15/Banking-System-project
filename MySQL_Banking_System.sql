CREATE DATABASE BANKING_SYSTEM;
USE BANKING_SYSTEM;

CREATE TABLE PERSON_DATAS (fullname VARCHAR(30), aadhar_number INT(5) UNIQUE, address VARCHAR(100),
                           Pincode INT(6), Phone_number BIGINT(10), balance INT, account_number INT UNIQUE);
SELECT * FROM PERSON_DATAS;


CREATE TABLE AMOUNT_DETAILS (fullname VARCHAR(30), account_number INT UNIQUE, balance INT);
SELECT * FROM AMOUNT_DETAILS;


CREATE TABLE CUSTOMER_QUERIES (fullname VARCHAR(30), account_number INT UNIQUE, customer_query VARCHAR(500));
SELECT * FROM CUSTOMER_QUERIES;

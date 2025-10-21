# SQL Injection — Writeups & Solved labs
**Category:** Web Security — SQL Injection  
**Disclaimer:** These write-ups document challenges solved on intentionally vulnerable labs (PortSwigger Web Security Academy). Do **not** use these techniques on systems you do not own or have permission to test.


## Lab 01 — Login bypass 
 This lab contains a SQL injection vulnerability in the login function.

To solve the lab, perform a SQL injection attack that logs in to the application as the administrator user. 

![image alt](https://github.com/GERRY-01/Cybersecurity-Projects-/blob/main/Cybersec/SQLinjection/Lab1%20Quiz.png?raw=true)

## Solution
To solve this lab, inject the following payload :
### username => admin' OR '1'='1'-- 
### password => anything

The resulting SQL becomes:
```
SELECT * FROM users WHERE username = 'admin' OR '1'='1'--' AND password = 'anything';
```
## Explanation
admin' — the extra single quote (') closes the username text the app expected.

OR '1'='1' — this part is always true (1 = 1). Because it’s joined with OR, the whole login check becomes true even if the username/password are wrong.

-- — this makes the rest of the SQL statement into a comment, so the password check is ignored.

So the password check gets skipped and the database may return a user row (often the admin), letting you log in without the correct password.

![image alt](https://github.com/GERRY-01/Cybersecurity-Projects-/blob/main/Cybersec/SQLinjection/Lab1%20Solution.png?raw=true)

## Lab 02 - Retrieval of hidden data in a Database
This lab contains a SQL injection vulnerability in the product category filter. When the user selects a category, the application carries out a SQL query like the following: 
```
SELECT * FROM products WHERE category = 'Gifts' AND released = 1
```
To solve the lab, we need to perform a SQL injection attack that causes the application to display one or more unreleased products. 

This is the lab 

![image alt](https://github.com/GERRY-01/Cybersecurity-Projects-/blob/main/Cybersec/SQLinjection/Screenshot%20from%202025-10-20%2023-55-06.png?raw=true)

At the moment the lab displays only released products. We want to perform SQL injection so that it can dispaly all products irregardless of whether they are released or not

## Solution
To solve this lab, you can use burpsuit or you can just make changes in the address bar. For instance, if I select the Gift Category. Look at how my address bar is 

![image alt](https://github.com/GERRY-01/Cybersecurity-Projects-/blob/main/Cybersec/SQLinjection/Screenshot%20from%202025-10-21%2000-35-40.png?raw=true)

I can just inject a query in the addressbar like this
```
category=Corporate gifts' OR 1=1--
```
This will result to an SQL query:
```
SELECT * FROM products WHERE category = 'Corporate gifts' OR 1=1--';
```
## What it does 

Corporate gifts' — the extra ' closes the category text the app expected.

OR 1=1 — this always returns true, so the filter matches every row.

-- — makes the rest of the query a comment hence ignoring the released part. So all the products will be retrieved, irregardless of whether they are released or not


## Lab 03 - SQL injection UNION attack to retrieve data from other tables

![image alt](https://github.com/GERRY-01/Cybersecurity-Projects-/blob/main/Cybersec/SQLinjection/Screenshot%20from%202025-10-21%2015-09-06.png?raw=true)

## Solution
This lab requires as to retrieve data(usernames and passwords) from the **users** table. Since we have a vulnerability
in the category filter, we can use union attack to combine the SQL query for the category filter and for users table. By doing this, all the usernames and passwords will be retrieved

1. To perform UNION attack, first you need to know the number of columns in a table. UNION is simply combining 2 SELECT statements. In this case we are combining the categories table and the users table. One of the condition necessary to perform UNION attack is that, the first table should have the same number of columns as the second table
2. Secondly, we need to know the data type of the various columns.
3. We can now do the UNION attack

This is the lab when you access it
![image alt](https://github.com/GERRY-01/Cybersecurity-Projects-/blob/main/Cybersec/SQLinjection/Screenshot%20from%202025-10-21%2015-21-44.png?raw=true)

## Step 1: Identifying the number of columns in the category table
we can achieve this by injecting this payload 
## category=pets' UNION SELECT NULL--
At first you may get an error.
Since UNION cn only be achieved when the number of columns of the first table corresponds with the number of columns in the second table, we will keep on incrementing "NULL" till we get no error ie

## category=pets' UNION SELECT NULL,NULL--

![image alt](https://github.com/GERRY-01/Cybersecurity-Projects-/blob/main/Cybersec/SQLinjection/Screenshot%20from%202025-10-21%2015-31-33.png?raw=true)

 we got no error, which means the category table has 2 columns.

## Step 2: Identifying the data type of each column
This can be achieved by replacing each **NULL** by any string, if it throws an error, that means that column is not a string. If it doesn't throw an error, that means that the column is a string.
Let's Start with the first one 
### category=pets' UNION SELECT 'abc',NULL--   
we replaced the first NULL with any string

we didn't get any error, meaning the first column accept the string data type

![image alt](https://github.com/GERRY-01/Cybersecurity-Projects-/blob/main/Cybersec/SQLinjection/Screenshot%20from%202025-10-21%2015-38-54.png?raw=true)

let's try it with the second column
### category=pets' UNION SELECT NULL, 'abc'--
we replaced the second NULL with 'abc' to test if it can accept string data type

![image alt](https://github.com/GERRY-01/Cybersecurity-Projects-/blob/main/Cybersec/SQLinjection/Screenshot%20from%202025-10-21%2015-43-19.png?raw=true)

No error, meaning column 2 also accept string

## step 3: Doing the UNION attack
Now that we know the number of columns and the data types. We can actually do the union attack. We want to get all the usernames and passwords from the user table. We can only achieve this by injecting a payload that will return them. SO we'll do UNION attack

This is the **payload** 

```
category=pets' UNION SELECT,username,password FROM users--
```
By doing this I was able to retreieve username and password of the administratot. So I can now login as the admin

![image alt](https://github.com/GERRY-01/Cybersecurity-Projects-/blob/main/Cybersec/SQLinjection/Screenshot%20from%202025-10-21%2015-50-48.png?raw=true)

 I will just go to My account enter the username and Password and I have solved the lab
 

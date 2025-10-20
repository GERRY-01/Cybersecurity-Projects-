# SQL Injection — Writeups & Solved labs
**Category:** Web Security — SQL Injection  
**Disclaimer:** These write-ups document challenges solved on intentionally vulnerable labs (PortSwigger Web Security Academy). Do **not** use these techniques on systems you do not own or have permission to test.


## Lab 01 — Login bypass (error-based)
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

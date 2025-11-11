## Web Enumeration
It invlolves gathering detailed information about a target web server or a web application

### Directory/File Enumeration
We will use **Gobuster** and run this command 

#### gobuster dir -u <url> -w <wordlist>

To get the wordlist you can 
```
git clone https://github.com/danielmiessler/SecLists
```
or 
```
sudo apt install seclists-y
```
### DNS Subdomain Enumeration
We can use GoBuster to enumerate available subdomains of a given domain using the dns flag to specify DNS mode

we run this command 
```
gobuster dns -d inlanefreight.com -w /usr/share/SecLists/Discovery/DNS/namelist.txt
```
-d rep the domain name  -w rep wordlist

### Banner grabbing
we can use this command
```
curl -IL https://www.inlanefreight.com
```
### whatweb
We can extract the version of web servers, supporting frameworks, and applications using the command-line tool whatweb.
You run this command

```
whatweb <url>
```

### Source code
It is also worth checking the source code for any web pages we come across. We can hit [CTRL + U] to bring up the source code window in a browser. 

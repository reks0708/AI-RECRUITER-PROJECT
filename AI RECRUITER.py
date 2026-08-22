import json
import mysql.connector

resume_input=input("Enter the resume info: ")
print("input received")
list=resume_input.split()

extracted_data={"skills":[],"technologies":[],"languages":[]}
mycon=mysql.connector.connect(host="localhost",user="root",password="reks",database="recruiter",use_pure=True)
c=mycon.cursor()
print("Successfully connected")

s1="Select * from skills"
c.execute(s1)
r1=c.fetchall()
skills=[row[0] for row in r1]

s2="Select * from technologies"
c.execute(s2)
r2=c.fetchall()
technologies=[row[0] for row in r2]

s3="Select * from languages"
c.execute(s3)
r3=c.fetchall()
languages=[row[0] for row in r3]

for i in list:
    if i.lower() in skills:
        extracted_data["skills"].append(i)
    if i.lower() in technologies:
        extracted_data["technologies"].append(i)
    if i.lower() in languages:
        extracted_data["languages"].append(i)

print(extracted_data)

c.close()
mycon.close()
    



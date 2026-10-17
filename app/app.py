import os
import time

name = os.getenv("STUDENT_NAME", "Yeldos")
surname = os.getenv("STUDENT_SURNAME", "Taipakov")
group = os.getenv("STUDENT_GROUP", "IT2-2310")
student_id = os.getenv("STUDENT_ID", "38321")

print("================================", flush=True)
print("DevOps Student Application", flush=True)
print("================================", flush=True)

print("Name:", name, flush=True)
print("Surname:", surname, flush=True)
print("Group:", group, flush=True)
print("Student ID:", student_id, flush=True)

print("Application is running successfully!", flush=True)

while True:
    time.sleep(60)

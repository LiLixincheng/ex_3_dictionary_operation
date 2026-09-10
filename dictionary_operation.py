```python
student = {
    "name": "Alice Wong",
    "student_id": "ST1024",
    "age": 21,
    "program": "Software Engineering",
    "city": "Nanjing",
    "gpa": 3.6
}

for key, value in student.items():
    print(f"{key.replace('_', ' ').title()}: {value}")

if "email" not in student:
    student["email"] = input("Enter your email: ").strip()

new_city = input("Enter your new city: ").strip()
while new_city == "":
    print("City cannot be empty.")
    new_city = input("Enter your new city: ").strip()
student["city"] = new_city

phone = student.get("phone")
if phone is None:
    print("Phone number not found.")
    phone = input("Enter your phone number: ").strip()

student["contact"] = {
    "phone": phone,
    "email": student["email"]
}

student["courses"] = {
    "Python": 88,
    "Databases": 91,
    "Software Engineering": 84
}

total_score = 0
course_count = 0

for score in student["courses"].values():
    total_score += score
    course_count += 1

student["average_score"] = total_score / course_count

if student["average_score"] >= 90:
    student["academic_status"] = "Excellent"
elif student["average_score"] >= 75:
    student["academic_status"] = "Good"
elif student["average_score"] >= 60:
    student["academic_status"] = "Pass"
else:
    student["academic_status"] = "At Risk"

course_name = input("Enter a course name to search: ").strip()

if course_name in student["courses"]:
    print(f"{course_name}: {student['courses'][course_name]}")
else:
    print("Course not found")

course_name = input("Enter a course name to update: ").strip()

if course_name in student["courses"]:
    while True:
        try:
            new_score = float(input("Enter the new score (0–100): "))
            if 0 <= new_score <= 100:
                break
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

    old_score = student["courses"][course_name]
    student["courses"][course_name] = new_score
    print(f"{course_name} score updated from {old_score:g} to {new_score:g}.")
else:
    print("Course not found")

total_score = 0
course_count = 0

for score in student["courses"].values():
    total_score += score
    course_count += 1

student["average_score"] = total_score / course_count

if student["average_score"] >= 90:
    student["academic_status"] = "Excellent"
elif student["average_score"] >= 75:
    student["academic_status"] = "Good"
elif student["average_score"] >= 60:
    student["academic_status"] = "Pass"
else:
    student["academic_status"] = "At Risk"

print("\n    STUDENT RECORD")
print("=" * 37)
print(f"\nName: {student['name']}")
print(f"Student ID: {student['student_id']}")
print(f"Age: {student['age']}")
print(f"Program: {student['program']}")
print(f"City: {student['city']}")
print(f"GPA: {student['gpa']}")

print("\nCONTACT")
print(f"Phone: {student['contact']['phone']}")
print(f"Email: {student['contact']['email']}")

print("\nCOURSE RESULTS")
for course, score in student["courses"].items():
    print(f"{course}: {score:g}")

print(f"\nAverage Score: {student['average_score']:.1f}")
print(f"Academic Status: {student['academic_status']}")
print("\n" + "=" * 37)
```

===================================== """


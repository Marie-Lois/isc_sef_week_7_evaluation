students = ["John", "Emma", "Micheal", "Sophia"]
with open("students.txt", "w") as file:
    for student in students:
        file.write(student)
with open("students.txt", "r") as file:
    contents = file.read()
    print(contents)
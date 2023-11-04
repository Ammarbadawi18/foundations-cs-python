student_data = [
  {
      "ID": 1,
      "Name": "Ammar",
      "Age": 20,
      "Major": "Computer Science",
      "GPA": 3.7
  },
  {
      "ID": 2,
      "Name": "kamel",
      "Age": 21,
      "Major": "Engineeridng",
      "GPA": 3.9
  }
]
student_data1 = [
  {
      "ID": 1,
      "Name": "testtt",
      "Age": 20,
      "Major": "Computer Science",
      "GPA": 3.7
  },
  {
      "ID": 2,
      "Name": "test",
      "Age": 21,
      "Major": "Engineering",
      "GPA": 3.9
  }
]

def get_student_by_id(data, student_id):
  for student in data:
      if student["ID"] == student_id:
          return student
  return None

def get_all_students(data):
  return data

def get_students_by_major(data, major):
  filtered_students = []

  for student in data:
   if student["Major"] == major:
      filtered_students.append(student)
  return filtered_students

def add_student(data, student_id, name, age, major, gpa):
  new_student = {
      "ID": student_id,
      "Name": name,
      "Age": age,
      "Major": major,
      "GPA": gpa
  }
  data.append(new_student)

def find_common_majors(data, data1):
 majorsIn1 = set()
 majorsIn2 = set()

 for student in data:
     majorsIn1.add(student['Major'])
 for student in data1:
     majorsIn2.add(student['Major'])

 common= set()
 for major in majorsIn1:
     if major in majorsIn2:
         common.add(major)

 return common

def delete_student_by_id(data, student_id):
  for student in data:
    if student["ID"] == student_id:
      data.remove(student)

def calculate_average_gpa(data):
  if not data:
      return 0.0
  total_gpa = sum(student["GPA"] for student in data)
  return total_gpa / len(data)

while True:
  print("- - - - - - - - - - - - - - -")
  print("1. Get Student by ID")
  print("2. Get All Students")
  print("3. Get Students by Major")
  print("4. Add Student")
  print("5. Find Common Majors")
  print("6. Delete Student")
  print("7. Calculate Average GPA")
  print("9. Exit")

  choice = int(input("Enter your choice: "))

  if choice == 1:
      student_id = int(input("Enter the student's ID: "))
      student = get_student_by_id(student_data, student_id)
      if student:
          print(student)
      else:
          print("Student not found.")

  elif choice == 2:
      students = get_all_students(student_data)
      for student in students:
          print(student)

  elif choice == 3:
      major = input("Enter the major: ")
      students = get_students_by_major(student_data, major)
      for student in students:
          print(student)

  elif choice == 4:
      student_id = int(input("Enter student ID: "))
      name = input("Enter student name: ")
      age = int(input("Enter student age: "))
      major = input("Enter student major: ")
      gpa = float(input("Enter student GPA: "))
      add_student(student_data, student_id, name, age, major, gpa)

  elif choice == 5:
      common = find_common_majors(student_data, student_data1)
      print("Common majors: ", common)

  elif choice == 6:
      student_id = int(input("Enter the student's ID to delete: "))
      delete_student_by_id(student_data, student_id)

  elif choice == 7:
      average_gpa = calculate_average_gpa(student_data)
      print("Average GPA: {:.2f}".format(average_gpa))

  elif choice == 9:
      print("Exiting the program.")
      break

  else:
      print("Invalid choice. Please try again.")

students = {
    "Amit": {"Math": 85, "Science": 78, "English": 90},
    "Neha": {"Math": 92, "Science": 88, "English": 95},
    "Raj": {"Math": 70, "Science": 75, "English": 80}
}
total_marks = {}
for name, marks in students.items():
    total_marks[name] = sum(marks.values())
  
sorted_students = sorted(total_marks.items(), key=lambda x: x[1], reverse=True)

print("Student Ranking:")
for name, total in sorted_students:
    print(name, "->", total)

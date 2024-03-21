marks = {
    "Алексеев Данил": [8, 8, 10],
    "Крылов Сергей": [2, 5, 2],
    "Тихонова Амина": [10, 11, 12],
    "Дмитриев Григорий": [12, 7, 8],
    "Волкова Ульяна": [5, 12, 11]
}


average_marks = {}
for student, marks_list in marks.items():
    average_marks[student] = sum(marks_list) / len(marks_list)


max_average = max(average_marks.values())
min_average = min(average_marks.values())
top_student = [student for student, avg in average_marks.items() if avg == max_average]
worst_student = [student for student, avg in average_marks.items() if avg == min_average]


print(f"Самый успешный студент: {top_student[0]} со средним баллом {max_average}")
print(f"Самый слабый студент: {worst_student[0]} со средним баллом {min_average}")

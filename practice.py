gpa_all_students = {}

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_list = list(sorted(students))

sum_grades_1 = sum(grades[0]) / 5
sum_grades_2 = sum(grades[1]) / 4
sum_grades_3 = sum(grades[2]) / 4
sum_grades_4 = sum(grades[3]) / 3
sum_grades_5 = sum(grades[4]) / 5

gpa_all_students.update({students_list[0]:sum_grades_1,
                         students_list[1]:sum_grades_2,
                         students_list[2]:sum_grades_3,
                         students_list[3]:sum_grades_4,
                         students_list[4]:sum_grades_5})

print(gpa_all_students)
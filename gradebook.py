# gradebook.py

# Display the average of each student's grade.
# Display the average for each assignment.

from itertools import islice

gradebook = [[61, 74, 69, 62, 72, 66, 73, 65, 60, 63, 69, 63, 62, 61, 64],
             [73, 80, 78, 76, 76, 79, 75, 73, 76, 74, 77, 79, 76, 78, 72],
             [90, 92, 93, 92, 88, 93, 90, 95, 100, 99, 100, 91, 95, 99, 96],
             [96, 89, 94, 88, 100, 96, 93, 92, 94, 98, 90, 90, 92, 91, 94],
             [76, 76, 82, 78, 82, 76, 84, 82, 80, 82, 76, 86, 82, 84, 78],
             [93, 92, 89, 84, 91, 86, 84, 90, 95, 86, 88, 95, 88, 84, 89],
             [63, 66, 55, 67, 66, 68, 66, 56, 55, 62, 59, 67, 60, 70, 67],
             [86, 92, 93, 88, 90, 90, 91, 94, 90, 86, 93, 89, 94, 94, 92],
             [89, 80, 81, 89, 86, 86, 85, 80, 79, 90, 83, 85, 90, 79, 80],
             [99, 73, 86, 77, 87, 99, 71, 96, 81, 83, 71, 75, 91, 74, 72]]

def get_stu_avg(gradebook):
    assignments = len(gradebook[0])
    students = len(gradebook)

    stu_grade = list()

    row = 0
    while row < students:
        stu_grade.append(sum(gradebook[row]))
        row += 1

    stu_avg = list()

    student = 0
    while student < students:
        avg = stu_grade[student] / assignments
        stu_avg.append(avg)
        student += 1

    final_stu_avg = list()

    grade_count = 0
    for grade_count in stu_avg:
        final_stu_avg.append(float(grade_count))

    print("Student Averages:")
    people = 0
    while people < students:
        final_stu_avg[people] = "%.2f" % final_stu_avg[people]
        print(final_stu_avg[people])
        people += 1

def get_assignment_avg(gradebook):

    assignments = len(gradebook[0])
    students = len(gradebook)

    assignment_grade = list()

    index = 0
    while index < assignments:
        for row in gradebook:
            element_in_column_2 = row[index]
            assignment_grade.append(element_in_column_2)
        index += 1

    a = students

    length_to_split = [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a]
  
    # Using islice
    Inputt = iter(assignment_grade)
    assignment_grade = [list(islice(Inputt, elem))
          for elem in length_to_split]

    assignment_total = list()

    column = 0
    while column < assignments:
        assignment_total.append(sum(assignment_grade[column]))
        column += 1

    assignment_avg = list()

    assignment_num = 0
    while assignment_num < assignments:
        avg = assignment_total[assignment_num] / students
        assignment_avg.append(avg)
        assignment_num += 1

    final_assignment_avg = list()

    assignment_count = 0
    for assignment_count in assignment_avg:
        final_assignment_avg.append(float(assignment_count))

    print("Assignment Averages:")

    assignment = 0
    while assignment < assignments:
        final_assignment_avg[assignment] = "%.2f" % final_assignment_avg[assignment]
        print(final_assignment_avg[assignment])
        assignment += 1

    print("")

    
def main():
    get_assignment_avg(gradebook)
    get_stu_avg(gradebook)


main()






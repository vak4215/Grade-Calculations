
def math241h():
    # Component: Exam 1 ; Percent of Final Grade: 20%
    exam_1_current = 18.37 / 20.0 # Final
    exam_1 = exam_1_current * 20

    # Component: Exam 2 ; Percent of Final Grade: 24%
    exam_2_current = float(22.5/24) # Final
    exam_2 = exam_2_current * 24

    # Component: Exam 3 ; Percent of Final Grade: 20%
    exam_3_current = float(0.784)
    exam_3 = exam_3_current * 20

    # Component: HW & Projects ; Percent of Final Grade: 18%
    #      23 lesson homeworks : x/3 each
    #      5 matlab : x/10 each
    elements = [1.00] * 28

    elements[3] = 2.7 / 3.0 # Final : lesson 4
    elements[5] = 2.9 / 3.0 # Final : lesson 6
    elements[9] = 2.9 / 3.0 # Final : lesson 10
    elements[10] = 2.9 / 3.0 # Final : lesson 11
    elements[11] = 2.9 / 3.0 # Final : lesson 12
    elements[12] = 2.7 / 3.0 # Final : lesson 13
    elements[16] = 2.8 / 3.0 # Final : lesson 17
    elements[18] = 2.9 / 3.0 # Final : lesson 19
    elements[20] = 2.9 / 3.0 # Final : lesson 21
    elements[22] = 2.8 / 3.0 # Final : lesson 23
    elements[23] = 9.9 / 10.0 # Final : matlab 3

    # grades final through L23 and M5

    sum = 0

    for i in range(0,28):
        sum += elements[i]

    hw_projects_current = sum / 28.0
    hw_projects = hw_projects_current * 18

    # Component: Quizzes ; Percent of Final Grade: 18%
    quiz_1 = (9.0 + 9.0) / (9.0 + 15.0) # Final
    quiz_2 = (15.0 + 4.9) / 20.0 # Final
    quiz_3 = 4.9 / 5.0 # Final
    quiz_4 = 15.5 / 17.0 # Final
    quiz_5 = .85 # Final
    quiz_6 = .95 # Final
    quiz_7 = (9.4+10)/20.0 # Final
    quizzes_current = (quiz_1 + quiz_2 + quiz_3 + quiz_4 + quiz_5 + quiz_6 + quiz_7)/(7)
    quizzes = quizzes_current * 18

    grade = exam_1 + exam_2 + exam_3 + hw_projects + quizzes

    if grade >= 93:
        grade_letter = "A"
    elif grade >= 90:
        grade_letter = "A-"
    else:
        grade_letter = "Not an A"

    print("math 241H grade: " + str(round(grade, 2)) + "%  ~  " + grade_letter)
    print("math 241H grade with 1 extra cred (guaranteed): " + str(round(grade +2, 2)) + "%")
    print("math 241H grade with 3 extra cred (completed): " + str(round(grade +6, 2)) + "%")

def swen262():
    # Component: Midterm Exam 1 ; Percent of Final Grade: 10%
    exam_1_current = float(0.7946) # Final
    exam_1 = exam_1_current * 10

    # Component: Midterm Exam 2 ; Percent of Final Grade: 10%
    exam_2_current = float(1.0) # Final
    exam_2 = exam_2_current * 10

    # Component: Final Exam ; Percent of Final Grade: 20%
    final_exam_current = float(0.90)
    final_exam = final_exam_current * 20

    # Component: Mini Design ; Percent of Final Grade: 10%
    mini_1 = 1.0 # Final
    mini_2 = 1.0 # Final
    quick_design = mini_1 * 5 + mini_2 * 5

    # Component: Design Project R1 ; Percent of Final Grade: 17.5%
    design_R1_current = float(0.846) # Final
    design_R1 = design_R1_current * 17.5

    # Component: Design Project R2 ; Percent of Final Grade: 17.5%
    design_R2_current = float(18.1 / 17.5) # Final
    design_R2 = design_R2_current * 17.5

    # Component: Refactoring Project ; Percent of Final Grade: 5%
    refactor_project_current = float(4.37/5)
    refactor_project = refactor_project_current * 5

    # Component: Activities ; Percent of Final Grade: 10%
    activity = [1.00] * 31
    activity[0] = 0.8865 # Course Overview Quiz
    activity[1] = 0.9 # Decorator Quiz
    activity[2] = 0.9048 # Visitor Quiz
    activity[3] = 0.88 # R2 Planning
    
    """ type1 = [1.00] * 26

    type1[0] = 0.8865 # Course Overview Quiz
    type1[1] = 0.9 # Decorator Quiz
    type1[2] = 0.9048 # Visitor Quiz
    type1[3] = 0.88 # R2 Planning

    type2 = [1.00] * 2

    type3 = [1.00] * 3

    total = 0.0
    achieved = 0.0

    for grade in type1:
        total += 100.0
        achieved += grade * 100.0

    for grade in type2:
        total += 10.0
        achieved += grade * 10.0

    for grade in type3:
        total += 5.0
        achieved += grade * 5.0 """
    
    total = 31
    achieved = 0

    for grade in activity:
        achieved += grade

    activities_current = achieved / total#float(0.945)
    print("activities current : ", activities_current)
    activities = activities_current * 10

    grade = exam_1 + exam_2 + final_exam + quick_design + design_R1 + design_R2 + refactor_project + activities

    if grade >= 93:
        grade_letter = "A"
    elif grade >= 90:
        grade_letter = "A-"
    else:
        grade_letter = "Not an A"

    print("swen 262 grade: " + str(round(grade, 2)) + "%  ~  " + grade_letter)

def physics():
    # Daily Checks (in class)
    daily_checks = 0.08 * (9.7/10)

    # In-Class Problem Sets (in class) 
    problem_sets = 0.04 * (10/10)

    # Expert TA Homework (at home)
    expert_ta = 0.08 * (9.7/10)

    # Labs (in class) 
    labs = 0.12 * (10.0/10)

    # Video Notes (at home) 
    video_notes = .04 * (5/5)

    exam_1 = 0.16 * (100/100) # Final
    exam_2 = 0.16 * (96/100)  # Final
    exam_3 = 0.16 * (82/100)
    final_exam = 0.16 * (82/100)

    total = daily_checks + problem_sets + expert_ta + labs + video_notes + exam_1 + exam_2 + exam_3 + final_exam
    total *= 100

    if (total >= 90.0):
        grade_letter = "at least A-"
    else:
        grade_letter = "Not an A"

    print("phys grade: " + str(total) + "%  ~  " + grade_letter)

def french():
    participation = (10.0/10.0) * 10
    homework = (1.00) * 5

    # Written Expression Files (Dossiers d’expression écrite), Reports (Comptes-rendus), and Research Project (Projet de recherche)
    written = (10.0 / 10.0) * 20

    # Reading and Listening Comprehension Questions
    reading1 = 100.0 / 100.0 # FINAL
    reading2 = 100.0 / 100.0 # FINAL
    reading3 = 95.0 / 100.0
    listeningComprehension1 = 100.0 / 100.0  # FINAL
    listeningComprehension2 = 100.0 / 100.0 # FINAL
    listeningComprehension3 = 100.0 / 100.0 # FINAL
    listeningComprehension4 = 100.0 / 100.0 # FINAL

    reading = 15.0 # ((reading1 + reading2 + reading3 + listeningComprehension1 + listeningComprehension2 + listeningComprehension3 + listeningComprehension4) / 7) * 15

    # Oral Evaluations
    oral = (9.8  / 10.0) * 17

    # Chapter Tests, and Quizzes
    ch_test_1 = 47.5 / 53 # FINAL
    ch_test_2 = 53.25 / 56 # FINAL
    ch_test_3 = 58.25 / 62 # FINAL
    ch =  ( (15.99+8)/(17+8) ) *25 #((ch_test_1 + ch_test_2 + ch_test_3) / 3) * 25

    final = (8.0 / 10.0) * 8

    total = participation + homework + written + reading + oral + ch + final

    if total >= 93:
        grade_letter = "A"
    elif total >= 90:
        grade_letter = "A-"
    else:
        grade_letter = "Not an A"

    print("french grade: " + str(total) + "%  ~  " + grade_letter)

def swen256():
    # Component: Midterm Exam 1 ; Percent of Final Grade: 20%
    exam_1_current = 56.0 / 65.0 # Final
    exam_1 = exam_1_current * 20

    # Component: Midterm Exam 2 ; Percent of Final Grade: 20%
    exam_2_current = float(1.0) # Final
    exam_2 = exam_2_current * 20

    # Component: Final Exam ; Percent of Final Grade: 20%
    final_exam_current = float(0.83)
    final_exam = final_exam_current * 20

    # Component: Team Project ; Percent of Final Grade: 20%
    team_proj_current = float(19.23 / 20)
    team_proj = team_proj_current * 20

    # Component: Quizzes ; Percent of Final Grade: 10%
    quiz_current = float(1.0)
    quiz = quiz_current * 10

    # Component: Class Activities ; Percent of Final Grade: 10%
    class_activities_current = float(1.0)
    class_activities = class_activities_current * 10

    grade = exam_1 + exam_2 + final_exam + team_proj + quiz + class_activities

    if grade >= 93:
        grade_letter = "A"
    elif grade >= 90:
        grade_letter = "A-"
    else:
        grade_letter = "Not an A"

    print("swen 256 grade: " + str(round(grade, 2)) + "%  ~  " + grade_letter)

def main():
    print('Math 241H :')
    math241h()
    print('\nPhysics :')
    physics()
    print('\nSwen 262 :')
    swen262()
    print('\nFrench :')
    french()
    print('\nSwen 256 :')
    swen256()
    print()

main()

def individual_261():
    # Build and run the Heroes REST API - individual.
    # Setup the REST API build environment - individual
    # Team formation survey - individual                                    NOT FINAL!!!
    # Angular Setup - individual
    # Angular Tutorial: Part 1 - individual
    # Static Code Analysis SETUP - individual
    # Static Code Analysis - individual
    # Course Overview-Individual Quiz
    # Appreciation for Software Development Process Quiz-Individual Quiz
    # Team Formation Quiz-Individual Quiz
    # Appreciation for software architecture-Individual Quiz
    # Sprint planning-Individual Quiz
    # Acceptance testing-Individual Quiz
    # Sequence diagams-Individual Quiz
    a_1_n = 1 * 14
    a_1_d = 1 * 14

    # Defining project requirements - individual
    # Domain analysis - individual
    # Object-oriented design I - individual
    # Individual Retrospective - individual                                 NOT FINAL!!!
    # Unit testing - individual
    # Version control concepts-Individual Quiz
    # Unit Testing-Individual Quiz
    # Sprint retrospective-Individual Quiz
    # Professional responsibility-Individual Quiz
    a_2_n = 2 * 9
    a_2_d = 2 * 9

    # REST API Basics (Spike) -Heroes API - individual Assignment
    a_3_n = 3.4
    a_3_d = 4

    # Angular Tutorial: Spike - individual
    a_4_n = 4
    a_4_d = 4

    # Defining project requirements-Individual Quiz
    a_5_n = 0.55
    a_5_d = 1

    # Backlog refinement and estimation-Individual Quiz
    a_6_n = 0.95
    a_6_d = 1

    total_n = a_1_n + a_2_n + a_3_n + a_4_n + a_5_n + a_6_n
    total_d = a_1_d + a_2_d + a_3_d + a_4_d + a_5_d + a_6_d

    return float(total_n) / total_d

def swen261():
    # Component: Term Project ; Percent of Final Grade: 43%
    term_current = float(28.36 / 30) # Term Project
    team_current = float(13/13) # Team Exercises
    term_project = term_current * 30 + team_current * 13

    # Component: Individual Exercises ; Percent of Final Grade: 22%
    individual_current = individual_261()
    individual_exercises = individual_current * 22

    # Component: Exam 1 ; Percent of Final Grade: 10%
    exam_1_current = float(0.8967)
    exam_1 = exam_1_current * 10

    # Component: Final Exam ; Percent of Final Grade: 25%
    final_current = float(0.91)
    final_exam = final_current * 25

    grade = term_project + individual_exercises + exam_1 + final_exam

    if grade >= 93:
        grade_letter = "A"
    elif grade >= 90:
        grade_letter = "A-"
    else:
        grade_letter = "Not an A"

    print("swen 261 grade: " + str(grade) + "%  ~  " + grade_letter)

def swen344():
    db_project_current = float(15/15) # Final
    db_project = db_project_current * 15

    db_practicum_c = float(1.0) # Final
    db_practicum = db_practicum_c * 15

    backend_project_current = float(15/15) # Final
    backend_project = backend_project_current * 15

    backend_practicum_c = float(1.0) # Final
    backend_practicum = backend_practicum_c * 10

    frontend_project_current = float(15/15)
    frontend_project = frontend_project_current * 15

    frontend_practicum_c = float(0.95)
    frontend_practicum = frontend_practicum_c * 15

    tech_quizzes_c = float(13.5/15)
    tech_quizzes = tech_quizzes_c * 15

    grade = db_project + db_practicum + backend_project + backend_practicum + frontend_project + frontend_practicum + tech_quizzes

    grade_letter = "Not an A"
    if grade > 92:
        grade_letter = "A"
    elif grade > 89:
        grade_leter = "A-"

    print("swen 344 grade: " + str(grade) + "%  ~  " + grade_letter)

def comm():
    resume_cover_letter = (0.92 * 100.0) + (.92 * 50.0)
    mock_interview = .95 * 100.0 #Final

    dp_1 = 1.0 #Final
    dp_2 = 1.0 #Final
    dp_3 = 1.0 #Final
    dp_4 = 1.0 #Final
    dp_5 = 1.0 #Final
    dp_6 = 1.0 #Final
    dp_7 = 1.0 #Final
    dp_8 = 1.0 #Final
    dp_9 = 1.0
    dp_10 = 1.0 #Final
    dp_avg = (dp_1 + dp_2 + dp_3 + dp_4 + dp_5 + dp_6 + dp_7 + dp_8 + dp_9 + dp_10) / 10
    d_p = dp_avg * 100.0

    quiz_1 = 1.0 #Final
    quiz_2 = 19.0/20.0 #Final
    quiz_3 = 19.75/20.0 #Final
    quiz_4 = .93
    quiz_5 = 18.0 / 20.0 # Final
    quiz_avg = (quiz_1 + quiz_2 + quiz_3 + quiz_4 + quiz_5) / 5
    quiz = quiz_avg * 100.0

    elevator_pitch = 0.97 * 100.0 #Final
    business_memo = 0.9 * 100.0
    final_presentation = (.8*50) + (.9*150)
    participation = 1.00 * 150.0 #Final

    grade = resume_cover_letter + mock_interview + d_p + quiz + elevator_pitch + business_memo + final_presentation + participation

    if grade >= 930:
        grade_letter = "A"
    elif grade >= 900:
        grade_letter = "A-"
    else:
        grade_letter = "Not an A"

    print("comm 253 grade: " + str(grade/10) + "%  ~  " + grade_letter)

def calc_avg():
    sum_of_scores = float(0)
    total_value = float(0)

    while True:
        grade = input("Enter grade: ")

        if len(grade.split('/')) < 2:
            break

        score, value = grade.split('/')

        sum_of_scores += float(score)
        total_value += float(value)

    print("Grade Avg = " + str(sum_of_scores/total_value))

def phys():
    daily_checks = 0.1 * (10/10)
    problem_sets = 0.1 * (9.93/10)
    labs = 0.1 * (9.84/10)
    in_class = 0.05 * (5/5)
    video_notes = .05 * (5/5)
    exam_1 = 0.2 * (100/100) # Final
    exam_2 = 0.2 * (100/100) # Final
    final = 0.2 * (80/100)

    total = daily_checks + problem_sets + labs + in_class + video_notes + exam_1 + exam_2 + final
    total *= 100

    if (total >= 90.0):
        grade_letter = "at least A-"
    else:
        grade_letter = "Not an A"

    print("phys grade: " + str(total) + "%  ~  " + grade_letter)

def main():
    # calc_avg()
    swen261()
    print()
    swen344()
    print()
    comm()
    print()
    phys()

main()
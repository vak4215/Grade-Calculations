
def math241h():
    # Component: Exam 1 ; Percent of Final Grade: 20%
    exam_1_current = float(0.8967)
    exam_1 = exam_1_current * 20

    # Component: Exam 2 ; Percent of Final Grade: 24%
    exam_2_current = float(0.8967)
    exam_2 = exam_2_current * 24

    # Component: Exam 3 ; Percent of Final Grade: 20%
    exam_3_current = float(0.945)
    exam_3 = exam_3_current * 20

    # Component: HW & Projects ; Percent of Final Grade: 18%
    hw_projects_current = float(0.945)
    hw_projects = hw_projects_current * 18

    # Component: Quizzes ; Percent of Final Grade: 18%
    quizzes_current = float(0.945)
    quizzes = quizzes_current * 18

    grade = exam_1 + exam_2 + exam_3 + hw_projects + quizzes

    if grade >= 93:
        grade_letter = "A"
    elif grade >= 90:
        grade_letter = "A-"
    else:
        grade_letter = "Not an A"

    print("math 241H grade: " + str(grade) + "%  ~  " + grade_letter)

def swen262():
    # Component: Midterm Exam 1 ; Percent of Final Grade: 10%
    exam_1_current = float(0.8967)
    exam_1 = exam_1_current * 10

    # Component: Midterm Exam 2 ; Percent of Final Grade: 10%
    exam_2_current = float(0.8967)
    exam_2 = exam_2_current * 10

    # Component: Final Exam ; Percent of Final Grade: 25%
    final_exam_current = float(0.945)
    final_exam = final_exam_current * 25

    # Component: Quick Design Problem ; Percent of Final Grade: 5%
    quick_design_current = float(0.945)
    quick_design = quick_design_current * 5

    # Component: Design Project R1 ; Percent of Final Grade: 10%
    design_R1_current = float(0.945)
    design_R1 = design_R1_current * 10

    # Component: Design Project R2 ; Percent of Final Grade: 10%
    design_R2_current = float(0.945)
    design_R2 = design_R2_current * 10

    # Component: Refactoring Project ; Percent of Final Grade: 10%
    refactor_project_current = float(0.945)
    refactor_project = refactor_project_current * 10

    # Component: Refactoring Assignments ; Percent of Final Grade: 5%
    refactor_assignments_current = float(0.945)
    refactor_assignments = refactor_assignments_current * 5

    # Component: Class Activities ; Percent of Final Grade: 15%
    class_activities_current = float(0.945)
    class_activities = class_activities_current * 15

    grade = exam_1 + exam_2 + final_exam + quick_design + design_R1 + design_R2 + refactor_project + refactor_assignments + class_activities

    if grade >= 93:
        grade_letter = "A"
    elif grade >= 90:
        grade_letter = "A-"
    else:
        grade_letter = "Not an A"

    print("swen 262 grade: " + str(grade) + "%  ~  " + grade_letter)


def phys():
    # Daily Checks (in class)
    daily_checks = 0.08 * (10/10)

    # In-Class Problem Sets (in class) 
    problem_sets = 0.04 * (9.93/10)

    # Expert TA Homework (at home)
    expert_ta = 0.08 * (10/10)

    # Labs (in class) 
    labs = 0.12 * (9.84/10)

    # Video Notes (at home) 
    video_notes = .04 * (5/5)

    exam_1 = 0.16 * (100/100)
    exam_2 = 0.16 * (100/100)
    exam_3 = 0.16 * (100/100)
    final_exam = 0.16 * (100/100)

    total = daily_checks + problem_sets + expert_ta + labs + video_notes + exam_1 + exam_2 + exam_3 + final_exam
    total *= 100

    if (total >= 90.0):
        grade_letter = "at least A-"
    else:
        grade_letter = "Not an A"

    print("phys grade: " + str(total) + "%  ~  " + grade_letter)

def main():
    math241h()
    print()
    phys()
    print()
    swen262()

main()
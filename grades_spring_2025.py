def get_grade_letter(grade):
    if grade >= 93:
        grade_letter = "A"
    elif grade >= 90:
        grade_letter = "A-"
    else:
        grade_letter = "Not an A"
    
    return grade_letter

def swen_444() :
    """ 
    Exam 1	12%
    Exam 2	12%
    Final Exam	24%
    Team Project	42%
    UX Critique 10%
    """

    d_0 = 9.75 # /10    # graded
    d_1 = 19.75 # /20   # graded
    d_2 = 20 # /20      # graded
    d_3 = 10 # /10 # graded
    d_4 = 16.5 # /20    # graded
    c_w = 10 # /10      # graded
    d_5 = 19 # /20      # graded
    d_6 = 9 # /10       # graded
    d_7 = 9.5 # /10     # graded
    d_8 = 18 # /20      # graded
    d_9 = 49 # /50

    numerator = d_0 + d_1 + d_2 + d_3 + d_4 + d_5 + d_6 + d_7 + d_8 + d_9 + c_w
    denomenator = 10*5 + 20*5 + 50

    exam_1 = 38/40 # graded
    exam_2 = 0.90
    final_exam = 0.90
    team_project = numerator/denomenator
    ux_critique = (19.75/20) *0.5 + 1.00 *0.5 # first part graded

    grade = exam_1 * 12 + exam_2 * 12 + final_exam * 24 + team_project * 42 + ux_critique * 10
    grade_letter = get_grade_letter(grade)

    print("swen 444 grade: " + str(grade) + "%  ~  " + grade_letter)

def swen_331():
    """
    5%: Quizzes & Activities (Exam 1 practice, Permissions)
    20%: Fuzzer project
    15%: Case Study project
    5%: IPC Project
    5%: Input handling project
    15%: Exam 1
    15%: Exam 2
    20%: Final exam (cumulative)
    """

    # quizzes and activities
    """
    Misuse and Abuse Cases Activity ->  - / 10
    Web Activity ->  - / 10
    Threat Modeling Activity -> - / 10
    CVSS Activity ->  - / 10
    OAuth Activity ->  - / 10
    Case Study Recon Activity ->  - / 10
    Insider Threat Activity ->  - / 10
    File Permissions ->  - / 40
    """
    Misuse = 1.00 * 10           # graded
    Web_Activity= 1.00 * 10      # graded
    # Threat_Modeling = 1.00 * 10 
    CVSS_Activity = 1.00 * 10    # graded
    OAuth_Activity= 1.00 * 10    # graded
    Case_Study = 1.00 * 10       # graded
    Insider_Threat = 1.00 * 10   # graded
    File_Permissions = 1.00 * 40 # graded
    quizzes = (Misuse + Web_Activity + CVSS_Activity + OAuth_Activity + Case_Study + Insider_Threat + File_Permissions) / 100

    # fuzzer project
    """
    Fuzzer Round 1 ->  - / 45
    Fuzzer Round 2 ->  - / 30
    Fuzzer Round 0 ->  - / 25
    """
    round_1 = 1.00 * 45 # graded : 45/45
    round_2 = 1.00 * 30 # graded : 30 / 30
    round_0 = 1.00 * 25 # graded : 25/25
    fuzzer = (round_0 + round_1 + round_2) / (45+30+25)

    # case study project
    """
    Proposal ->  - / 10
    Domain Analysis ->  - / 60
    Design Analysis ->  - / 75
    Presentation ->  - / 35
    """
    proposal = 1.00 * 10 # graded 
    domain = 1.00 * 60 # graded 
    design = 1.00 * 75 # graded 
    present = 1 * 35
    case_study = (proposal + domain + design + present) / (10+60+75+35)
    
    # IPC Project
    """
    IPC Project Assignment -> - / 25
    """
    ipc = 25 / 25               # graded

    input_handling = 48 / 50    # graded

    Exam_1 = 0.90 * 100         # graded
    Exam_1_Takehome = 1.00 * 30 # graded
    e_1 = (Exam_1 + Exam_1_Takehome) / 130

    Exam_2 = (60/75)            # graded
    Final_Exam = 0.87           # out of 150

    total = quizzes * 5 + fuzzer * 20 + case_study * 15 + ipc * 5 + input_handling * 5 + e_1 * 15 + Exam_2 * 15 + Final_Exam * 20
    grade_letter = get_grade_letter(total)

    print("swen 331 grade: " + str(total) + "%  ~  " + grade_letter)

def swen_340():
    """
    In-class activities	10%
    Homework and short projects	20%
    STM32 Projects	30%
    Midterm Exam	20%
    Final Exam	20%
    """
    in_class = 1.00 * 10
    hw = 1.00 * 20
    projects = 1.00 * 30
    midterm = 1.00 * 20
    final = 0.5 * 20

    total = in_class + hw + projects + midterm + final
    grade_letter = get_grade_letter(total)

    print("swen 340 grade: " + str(total) + "%  ~  " + grade_letter)

def math():
    """
    cumulative final exam (30%)
    two midterm exams (20% each)
    homework assignments (30%)
    """

    # hw
    """
    hw 1 part 1 - 10
    hw 1 part 2 - 40
    hw 2 part 1 - 10
    hw 2 part 2 - 40
    hw 3 part 1 - 10
    hw 3 part 2 - 40
    hw 4 part 1 - 10
    hw 4 part 2 - 40
    hw 5 part 1 - 10
    hw 5 part 2 - 40
    hw 6 part 1 - 10
    hw 6 part 2 - 40
    hw 7 part 1 - 10
    hw 7 part 2 - 40
    hw 8 part 1 - 10
    hw 8 part 2 - 40
    hw 9 part 1 - 10
    hw 9 part 2 - 40
    hw 10 part 1 - 10
    hw 10 part 2 - 40
    """
    hw_1_part_1 = 1.00 * 10 #graded
    hw_1_part_2 = 1.00 * 40 #graded
    hw_2_part_1 = 1.00 * 10 #graded
    hw_2_part_2 = (49/50) * 40 #graded
    hw_3_part_1 = 1.00 * 10 #graded
    hw_3_part_2 = (58/60) * 40 #graded
    hw_4_part_1 = 1 * 10 #graded
    hw_4_part_2 = (55/60) * 40 #graded
    hw_5_part_1 = 1 * 10 #graded
    hw_5_part_2 = (57/60) * 40 #graded
    hw_6_part_1 = 1 * 10 #graded
    hw_7_part_2 = (39/40) * 40 #graded
    hw_7_part_1 = 1 * 10 # graded
    hw_8_part_2 = 1.00 * 40 # graded
    hw_8_part_1 = 1 * 10 # graded
    hw_9_part_2 = 1.00 * 40 # graded
    hw_9_part_1 = 1 * 10 # graded
    hw_10_part_2 = (48/50) * 40 # graded
    hw_10_part_1 = 1 * 10 # graded
    hw_11_part_2 = 1 * 40 # graded
    hw = (
        hw_1_part_1 + hw_1_part_2 +
        hw_2_part_1 + hw_2_part_2 +
        hw_3_part_1 + hw_3_part_2 +
        hw_4_part_1 + hw_4_part_2 +
        hw_5_part_1 + hw_5_part_2 +
        hw_6_part_1 + hw_11_part_2 +
        hw_7_part_1 + hw_7_part_2 +
        hw_8_part_1 + hw_8_part_2 +
        hw_9_part_1 + hw_9_part_2 +
        hw_10_part_1 + hw_10_part_2
    ) / (10 * 10 + 10 * 40)
    hw = hw * 30

    midterm_1 = (56/60) * 20 #graded
    midterm_2 = (56/60) * 20 #graded
    final = (56/60) * 30

    total = hw + midterm_1 + midterm_2 + final
    grade_letter = get_grade_letter(total)

    print("math grade: " + str(total) + "%  ~  " + grade_letter)

def dsci() :
    # 70% assignments, 30% project. 

    asnmnt_1 = 1.0 # graded
    asnmnt_2 = 1.0 # graded
    asnmnt_3 = 1.0 # graded
    asnmnt_4 = 1.0 # graded
    asnmnt_5 = 1.0 # graded
    asnmnt_6 = 1.0 # graded
    asnmnt_7 = 1.0 # graded
    asnmnt_8 = 1.0
    asnmnt_9 = 1.0
    asnmnt_10 = 1.0

    asnmnt_total = (asnmnt_1 + asnmnt_2 + asnmnt_3 + asnmnt_4 + asnmnt_5 + asnmnt_6 + asnmnt_7 + asnmnt_8 + asnmnt_9 + asnmnt_10) / 10
    
    project_part_1 = 0.88
    project_part_2 = 0.9

    project_total = project_part_1 *.7 + project_part_2 * .3

    total = 70 * asnmnt_total + 30 * project_total
    grade_letter = get_grade_letter(total)

    print("dsci grade: " + str(total) + "%  ~  " + grade_letter)

def main():
    swen_444()
    print()
    swen_331()
    print()
    swen_340()
    print()
    math()
    print()
    dsci()
    print()

main()
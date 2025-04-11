##################

#프로그램명: grade management program

#작성자: 소프트웨어학부/문서연

#작성일: 2025.04.11

#프로그램 설명: 학생의 성적을 입력 받아 총점, 평균, 학점, 등수 등을 계산 및 출력하는 프로그램

###################
students = {}
subjects = ["영어점수", "C-언어 점수", "파이썬"]
rank = {}

def get_info():
    key = input("학생의 학번: ")
    student = {
        "이름": input("학생의 이름: ")
    }
    for subject in subjects:
        student[subject] = int(input(f"{subject}: "))
    return key, student

def add_student():
    key, student = get_info()
    students[key] = student
    calculate_scores()

def calculate_scores():
    for key, student in students.items():
        student["총점"] = sum(student[subject] for subject in subjects)
        student["평균"] = student["총점"] / len(subjects)
        student["학점"] = get_grade(student["평균"])

def get_grade(avg):
    if avg >= 95: return 'A+'
    elif avg >= 90: return 'A0'
    elif avg >= 85: return 'B+'
    elif avg >= 80: return 'B0'
    elif avg >= 75: return 'C+'
    elif avg >= 70: return 'C0'
    elif avg >= 65: return 'D+'
    elif avg >= 60: return 'D'
    else: return 'F'

def calculate_ranks():
    global rank
    rank.clear()
    sorted_students = sorted(students.items(), key=lambda x: x[1]["총점"], reverse=True)
    for r, (key, student) in enumerate(sorted_students, start=1):
        student["등수"] = r
        rank[r]=key

def print_students():
    print("\n성적관리 프로그램")
    print("=" * 70)
    print("학번      이름      영어  C-언어  파이썬  총점   평균   학점  등수")
    print("=" * 70)
    for i in range(1,len(students)+1):
        key = rank[i]
        student = students[key]
        print(f"{key:<10} {student['이름']:<5} {student['영어점수']:<6} {student['C-언어 점수']:<6} {student['파이썬']:<6} {student['총점']:<6} {student['평균']:<6.2f} {student['학점']:<4} {student.get('등수', ''):<4}")

def remove_student():
    key = input("삭제할 학생의 학번: ")
    if key in students:
        del students[key]
        calculate_scores()
        calculate_ranks()
    else:
        print("학생을 찾을 수 없습니다.")

def search_student():
    key = input("검색할 학생의 학번: ")
    if key in students:
        student = students[key]
        print(f"학번: {key}, 이름: {student['이름']}, 총점: {student['총점']}, 평균: {student['평균']:.2f}, 학점: {student['학점']}, 등수: {student.get('등수', '미정')}")
    else:
        print("학생을 찾을 수 없습니다.")

def sort_students():
    calculate_ranks()
    print_students()

def count_above_80():
    count = sum(1 for student in students.values() if student["평균"] >= 80)
    print(f"80점 이상 학생 수: {count}")

while True:
    print("""
1. 학생 추가
2. 학생 삭제
3. 학생 검색
4. 정렬 및 등수 계산
5. 전체 출력
6. 80점 이상 학생 수 출력
7. 종료
    """)
    choice = int(input("선택: "))
    if choice == 1:
        add_student()
    elif choice == 2:
        remove_student()
    elif choice == 3:
        search_student()
    elif choice == 4 or choice == 5:
        sort_students()
    elif choice == 6:
        count_above_80()
    elif choice == 7:
        break
    else:
        print("올바른 번호를 입력하세요.")

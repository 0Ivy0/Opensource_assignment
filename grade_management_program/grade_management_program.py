##################

#프로그램명: grade management program

#작성자: 소프트웨어학부/문서연

#작성일: 2025.04.11

#프로그램 설명: 학생의 성적을 입력 받아 총점, 평균, 학점, 등수 등을 계산 및 출력하는 프로그램

###################
import sqlite3

# 학생 클래스
class Student:
    subjects = ["영어점수", "C-언어 점수", "파이썬"]

    def __init__(self, student_id, name, scores):
        self.student_id = student_id
        self.name = name
        self.scores = dict(zip(Student.subjects, scores))
        self.total = 0
        self.average = 0.0
        self.grade = ''
        self.rank = None
        self.calculate_scores()

    def calculate_scores(self):
        self.total = sum(self.scores[subject] for subject in Student.subjects)
        self.average = self.total / len(Student.subjects)
        self.grade = self.get_grade()

    def get_grade(self):
        avg = self.average
        if avg >= 95: return 'A+'
        elif avg >= 90: return 'A0'
        elif avg >= 85: return 'B+'
        elif avg >= 80: return 'B0'
        elif avg >= 75: return 'C+'
        elif avg >= 70: return 'C0'
        elif avg >= 65: return 'D+'
        elif avg >= 60: return 'D'
        else: return 'F'

    def __str__(self):
        scores_str = '  '.join(f"{self.scores[s]:<6}" for s in Student.subjects)
        return f"{self.student_id:<10} {self.name:<5} {scores_str} {self.total:<6} {self.average:<6.2f} {self.grade:<4} {self.rank or ''}"


# 학생관리 클래스
class StudentManager:
    def __init__(self):
        self.students = {}
        self.init_db()
        self.load_students_from_db()

    def init_db(self):
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id TEXT PRIMARY KEY,
            name TEXT,
            english INTEGER,
            c_language INTEGER,
            python INTEGER
        )
        """)
        conn.commit()
        conn.close()

    def load_students_from_db(self):
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        for row in rows:
            student_id, name, english, c_lang, python_score = row
            scores = [english, c_lang, python_score]
            student = Student(student_id, name, scores)
            self.students[student_id] = student
        conn.close()
        self.calculate_ranks()

    def save_student_to_db(self, student):
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO students (student_id, name, english, c_language, python)
            VALUES (?, ?, ?, ?, ?)
        """, (
            student.student_id,
            student.name,
            student.scores["영어점수"],
            student.scores["C-언어 점수"],
            student.scores["파이썬"]
        ))
        conn.commit()
        conn.close()

    def delete_student_from_db(self, student_id):
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
        conn.commit()
        conn.close()

    def get_info(self):
        student_id = input("학생의 학번: ")
        name = input("학생의 이름: ")
        scores = [int(input(f"{subject}: ")) for subject in Student.subjects]
        return Student(student_id, name, scores)

    def add_student(self):
        student = self.get_info()
        self.students[student.student_id] = student
        self.save_student_to_db(student)
        self.calculate_ranks()

    def remove_student(self):
        student_id = input("삭제할 학생의 학번: ")
        if student_id in self.students:
            del self.students[student_id]
            self.delete_student_from_db(student_id)
            self.calculate_ranks()
        else:
            print("학생을 찾을 수 없습니다.")

    def search_student(self):
        student_id = input("검색할 학생의 학번: ")
        student = self.students.get(student_id)
        if student:
            print(f"학번: {student.student_id}, 이름: {student.name}, 총점: {student.total}, 평균: {student.average:.2f}, 학점: {student.grade}, 등수: {student.rank or '미정'}")
        else:
            print("학생을 찾을 수 없습니다.")

    def calculate_ranks(self):
        sorted_students = sorted(self.students.values(), key=lambda s: s.total, reverse=True)
        for rank, student in enumerate(sorted_students, start=1):
            student.rank = rank

    def print_students(self):
        self.calculate_ranks()
        print("\n성적관리 프로그램")
        print("=" * 70)
        print("학번      이름      영어  C-언어  파이썬  총점   평균   학점  등수")
        print("=" * 70)
        for student in sorted(self.students.values(), key=lambda s: s.rank or 0):
            print(student)

    def count_above_80(self):
        count = sum(1 for student in self.students.values() if student.average >= 80)
        print(f"80점 이상 학생 수: {count}")

    def run(self):
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
            try:
                choice = int(input("선택: "))
                if choice == 1:
                    self.add_student()
                elif choice == 2:
                    self.remove_student()
                elif choice == 3:
                    self.search_student()
                elif choice == 4 or choice == 5:
                    self.print_students()
                elif choice == 6:
                    self.count_above_80()
                elif choice == 7:
                    break
                else:
                    print("올바른 번호를 입력하세요.")
            except ValueError:
                print("숫자를 입력하세요.")


# 프로그램 실행
if __name__ == "__main__":
    manager = StudentManager()
    manager.run()
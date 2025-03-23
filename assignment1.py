student = [0] * 5
name = [0] * 5
eng = [0] * 5
c = [0] * 5
py = [0] * 5
suum = [0] * 5
average = [0] * 5
grade = [0] * 5
rank = [1] * 5

def scan():
    for i in range(5):
        student[i] = input("학번: ")
        name[i] = input("이름: ")
        eng[i] = int(input("영어: "))
        c[i] = int(input("C-언어: "))
        py[i] = int(input("파이썬: "))

def cal_score():
    for i in range(5):
        suum[i] = eng[i] + c[i] + py[i]
        average[i] = suum[i] / 3

def cal_grade():
    for i in range(5):
        if (average[i] >= 95):
            grade[i] = 'A+'
        elif (average[i] >= 90):
            grade[i] = 'A0'
        elif (average[i] >= 85):
            grade[i] = 'B+'
        elif (average[i] >= 80):
            grade[i] = 'B0'
        elif (average[i] >= 75):
            grade[i] = 'C+'
        elif (average[i] >= 70):
            grade[i] = 'C0'
        elif (average[i] >= 65):
            grade[i] = 'D+'
        elif (average[i] >= 60):
            grade[i] = 'D'
        else:
            grade[i] = 'F'

def cal_rank():
    for i in range(5):
        for j in range(5):
            if (suum[i] > suum[j]):
                rank[i] += 1

def prin():
    print('''
                            성적관리 프로그램         
=========================================================================
학번      이름      영어    C-언어  파이썬  총점    평균    학점   등수
=========================================================================''')
    for i in range(5):
        print("{0:<10} {1:<5} {2:<7} {3:<7} {4:<7} {5:<7} {6:<7} {7:<6} {8:<5}".format(student[i], name[i], eng[i], c[i], py[i], suum[i], average[i], grade[i], rank[i]))
        

scan()
cal_score()
cal_grade()
cal_rank()
prin()
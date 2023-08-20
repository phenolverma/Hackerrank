if __name__ == '__main__':
    if __name__ == '__main__':

        stu_data = []
        stu_name = []
        stu_mark = []
        stu_mark_sorted = []
        final_stu_grade = []
        sorted_sec_grade_stu = []
        count = 1
        for _ in range(int(input())):
            name = input()
            stu_data.append(name)
            score = float(input())
            stu_mark.append(score)
            stu_name.append(name)
            stu_data = []
            stu_mark_sorted = sorted(set(stu_mark))
            count += 1

        for each in range(count - 1):
            if stu_mark_sorted[1] == stu_mark[each]:
                final_stu_grade.append(stu_name[each])

        sorted_sec_grade_stu = sorted(final_stu_grade)

        for each in sorted_sec_grade_stu:
            print(each)


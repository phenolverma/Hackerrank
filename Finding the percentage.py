if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    total = 0
    for each in student_marks[query_name]:
        total = total + each

    print(format(total/3, ".2f"))


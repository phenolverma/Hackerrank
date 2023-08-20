if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

score = list(arr)
soreted_score = sorted(set(score), reverse=True)
runner_up_score = soreted_score[1]
print(runner_up_score)

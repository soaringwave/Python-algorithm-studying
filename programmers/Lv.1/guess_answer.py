def solution(answers):
    answer_dic = {0: [1, 2, 3, 4, 5], 1: [2, 1, 2, 3, 2, 4, 2, 5], 2: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]}
    scores = [0, 0, 0]
    for i in range(len(answers)):
        answer = answers[i]
        if answer == answer_dic[0][i % 5]:
            scores[0] += 1
        if answer == answer_dic[1][i % 8]:
            scores[1] += 1
        if answer == answer_dic[2][i % 10]:
            scores[2] += 1
    print(scores)
    print(scores.index(max(scores)))
    return scores

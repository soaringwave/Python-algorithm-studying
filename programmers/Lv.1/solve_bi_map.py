def solution(n, arr1, arr2):
    for i in range(n):
        arr1[i] = get_bi_str(arr1[i], n)
        arr2[i] = get_bi_str(arr2[i], n)
    result = ['' * n]
    print(result)
    for i in range(n):
        for j in range(n):
            if arr1[i][j] == 0 and arr2[i][j] == 0:
                result[i] += ' '
            else:
                result[i] += '#'
    return result

def get_bi_str(num, n):
    answer = ''
    temp = num
    while temp != 0:
        answer += str(temp % 2)
        temp = temp // 2
    left = n - len(answer)
    if left > 0:
        answer += '0' * left
    return answer[::-1]

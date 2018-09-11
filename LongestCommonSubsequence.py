"""
    Наибольшая общая подпоследовательность

    A, B - массивы чисел одномерные массивы Len(A) == N, Len(B) == M
    Последовательность C - содержит только элементы A и B исх. порядке,
    но возможно не все.
"""


def longest_common_subsequence(A, B):
    F = [[0] * (len(B) + 1) for i in range (len(A) + 1)]
    for i in range (1, len(A) + 1):
        for j in range (1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                F[i][j] = 1 + F[i - 1][j - 1]
            else:
                F[i][j] = max(F[i - 1][j], F[i][j - 1])
    return F[-1][-1]


A = [1, 2, 3, 4, 7, 8]
B = [5, 2, 3, 6, 9]

print(longest_common_subsequence(A, B)) # 2 [2, 3]

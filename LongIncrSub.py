"""
    Нибольшая возрастающая подпоследовательность
    Для отсортированных по возрастаню последовательностей
"""


def longest_increasing_subsequence(A):
    F = [0] * (len(A))
    for i in range (1, len(A)):
        m = 0
        for j in range(0, i):
            if A[i] > A[j] and F[j] > m:
                m = F[j]
            F[i] = m + 1
    print(A)
    print(F)
    return F[-1]


A = [1, 2, 3, 4, 3, 5]
B = [5, 5, 5, 5]
C = [5, 6, 7, 8, 9, 11, 111, 1111]
D = [1, 2, 111, 2, 1, 0] # не отсортирован поэтому и не правильный ответ

print(longest_increasing_subsequence(A))
print(longest_increasing_subsequence(B))
print(longest_increasing_subsequence(C))
print(longest_increasing_subsequence(D))

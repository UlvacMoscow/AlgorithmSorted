""" Слияние двух отсортированных массивов по возростанию в один """

def merge(A:list, B:list):
    C = [0] * (len(A) + len(B)) # создаем список равной длинной двух сливаемых
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    return C


""" Рекурентная функция, массив разбиваеться на левую и правую часть """

def merge_sort(A:list):
    if len(A) <= 1:
        return
    middle = len(A) // 2
    left = [A[i] for i in range(0, middle)]
    right = [A[i] for i in range(middle, len(A))]

    merge_sort(left)
    merge_sort(right)
    C = merge(left, right)
    for i in range(len(A)):
        A[i] = C[i]
    return A


def test_merge():
    list_one = [1, 2, 3, 4, 4, 4]
    list_two = [5, 6, 7, 8, 9]
    print(merge(list_one, list_two))
    if merge(list_one, list_two) == list_one + list_two:
        return print("testcase 1 - ok")
    print("testcase 1 - fail")


def test_merge_sort():
    list_three = [2, 3, 4, 8, 1, 7, 2, 3, 4]
    print(merge_sort(list_three))
    if merge_sort(list_three) == [1, 2, 2, 3, 3, 4, 4, 7, 8]:
        return print("testcase 2 - ok")
    print("testcase 2 - fail")


test_merge()
test_merge_sort()

"""  Сортировка Тони Хоар, случайным элемент массива береться и назначаеться
барьером, например нулевой элемент, и массив бьеться на три части, левая которая меньше, средняя равная барьеру,
и правая больше барьера.
"""


def hoar_sort(A):
    if len(A) <= 1:
        return
    barrier = A[0]
    left = []
    middle = []
    right = []
    for x in A:
        if x < barrier:
            left.append(x)
        elif x == barrier:
            middle.append(x)
        else:
            right.append(x)
    hoar_sort(left)
    hoar_sort(right)
    k = 0
    for x in left + middle + right:
        A[k] = x
        k += 1
    return A


def test_hoar_sort():
    A = [5, 3, 4, 5, 6, 5, 4, 3]
    print(hoar_sort(A))
    if hoar_sort(A) == [3, 3, 4, 4, 5, 5, 5, 6]:
        print("testcase 1 - ok")
        return
    print("testcase 1 - fail")


test_hoar_sort()

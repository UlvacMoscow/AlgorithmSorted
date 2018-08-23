""" Проверка упорядоченности [0,...,n] """


def check_sorted(A:list, ascending = True):
    flag = True
    for i in range(0, len(A) - 1):
        if int(ascending) * 2 - 1 * A[i] >= int(ascending) * A[i + 1]:
            flag = False
            break
    return flag


print(check_sorted([0, 1, 2, 3, 4])) #false
print(check_sorted([0, 2, 2, 3, 4])) #false
print(check_sorted([0, 1, 2, 3, 4])) #false
print(check_sorted([10, 11, 12, 13, 14])) #true
print(check_sorted([14, 11, 10, 9, 4])) #true

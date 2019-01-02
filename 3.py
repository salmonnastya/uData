"""
Задача 3.
Имеется несколько золотых слитков известного веса w1, …, wn. Необходимо распределить слитки в две кучи так, что разность весов этих двух куч будет минимальной.
Исходные данные
Первая строка: количество камней n (1 ≤ n ≤ 20).
Вторая строка: веса камней w1, …, wn (1 ≤ wi ≤ 100 000) — целые, разделённые пробельными символами.
Результат
Минимальная разность весов двух куч.
Ограничения: время - 1 секунда, память - 64 Мб
"""

def read_input():
    n = int(input())
    ws = list(map(int, input().split()))
    return ws

def calcul_sum(array):
    summ = 0
    for i in range(len(array)):
        summ += array[i]
    return summ

def selection_sort(arr, reverse=False):
    m = 0
    while m < len(arr)-1:
        indx = m
        i = m + 1
        while i < len(arr):
            if arr[i] > arr[indx] if reverse else arr[i] < arr[indx]:
                indx = i
            i += 1
        arr[m], arr[indx] = arr[indx], arr[m]
        m += 1
    return arr

def solve_diff(ws, verbose=False):   
    stack_a = []
    stack_b = []
    summ = calcul_sum(ws)
    summ = summ//2
    ws = selection_sort(ws, reverse=True)
    if verbose:
        print("Weights:", ws)
    for w in ws:        
        if sum(stack_a)+ w <= summ:
            stack_a.append(w)
        else:
            stack_b.append(w)
    if verbose:
        print("Stack a:", stack_a)
        print("Stack b:", stack_b)
    return abs(sum(stack_a) - sum(stack_b))

if __name__ == '__main__':
    ws = read_input()
    print(solve_diff(ws))

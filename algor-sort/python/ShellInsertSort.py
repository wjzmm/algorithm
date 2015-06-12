# -*- coding: utf-8 -*-
#希尔排序
def ShellInsertSort(numbers, n, dk):
    for i in xrange(dk, n, 1):
        watcher = numbers[i]
        j = i - dk
        while j >= 0 and watcher < numbers[j]:
            numbers[j+dk] = numbers[j]
            j = j - dk
        numbers[j+dk] = watcher

    print numbers
            
def ShellSort(numbers, n):
    dk = n / 2
    while dk >= 1:
        ShellInsertSort(numbers, n, dk)
        dk = dk / 2

def main():
    numbers = [71,14,51,91,12,18,31,16]
    ShellSort(numbers, len(numbers))

if __name__ == "__main__":
    main()
    

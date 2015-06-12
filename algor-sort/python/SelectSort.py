# -*- coding: utf-8 -*-
#简单选择排序

def minNumber(numbers):
    j = 0
    for i in xrange(0,len(numbers)):
        if numbers[i] < numbers[j]:
            j = i
    #print numbers[j]
    return j

def SelectSort(numbers):
    for i in xrange(0, len(numbers)):
        print numbers[i:]
        minnu = minNumber(numbers[i:])
        
        minnu += i
        if not minnu == i:
            numbers[i],numbers[minnu] = numbers[minnu],numbers[i]
        print numbers

def main():
    numbers = [5,2,9,4,1,7,6,3,8]
    SelectSort(numbers)

if __name__ == "__main__":
    main()

#personal
def InsertSort(numbers):
    for j in xrange(1,len(numbers)):
        #print 'current is ',j
        if numbers[j]<numbers[j-1]:
            i=j-1
            watcher=numbers[j]
            flag=True
            print 'watcher is',watcher
            numbers[j]=numbers[j-1]
            while watcher<numbers[i]:
                flag=True
                numbers[i+1]=numbers[i]
                if i==0:
                    numbers[i]=watcher
                    flag=False
                    break;
                i=i-1
            if flag:
                numbers[i+1]=watcher
        print numbers
# standard
def InsertSortDo(numbers):
    for j in xrange(1,len(numbers)):
        watcher = numbers[j]
        i = j-1
        while i >= 0 and watcher < numbers[i]:
            numbers[i+1] = numbers[i]
            i -= 1
        numbers[i+1] = watcher
    print numbers
def main():
    numbers = [13,11,21,16,41,18,21,19,17]
    InsertSortDo(numbers)

if __name__=='__main__':
    main()

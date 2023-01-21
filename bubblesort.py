# Bubble sort
ulist = []
g = int(input("Input a number ('0' ends collection and sorts): "))

def bubbleSort(ulist):
    for aLength in range(len(ulist)):
        for i in range(0, len(ulist) - aLength - 1):
            if ulist[i] > ulist[i + 1]:
                temp = ulist[i]
                ulist[i] = ulist[i + 1]
                ulist[i + 1] = temp

while True:
    if g != 0:
        g = int(input("Input a number: "))
        ulist.append(g)
    else:
        bubbleSort(ulist)
        print(ulist)
        break
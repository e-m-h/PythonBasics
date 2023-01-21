# Bubble sort
ulist = []
g = ""

def bubbleSort(ulist):
    for aLength in range(len(ulist)):
        for i in range(0, len(ulist) - aLength - 1):
            if ulist[i] > ulist[i + 1]:
                temp = ulist[i]
                ulist[i] = ulist[i + 1]
                ulist[i + 1] = temp

print("'0' ends integer collection and sorts.")
while True:
    try:
        if g != 0:
            g = int(input("Input a number: "))
            ulist.append(g)
        elif g == 0:
            ulist.remove(g)
            bubbleSort(ulist)
            print(ulist)
            break
    except ValueError:
        print("Please input an integer.")
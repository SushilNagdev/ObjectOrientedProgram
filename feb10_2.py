mylist =[5, 10, 15, 20, 45, 35, 40, 2, 50, 34]

def bubblesort():
    global mylist
    n = 10

    for x in range(0,n-1):
        for y in range(0,n-1-x):
            if mylist[y] > mylist[y+1]:
                temp = mylist[y]
                mylist[y] = mylist[y+1]
                mylist[y+1] = temp
bubblesort()

print(mylist)


mylist =[5, 10, 15, 20, 25, 35, 40, 45, 50, 55]

def linearSearch(num):





    global mylist

    found = False
    index = 0

    while found == False and index < 10:
        if num == mylist[index]:
            found = True
        else:
            index = index +1
    if found == True:
        return index
    else:
        return -1
    



def binarySearch(Num):

    global mylist


    top = 0
    bottom = 9
    found = False

    while top<= bottom and found == False:
        middle = int((top+bottom)/2)
        if Num == mylist[middle]:
            found = True
        elif Num > mylist[middle]:
            top= middle +1

        else:
            bottom + middle -1

    if found == True:
        return middle
    else:
        return -1

x = binarySearch(5)


    

if x==-1:
    print("Data not found....")
else:
    print("number found", x)
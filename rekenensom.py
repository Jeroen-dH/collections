listOne = [1,2,3,4,5,6,7,8,9,10]
listTwo = [2,4,6,8,10,12,14,16,18,20]
def addAndDisplayLists(list1,list2):
    print("---------------\nplus lijst")
    for a in range(len(list1)):
        print(list1[a], " + ", list2[a], " = ", list1[a] + list2[a])
def substractAndDisplayLists(list1,list2):
    print("---------------\nmin lijst")
    for a in range(len(list1)):
        print(list1[a], " - ", list2[a], " = ", list1[a] - list2[a])
def multiplyAndDisplayLists(list1,list2):
    print("---------------\nkeer list")
    for a in range(len(list1)):
        print(list1[a], " x ", list2[a], " = ", list1[a] * list2[a])
def divideAndDisplayLists(list1,list2):
    print("---------------\ngedeeld door lijst")
    for a in range(len(list1)):
        print(list1[a], " / ", list2[a], " = ", list1[a] / list2[a])

addAndDisplayLists(listOne,listTwo)
substractAndDisplayLists(listOne,listTwo)
multiplyAndDisplayLists(listOne,listTwo)
divideAndDisplayLists(listOne,listTwo)
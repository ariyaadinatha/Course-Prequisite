import os

path_parent = os.path.dirname(os.getcwd())
os.chdir(path_parent)


def getRow(namaFile):
    filepath = str(os.getcwd())+"/test/"+str(namaFile)
    row = 0
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            row += 1
            line = fp.readline()
    return row


def fileTodaGraph(namaFile):
    filepath = str(os.getcwd())+"/test/"+str(namaFile)
    row = getRow(namaFile)
    arraydaGra = [[] for i in range(row)]
    with open(filepath) as fp:
        line = fp.readline()
        countIndex = 0
        while line:
            striped = (line.rstrip(".\n").split(", "))
            arrayEdges = []
            index = 0
            for content in striped:
                if (index == 0):
                    vertices = content
                    index += 1
                else:
                    arrayEdges.append(content)
            arraydaGra[countIndex] += [[vertices], arrayEdges]
            countIndex += 1
            line = fp.readline()
    return (arraydaGra)


def head(array):
    return array[0]


def tail(array):
    return array[1:]


def isOneElmt(array):
    return len(array) == 1


def isEmpty(array):
    return len(array) == 0


# mencari nilai minimum dari edges
def minArray(array, minimum, index):
    if (minimum > len(head(array)[1])):
        minimum = len(head(array)[1])
        index = 0
    if (isOneElmt(array)):
        if (minimum > len(array[0][1])):
            minimum = len(array[0][1])
        return minimum
    minArray(tail(array), minimum, index)
    return minArray(tail(array), minimum, index)


# Melakukan sorting pada array
def selectionSort(array):
    sortedArray = [[] for i in range(row)]
    indexSort = 0
    while (len(array) != 0):
        minimum = 99
        for i in range(len(array)):
            if minimum > len(array[i][1]):
                minimum = len(array[i][1])
                index = i
        sortedArray[indexSort] = array[index]
        indexSort += 1
        array.remove(array[index])
    return sortedArray


def isTaken(taking, taken):
    for i in taken:
        if (taking == [i]):
            return True
    return False


def takeCourse(array):
    course = [[] for i in range(7)]

    # Mengambil course tanpa syarat
    for i in range(len(array)):
        if len(array[i][1]) == 0:
            course[0] += array[i][0]

    # list course yang sudah diambil
    taken = [elm for index in course for elm in index]
    semester = 1
    totalCourse = len(array)
    while (len(taken) != totalCourse):
        goingToTake = []
        for i in range(len(array))[1:]:
            preq = []
            preq += (array[i][1])
            if all(elmt in taken for elmt in preq):
                if (isTaken(array[i][0], taken) == False):
                    take = (array[i][0])
                    goingToTake += (array[i][0])
        if (isTaken(take, taken) == False):
            taken += goingToTake
            course[semester] += goingToTake
        semester += 1
    return course


# namaFile = input("Masukkan nama file : ")
namaFile = input("Masukkan nama file : ")
row = getRow(namaFile)
array = (fileTodaGraph(namaFile))
sortedDAG = selectionSort(array)
taken = takeCourse(sortedDAG)

for i in range(len(taken)):
    if len(taken[i]) != 0:
        print(f"Semester {i+1} :", end=" ")
        index = 0
        for j in taken[i]:
            if index == len(taken[i])-1:
                print(j)
            else:
                print(j, end=", ")
            index += 1

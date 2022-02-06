import numpy

fig1 = numpy.array([[1, 1, 1, 1],
                    [1, 0, 0, 0]])

fig2 = numpy.array([[1, 1, 1, 1],
                    [0, 1, 0, 0]])

fig3 = numpy.array([[1, 1, 1],
                    [1, 1, 1]])

fig4 = numpy.array([[1, 1, 1],
                    [1, 1, 0]])

fig5 = numpy.array([[1, 1, 1],
                    [1, 0, 1]])

fig6 = numpy.array([[1, 1, 1],
                    [1, 0, 0],
                    [1, 0, 0]])

fig7 = numpy.array([[1, 1, 1, 0],
                    [0, 0, 1, 1]])

fig8 = numpy.array([[1, 1, 0],
                    [0, 1, 0],
                    [0, 1, 1]])

constraints = numpy.array([[0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
                           [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
                           [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
                           [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
                           [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
                           [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
                           [0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])


def getRotations(fig):
    rotations = list()
    rotations.append(fig)
    appendNotDuplicatedRotation(rotations, numpy.rot90(fig, 1))
    appendNotDuplicatedRotation(rotations, numpy.rot90(fig, 2))
    appendNotDuplicatedRotation(rotations, numpy.rot90(fig, 3))

    transposed = numpy.transpose(fig)
    appendNotDuplicatedRotation(rotations, transposed)
    appendNotDuplicatedRotation(rotations, numpy.rot90(transposed, 1))
    appendNotDuplicatedRotation(rotations, numpy.rot90(transposed, 2))
    appendNotDuplicatedRotation(rotations, numpy.rot90(transposed, 3))

    return rotations


def appendNotDuplicatedRotation(list, fig):
    foundDuplicate = False
    for item in list:
        if numpy.array_equal(item, fig):
            foundDuplicate = True
            break

    if not foundDuplicate:
        list.append(fig)


def constrainted(pos):
    res = numpy.add(pos, constraints)
    return numpy.any(res == 2)


def getConstraintedPositions(fig):
    positions = list()
    lens = fig.shape
    for x in range(7):
        for y in range(7):
            pos = numpy.pad(fig, ((x, 10 - x - lens[0]), (y, 10 - y - lens[1])))
            if not constrainted(pos):
                positions.append(pos[0:7, 0:7])
    return positions


positions1 = [item for sublist in [getConstraintedPositions(i) for i in getRotations(fig1)] for item in sublist]
positions2 = [item for sublist in [getConstraintedPositions(i) for i in getRotations(fig2)] for item in sublist]
positions3 = [item for sublist in [getConstraintedPositions(i) for i in getRotations(fig3)] for item in sublist]
positions4 = [item for sublist in [getConstraintedPositions(i) for i in getRotations(fig4)] for item in sublist]
positions5 = [item for sublist in [getConstraintedPositions(i) for i in getRotations(fig5)] for item in sublist]
positions6 = [item for sublist in [getConstraintedPositions(i) for i in getRotations(fig6)] for item in sublist]
positions7 = [item for sublist in [getConstraintedPositions(i) for i in getRotations(fig7)] for item in sublist]
positions8 = [item for sublist in [getConstraintedPositions(i) for i in getRotations(fig8)] for item in sublist]

positions = [positions1, positions2, positions3, positions4, positions5, positions6, positions7, positions8]


def searchRightPositions():
    success = 0
    cnt1 = 0
    for i1 in positions1:
        cnt1 = cnt1 + 1
        cnt2 = 0
        for i2 in positions2:
            cnt2 = cnt2 + 1
            res2 = i1 + i2
            if not numpy.any(res2 > 1):
                cnt3 = 0
                for i3 in positions3:
                    cnt3 = cnt3 + 1
                    res3 = res2 + i3
                    if not numpy.any(res3 > 1):
                        cnt4 = 0
                        for i4 in positions4:
                            cnt4 = cnt4 + 1
                            res4 = res3 + i4
                            if not numpy.any(res4 > 1):
                                cnt5 = 0
                                for i5 in positions5:
                                    cnt5 = cnt5 + 1
                                    res5 = res4 + i5
                                    if not numpy.any(res5 > 1):
                                        cnt6 = 0
                                        for i6 in positions6:
                                            cnt6 = cnt6 + 1
                                            res6 = res5 + i6
                                            if not numpy.any(res6 > 1):
                                                cnt7 = 0
                                                for i7 in positions7:
                                                    cnt7 = cnt7 + 1
                                                    res7 = res6 + i7
                                                    if not numpy.any(res7 > 1):
                                                        cnt8 = 0
                                                        for i8 in positions8:
                                                            cnt8 = cnt8 + 1
                                                            res8 = res7 + i8
                                                            if not numpy.any(res8 > 1):
                                                                success = success + 1
                                                                print(cnt1, cnt2, cnt3, cnt4, cnt5, cnt6, cnt7, cnt8)



def checkSolution(solution):
    res = numpy.zeros((7,7), dtype=int)
    for i in range(len(solution)):
        res = res + positions[i][solution[i] - 1]

    if (numpy.any(res > 1)):
        return False, 0, 0

    months = res[0:2, 0:6]
    test = numpy.sum(res[0:2, 0:6]) == 11
    if test:
        monthIdx = numpy.where(months==0)
        month = monthIdx[0][0] * 6 + monthIdx[1][0] + 1

        days = res[2:7, 0:7]
        dayIdx = numpy.where(days == 0)
        day = dayIdx[0][0] * 7 + dayIdx[1][0] + 1
        # print(month, day)
        return True, month, day
    else:
        return False, 0, 0




def file_reader(file_name):
    for row in open(file_name, "r"):
        yield row

def rowToSolution(row):
    return list(map(int, row.split()))

def solutions():
    for row in file_reader("log.txt"):
        yield rowToSolution(row)

def correct_solutions():
    for solution in solutions():
        (correct, month, day) = checkSolution(solution)
        if (correct):
            yield (month, day, solution)


def analyze():
    solutionCountPerDay = numpy.zeros((12, 31), dtype=int)
    for month, day, solution in correct_solutions():
        solutionCountPerDay[month - 1, day - 1] += 1

    print(solutionCountPerDay)
    flatten = solutionCountPerDay.flatten()
    flatten.sort()
    print(flatten)

    print(numpy.where(solutionCountPerDay == 7))
    print(numpy.where(solutionCountPerDay == 216))
    print(numpy.sum(solutionCountPerDay))




import sys

# Matrix
matrix = []

# Directions
# east = 0
# south = 1
# west = 2
# north = 3


def main():
    if (len(sys.argv) < 2):
        print "> ERROR: You must specify the size of the matrix (one integer)."
        sys.exit(1)
    n = int(sys.argv[1])
    initMatrix(n);
    fillMatrix(0, 0, 0, 0)
    printMatrix()


def initMatrix(n):
    global matrix
    for i in xrange(n):
        matrix.append([])
    for i in xrange(n):
        for j in xrange(n):
            matrix[i].append(None)


def isInRange(pos, n):
    if pos[0] < 0 or pos[1] < 0:
        return False
    if pos[0] >= n or pos[1] >= n:
        return False
    return True


def getNewPos(row, column, direction):
    nextPos = None
    if direction == 0:
        nextPos = (row,column+1)
    elif direction == 1:
        nextPos = (row+1,column)
    elif direction == 2:
        nextPos = (row,column-1)
    else:
        nextPos = (row-1,column)
    return nextPos


def fillMatrix(row, column, direction, number):
    #import pdb; pdb.set_trace()
    global matrix
    # assign number
    matrix[row][column] = number

    # check if terminate
    n = int(sys.argv[1])
    if number == (n**2)-1:
        return

    # find next position
    nextPos = getNewPos(row, column, direction)

    nextDirection = direction
    # check if next position is valid
    if not isInRange(nextPos, n) or matrix[nextPos[0]][nextPos[1]] is not None:
        # Time to change directions
        nextDirection = (direction+1) % 4
        # And calculate new position
        nextPos = getNewPos(row, column, nextDirection)

    # now we have a valid position (in theory)
    fillMatrix(nextPos[0], nextPos[1], nextDirection, number+1)


def printMatrix():
    global matrix
    print ""
    for row in matrix:
        for col in row:
            print "[%d]" % (col),
        print ""


if __name__ == "__main__":
    main()
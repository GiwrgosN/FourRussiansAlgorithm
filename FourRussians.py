"""

This module is an implementation of the Four Russians Algorithm for
matrix multiplication and complementary graph.

One of the main requirements was to implement this algorith without
using any external libraries (use only built in libraries).


Algorithm Description:

The main idea of the method is to partition the matrix into small square
blocks of size t × t for some parameter t, and to use a lookup table to
perform the algorithm quickly within each block.
The index into the lookup table encodes the values of the matrix cells
on the upper left of the block boundary prior to some operation of the
algorithm, and the result of the lookup table encodes the values of the
boundary cells on the lower right of the block after the operation.
Thus, the overall algorithm may be performed by operating on only (n/t)^2
blocks instead of on n^2 matrix cells, where n is the side length
of the matrix. In order to keep the size of the lookup tables
(and the time needed to initialize them) sufficiently small,
t is typically chosen to be O(log n).

PEP 8 Style is being used for this module.

"""

import sys


def hasdecimalnumbers(x: float) -> bool:
    """
    Check if the given number has a decimal point.

    :param x: Input number of type `float`.
    :return: Return True if x has a decimal point otherwise return False
    """
    if x % 1 == 0:
        return False
    else:
        return True


def roundup(x: float) -> int:
    """
    Round given number to the next greater `int`.

    :param x: Input number of type `float`.
    :return: Output rounded number of type `int`.
    """
    if not hasdecimalnumbers(x):
        return int(x)
    else:
        return int(x+1)


def rounddown(x: float) -> int:
    """
    Round given number to the previous `int`.

    :param x: Input number of type `float`.
    :return: Output rounded number of type `int`.
    """
    if not hasdecimalnumbers(x):
        return int(x)
    else:
        return int(x)


def log_22(x: int) -> float:
    """
    Calculate log with base = 2 for big numbers (>10000)

    :param x: Input number of type `int`.
    :return: log2(x) of type `float`.
    """
    result = 0
    step = x / float(100000000)
    while x > (2 ** result):
        previously = result
        result += step
    return previously


def log_2(x: int) -> float:
    """
    Calculate log2(x) for both small and large numbers.

    :param x:  Input number of type `int`.
    :return: log2(x) of type `float`.
    """
    if x > 1000:  # We use the "if" case so that we get quicker results if "n" is a big number
        return log_22(x)
    else:
        result = 0
        while x != int(round(2**result, 3)):
            result += 0.001
        return result


sys.stderr.flush()
input_ = sys.argv
Apath = input_[1]
Bpath = []

if len(input_) == 2:
    Bpath.append("Notgiven")
else:
    Bpath.append(input_[2])

A = []  # Matrix A
B = []  # Matrix B
n = 0

# If the user gives two inputs we read B matrix as well
if Bpath[0] != "Notgiven":
    with open(Bpath[0]) as f:
        for line in f:
            line = line.split(',')
            if line:
                line = [int(i) for i in line]
                B.append(line)
    # We read A matrix
    with open(Apath) as f:
        for line in f:
            n = n+1
            line = line.split(',')
            if line:
                line = [int(i) for i in line]
                A.append(line)

# First we implement AxB
if Bpath[0] != "Notgiven":
    C = [[0 for x in range(n)] for y in range(n)]
    # First we need to check if n is divided by logn in order to use our algorythm
    m = log_2(n)
    m = rounddown(m)
    # We add a zero column to A matrix and a zero row for B matrix
    n2 = n
    while (n2 % m != 0) & (n != 3):
        n2 = n2+1
        Anew = [[0 for x in range(n2)] for y in range(n)]
        Bnew = [[0 for x in range(n)] for y in range(n2)]
    # We copy our data to the new matrixes
    # First for A matrix and then for B ( if it is given from the user )
    for i in range(0, n):
        for j in range(0, n):
            Anew[j][i] = A[j][i]

    if Bpath[0] != "Notgiven":
        for i in range(0, n):
            for j in range(0, n):
                Bnew[j][i] = B[j][i]
    # We use the algorythm
    limit = roundup(n / m) + 1
    for i in range(1, limit):
        rs = [[0 for x in range(n)] for y in range(2**m)]
        bp = 1
        k = 0
        if 2 ** m - 2 == 0:
            m = m + 1

        for j in range(1, (2**m)):
            # Binary sum
            a = Bnew[i*m-(k+1)]
            b = rs[j-(2**k)]
            sum_list = []
            for z in range(0, n):
                if a[z] + b[z] == 2:
                    sum_list.append(1)
                else:
                    sum_list.append(a[z] + b[z])
            rs[j] = sum_list
            if bp == 1:
                bp = j+1
                k = k+1
            else:
                bp = bp-1
        TempC = [[0 for x in range(n)] for y in range(n)]
        for j in range(0, n):
            number = ''
            # We find the binary number
            sublist = Anew[j]
            m1 = log_2(n)
            m1 = rounddown(m1)
            m = m1
            for h in range((i-1)*m1, i*m1):
                number = number + str(sublist[h])
            decimal_Numb = int(number, 2)
            TempC[j] = rs[decimal_Numb]
        # update C matrix
        for h in range(0, n):
            # we take each row
            a = C[h]
            b = TempC[h]
            sum_list = []
            for l in range(0, n):
                if a[l] + b[l] == 2:
                    sum_list.append(1)
                else:
                    sum_list.append(a[l] + b[l])

            C[h] = sum_list
    for j in range(0, n):
        row = C[j]
        Crow = ','.join(map(str, row))
        print(Crow)

if Bpath[0] == "Notgiven":
    n = 0
    # in this case we have only A matrix which represents our graph
    # first we have to find the dimension n of the matrix
    numbers1 = []  # the list with all the numbers we are going to read
    numbers2 = []  # list with the numbers we have found so far
    with open(Apath) as f:
        for line in f:
            line = line.split(' ')
            if line:
                line = [int(i) for i in line]
                newNumber = line
                numbers1.append(newNumber[0])
                numbers1.append(newNumber[1])

    for j in range(0, len(numbers1)):
        found = 'False'
        if not numbers2:
            numbers2.append(numbers1[0])
        else:
            # check if we have already found the number
            for z in range(0, len(numbers2)):
                if numbers1[j] == numbers2[z]:
                    found = "True"

            if found == "False":
                numbers2.append(numbers1[j])
    n = len(numbers2)
    # knowing the dimension we construct the matrix
    Anew = [[0 for x in range(n)] for y in range(n)]
    with open(Apath) as f:
        for line in f:
            line = line.split(' ')
            if line:
                line = [int(i) for i in line]
                Start = line[0]
                End = line[1]
                RowtoChange1 = Anew[Start]
                RowtoChange1[End] = 1
                RowtoChange1[Start] = 1
                RowtoChange2 = Anew[End]
                RowtoChange2[End] = 1
                # update row
                sum1 = []
                sum2 = []
                a = Anew[Start]  # update first element
                b = RowtoChange1
                x1 = Anew[End]
                x2 = RowtoChange2
                for j in range(0, n):
                    if a[j]+b[j] == 2:  # we update the row of the firt element
                        sum1.append(1)
                    else:
                        sum1.append(a[j]+b[j])
                    if x1[j] + x2[j] == 2:  # we update the row of the second element
                        sum2.append(1)
                    else:
                        sum2.append(x1[j]+x2[j])
                Anew[Start] = sum1  # Anew -> matrix of the graph
                Anew[End] = sum2
    # We use FourRussians Algoryhm n times for Anew matrix
    A = Anew
    B = Anew
    Bnew = Anew
    for t in range(0, n):
        C = [[0 for x in range(n)] for y in range(n)]
        # We check if the dimension of the matrixes is divided by logn
        m = log_2(n)
        m = rounddown(m)
        # We add a zero column in A and a zero row in B
        n2 = n
        while (n2 % m != 0) & (n != 3):
            n2 = n2+1
            Anew = [[0 for x in range(n2)] for y in range(n)]
            Bnew = [[0 for x in range(n)] for y in range(n2)]
        # We need to copy the elements to the new matrixex
        # First we start with A matrix
        for i in range(0, n):
            for j in range(0, n):
                Anew[j][i] = A[j][i]

        if Bpath[0] == "Notgiven":
            for i in range(0, n):
                for j in range(0, n):
                    Bnew[j][i] = B[j][i]

        limit = roundup(n / m) + 1
        for i in range(1, limit):
            rs = [[0 for x in range(n)] for y in range(2**m)]
            bp = 1
            k = 0
            if 2 ** m - 2 == 0:
                m = m+1

            for j in range(1, (2**m)):
                # We need binary sum
                a = Bnew[i*m-(k+1)]
                b = rs[j-(2**k)]
                sum_list = []
                for z in range(0, n):
                    if a[z] + b[z] == 2:
                        sum_list.append(1)
                    else:
                        sum_list.append(a[z] + b[z])
                rs[j] = sum_list
                if bp == 1:
                    bp = j+1
                    k = k+1
                else:
                    bp = bp-1

            TempC = [[0 for x in range(n)] for y in range(n)]
            for j in range(0, n):
                number = ''
                # We find the binary number

                sublist = Anew[j]
                m1 = log_2(n)
                m1 = rounddown(m1)
                m = m1
                for h in range((i-1)*m1, i*m1):
                    number = number + str(sublist[h])
                decimal_Numb = int(number, 2)
                TempC[j] = rs[decimal_Numb]

            # Calculate new C matrix
            for h in range(0, n):
                # We take each row of the matrix
                a = C[h]
                b = TempC[h]
                sum_list = []
                for l in range(0, n):
                    if a[l] + b[l] == 2:
                        sum_list.append(1)
                    else:
                        sum_list.append(a[l] + b[l])

                C[h] = sum_list

            A = C
    for j in range(0, n):
        row = C[j]
        for z in range(0, n):
            if row[z] == 1:
                print(j, z)

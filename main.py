from prediksiCostProgram import soal_nomor_4

def soal_nomor_1(x):
    last_index = x[-1]
    for n in range(1, last_index + 1):
        if n not in x:
            print('jawaban no 1: y =', n)

def soal_nomor_2(y):
    number = list()
    x = [1,5,6,1,0,1]
    length = len(x)
    for n in range(0, length):
        a = x[n]
        for j in range(0, n):
            b = x[j]
            if a + b == y:
                number.append([a, b])
    print('jawaban no 2: z =', number)

def soal_nomor_3(colMap):
    output = list()
    left_range, right_range = colMap
    rangeMap = left_range + right_range
    number = []
    n = 1
    while n < 15:
        left = []
        for l in range(n, n + left_range):
            left.append(l)
        number.append(left)
        n += rangeMap
    output.append(number)
    number_second = []
    n = 1 + left_range
    while n < 15:
        right = []
        for r in range(n, n + right_range):
            right.append(r)
        number_second.append(right)
        n += rangeMap
    output.append(number_second)
    print('jawaban no 3:', output)

if __name__ == '__main__':
    soal_nomor_1([1, 2, 3, 4, 5, 6, 8, 9, 10])
    soal_nomor_2(6)
    soal_nomor_3([3, 2])
    soal_nomor_4(500, 180, [100,140,150,200,330,360,400], [1000,2000,5000,1000,6000,4000,1000])

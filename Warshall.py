
def genMatrix(size=10, value=5):
    """
    Generates a 2d square matrix of the specified size with the specified values
    """

    matrix = [[value for col in range(0,size)] for row in range(0,size)]

    return matrix


testMatrix2 = [[5,3,4,0], [9,4,5,2], [0,2,0,1]]

def warshall_Algorithm(matrix):

    length = len(matrix)

    for k in range(length):
        for i in range(length):
            for j in range(length):
                matrix[i][j] = min(int(matrix[i][j]), int(matrix[i][k]) + int(matrix[k][j]))
                
    print(matrix)


testMatrix = genMatrix()

warshall_Algorithm(testMatrix2)








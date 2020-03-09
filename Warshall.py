
from mpi4py import MPI

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






#Number of rows per threads= number of rows / # of threads
#Threads per row = # of threads/ number of rows
#Starting row = number of rows per threads* process #
#Ending row = number of rows per threads* (threads# + 1)
#Owner of a row = (threads per row * row)


testMatrix = genMatrix()

warshall_Algorithm(testMatrix2)








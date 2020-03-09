from mpi4py import MPI


MPIMatrix = [[5,3,4,0,4], [9,4,5,2,2], [0,2,0,1,4],[1,4,9,1,7], [1,4,9,1,7] ] 


print("Input Matrix (5x5)")
print(MPIMatrix)
print("-----------------------------------")



comm = MPI.COMM_WORLD



length = len(MPIMatrix) #length of matrix (rows)

threads_Per_Row = comm.Get_size() / length #helpful formulas from David 
rows_Per_Thread = length // comm.Get_size()

startRow = rows_Per_Thread * comm.Get_rank()
endRow = rows_Per_Thread * (comm.Get_rank() + 1)



for k in range(length): #MPI Warshall

    owner = int((comm.Get_size() / length) * k)
    MPIMatrix[k] = comm.bcast(MPIMatrix[k], root=owner)

    for x in range(startRow, endRow):
        for y in range(length):
            
            MPIMatrix[x][y] = min(int(MPIMatrix[x][y]), (int(MPIMatrix[x][k]) + int(MPIMatrix[k][y])))



#PUT MATRIX TOGETHER

if comm.Get_rank() == 0:
    for k in range(endRow, length):
        owner = int((comm.Get_size() / length) * k) 
        MPIMatrix[k] = comm.recv(source = owner, tag = k)
        
else:
    for k in range(startRow, endRow):
        owner = int((comm.Get_size() / length) * k) 
        comm.send(MPIMatrix[k], dest = 0, tag = k)
    
  
  
  

print("Warshall Algorithm")
print(MPIMatrix)








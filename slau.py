# Task 2 
def gaussian_elimination(matrix):
    for i in range(len(matrix[0])):
        for j in range(i+1,len(matrix)):
            m = matrix[j][i]/matrix[i][i]
            matrix[j] = [matrix[j][k]-m*matrix[i][k] for k in range(len(matrix[0]))]
  # backward substitution
    x = [0] * n
    print('-'*20)
    if matrix[n-1][n-1] == 0 and matrix[n-1][n] != 0:
        flag = -1
    else:
        if matrix[n-1][n-1] != 0:
            for i in range(n-1, -1, -1):
                s = sum(matrix[i][j] * x[j] for j in range(i, n))
                x[i] = (matrix[i][n] - s) / matrix[i][i]  
                flag = 1
        else:
            flag = 2 
    return x, flag

n = int(input("Enter the matrix size and matrix:"))
matrix = []
for i in range(n):
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
    matrix.append(row)
x,flag = gaussian_elimination(matrix)

if flag == 2:
    print('No unique solution') 
elif flag == 1:   
    for temp in range(0, n):                
        print ('Answer is: x%(number)s = %(x)f' % {"x": x[temp], "number": temp+1})
else:
    print('No solution. For you -1')
#[[1.0, 3.0, 2.0, 4.0], [2.0, -1.0, 1.0, 1.0], [3.0, 1.0, -2.0, 2.0]]
#[[3 2 1 1 -2],[1 -1 4 -1 -1],[-2 -2 -3 1 9],[1 5 -1 2 4]]
#[[7 -2 -1 2],[6 -4 -5 3],[1 2 4 5]] - no solution

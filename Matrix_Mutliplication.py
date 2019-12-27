# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 14:23:52 2019

@author: amo010
"""
# =============================================================================
# start of the function ReadMatrices()
# =============================================================================
def ReadMatrices(Matrix1, Matrix2):
    '''
    1. This function reads two matrices from the hard disk into the python IDE and
    stores them in variables, given that the user provides the correct file path, file name and extension
    
    2. Each of the matrices has to be stored in a file, in which there is nothing else (i.e. headings, titles, etc.)
    is stored. Only the matrices are stored in the files, separated by spaces (for values in columns), and each new
    lines count as new row
    '''
    #creates a list to contain Matrix A.
    MatrixA=[]
    #opening the file "Matrix1": a variable that includes the folder path, file name, and file extension,
    #the opened file is named "MatA"
    with open(Matrix1, 'r') as MatA:
        #the read() method reads the whole file into variable "MatrixAStr"
        #Each line of the file MatA is stored as a string in the "MatrixAStr" list
        MatrixAStr = MatA.read().splitlines()
        # looping over each (string) element inside the "MatrixAStr" list
        for i in MatrixAStr:
            #splitting each string (element) inside the list based on the " " (i.e. space) between string characters 
            #storing the outcome of applying the split() method on each element of the "MatrixAStr" in a variable "targetStrA"
            targetStrA = i.split(' ')
            #adding each character into "MatrixA", after converting it into an float.
            MatrixA.append([round(float(k), 2) for k in targetStrA])
    
    #creates a list to contain Matrix B.    
    MatrixB=[]
    #opening the file "Matrix2": a variable that includes the folder path, file name, and file extension,
    #the opened file is named "MatB"
    with open(Matrix2, 'r') as MatB:
        #the read() method reads the whole file into variable "MatrixBStr"
        #Each line of the file MatB is stored as a string in the "MatrixBStr" list
        MatrixBStr = MatB.read().splitlines()
        # looping over each (string) element inside the "MatrixBStr" list
        for j in MatrixBStr:
            #splitting each string (element) inside the list based on the " " (i.e. space) between string characters 
            #storing the outcome of applying the split() method on each element of the "MatrixBStr" in a variable "targetStrB"
            targetStrB = j.split(' ')
            #adding each character into "MatrixB", after converting it into an integer.
            MatrixB.append([float(l) for l in targetStrB])
    #the function returns two outputs: MatrixA (i.e. Matrix A) and MatrixB (i.e. Matrix B)
    return MatrixA, MatrixB    
# =============================================================================
# end of function ReadMatrices()
# =============================================================================

# =============================================================================
# start of the function MultipyMatrices()
# =============================================================================
def MultiplyMatrices(Matrix1, Matrix2):
    '''
    1. This function takes two matrices as input parameters.
    2. It checks if the matrices can be multiplied or not.
    3. It return the output.
    '''
    #create a list to contain Matrix C (i.e. the resultant matrix of the multiplication of Matrix A and Matrix B)
    MatrixC=[]
    
    #counts the number of rows of Matrix A, and stores it in variable "nA"
    nA = len(Matrix1)
    #counts the number of columns of Matrix A, and stores it in variable "mA"
    mA = len(Matrix1[0])
    
    #counts the number of rows of Matrix B, and stores it in variable "nB"
    nB = len(Matrix2)
    #counts the number of columns of Matrix B, and stores it in variable "mB"
    mB = len(Matrix2[0])
    
    #Checks if the number of columns of Matrix A equals the number of rows of Matrix B
    if mA == nB:
        #it adds a new list inside the Matrix C list, depending on the number of rows of Matrix A
        for i in range(nA):
            MatrixC.append([])
            #it fills each of insider lists (contained inside the Matrix C list) with zeros, depending on the number of columns of Matrix B
            for j in range(mB):
                MatrixC[i].append(0)
        
        #calculates the resultant of matrix multiplication of Matrix A and Matrix B, and stores the results in Matrix C
        for i in range(nA):
            for j in range(mB):
                for k in range(nB):
                    #it rounds the output to 2 decimal places
                    MatrixC[i][j] += Matrix1[i][k]*Matrix2[k][j]
                    
        #This loop checks of a value in Matrix C is an integer or a float, and reduces the number to a whole integer if
        #it encounters a ".0" float value attached to the number.
        for y in range(len(MatrixC)):
            for u in range(len(MatrixC[y])):
                if MatrixC[y][u].is_integer():
                    p= MatrixC[y][u]
                    MatrixC[y][u] = int(p)
                #If the number has a decimal float value, it reduces it to 2 decimal numbers.
                elif isinstance(MatrixC[y][u], float):
                    p= MatrixC[y][u]
                    MatrixC[y][u] = round(p, 2)
                    
        #This prints the final resultant (Matrix C) into the console.
        print(MatrixC)
        #Returns Matrix C as function output.
        return MatrixC
    else:
        #in case the matrices can NOT be multiplied (i.e. if the number of columns in Matrix A does NOT equal the number of row in Matrix B)
        #the function returns the following statement a printed statement.
        return print("Those two matrices can not be multiplied!")
# =============================================================================
# end of function MultipyMatrices()
# =============================================================================


# =============================================================================
# start of function MatrixAddition()
# =============================================================================
def MatrixAddition(Matrix1, Matrix2):
    '''
    
    '''
    #create a list to contain Matrix C (i.e. the resultant matrix of the multiplication of Matrix A and Matrix B)
    MatrixC=[]
    
    #counts the number of rows of Matrix A, and stores it in variable "nA"
    nA = len(Matrix1)
    #counts the number of columns of Matrix A, and stores it in variable "mA"
    mA = len(Matrix1[0])
    
    #counts the number of rows of Matrix B, and stores it in variable "nB"
    nB = len(Matrix2)
    #counts the number of columns of Matrix B, and stores it in variable "mB"
    mB = len(Matrix2[0])
    
    if nA == nB and mA == mB:
        #it adds a new list inside the Matrix C list, depending on the number of rows of Matrix A
        for i in range(nA):
            MatrixC.append([])
            #it fills each of insider lists (contained inside the Matrix C list) with zeros, depending on the number of columns of Matrix B
            for j in range(mB):
                MatrixC[i].append(0)
        
        #calculates the resultant of matrix multiplication of Matrix A and Matrix B, and stores the results in Matrix C
        for i in range(nA):
            for j in range(mB):
                MatrixC[i][j] = Matrix1[i][j]+Matrix2[i][j]
                    
        #This loop checks of a value in Matrix C is an integer or a float, and reduces the number to a whole integer if
        #it encounters a ".0" float value attached to the number.
        for y in range(len(MatrixC)):
            for u in range(len(MatrixC[y])):
                if MatrixC[y][u].is_integer():
                    p= MatrixC[y][u]
                    MatrixC[y][u] = int(p)
                #If the number has a decimal float value, it reduces it to 2 decimal numbers.
                elif isinstance(MatrixC[y][u], float):
                    p= MatrixC[y][u]
                    MatrixC[y][u] = round(p, 2)
                    
        #This prints the final resultant (Matrix C) into the console.
        print(MatrixC)
        #Returns Matrix C as function output.
        return MatrixC
    else:
        #in case the matrices can NOT be multiplied (i.e. if the number of columns in Matrix A does NOT equal the number of row in Matrix B)
        #the function returns the following statement a printed statement.
        return print("Those two matrices can not be Added!")
        
# =============================================================================
# end of function MatrixAddition()    
# =============================================================================

# =============================================================================
# start of function MatrixSubtraction()
# =============================================================================
def MatrixSubtraction(Matrix1, Matrix2):
    '''
    
    '''
    #create a list to contain Matrix C (i.e. the resultant matrix of the multiplication of Matrix A and Matrix B)
    MatrixC=[]
    
    #counts the number of rows of Matrix A, and stores it in variable "nA"
    nA = len(Matrix1)
    #counts the number of columns of Matrix A, and stores it in variable "mA"
    mA = len(Matrix1[0])
    
    #counts the number of rows of Matrix B, and stores it in variable "nB"
    nB = len(Matrix2)
    #counts the number of columns of Matrix B, and stores it in variable "mB"
    mB = len(Matrix2[0])
    
    if nA == nB and mA == mB:
        #it adds a new list inside the Matrix C list, depending on the number of rows of Matrix A
        for i in range(nA):
            MatrixC.append([])
            #it fills each of insider lists (contained inside the Matrix C list) with zeros, depending on the number of columns of Matrix B
            for j in range(mB):
                MatrixC[i].append(0)
        
        #calculates the resultant of matrix multiplication of Matrix A and Matrix B, and stores the results in Matrix C
        for i in range(nA):
            for j in range(mB):
                MatrixC[i][j] = Matrix1[i][j]-Matrix2[i][j]
                    
        #This loop checks of a value in Matrix C is an integer or a float, and reduces the number to a whole integer if
        #it encounters a ".0" float value attached to the number.
        for y in range(len(MatrixC)):
            for u in range(len(MatrixC[y])):
                if MatrixC[y][u].is_integer():
                    p= MatrixC[y][u]
                    MatrixC[y][u] = int(p)
                #If the number has a decimal float value, it reduces it to 2 decimal numbers.
                elif isinstance(MatrixC[y][u], float):
                    p= MatrixC[y][u]
                    MatrixC[y][u] = round(p, 2)
                    
        #This prints the final resultant (Matrix C) into the console.
        print(MatrixC)
        #Returns Matrix C as function output.
        return MatrixC
    else:
        #in case the matrices can NOT be multiplied (i.e. if the number of columns in Matrix A does NOT equal the number of row in Matrix B)
        #the function returns the following statement a printed statement.
        return print("Those two matrices can not be subtracted!")
        
# =============================================================================
# end of function MatrixSubtraction()    
# =============================================================================

# =============================================================================
# start of the function MultipyByScaler()
# =============================================================================
def MultipyByScaler(Matrix1, Scaler):
    '''
    1. This function takes two matrices as input parameters.
    2. It checks if the matrices can be multiplied or not.
    3. It return the output.
    '''
    #create a list to contain Matrix C (i.e. the resultant matrix of the multiplication of Matrix A and Matrix B)
    MatrixC=[]
    
    #counts the number of rows of Matrix A, and stores it in variable "nA"
    nA = len(Matrix1)
    #counts the number of columns of Matrix A, and stores it in variable "mA"
    mA = len(Matrix1[0])
    
    for i in range(nA):
        MatrixC.append([])
        #it fills each of insider lists (contained inside the Matrix C list) with zeros, depending on the number of columns of Matrix B
        for j in range(mA):
            MatrixC[i].append(0)
    
    #calculates the resultant of matrix multiplication of Matrix A and Matrix B, and stores the results in Matrix C
    for i in range(nA):
        for j in range(mA):
            MatrixC[i][j] = Matrix1[i][j]*Scaler
                    
        #This loop checks of a value in Matrix C is an integer or a float, and reduces the number to a whole integer if
        #it encounters a ".0" float value attached to the number.
        for y in range(len(MatrixC)):
            for u in range(len(MatrixC[y])):
                if MatrixC[y][u].is_integer():
                    p= MatrixC[y][u]
                    MatrixC[y][u] = int(p)
                #If the number has a decimal float value, it reduces it to 2 decimal numbers.
                elif isinstance(MatrixC[y][u], float):
                    p= MatrixC[y][u]
                    MatrixC[y][u] = round(p, 2)
                    
    #This prints the final resultant (Matrix C) into the console.
    print(MatrixC)
    #Returns Matrix C as function output.
    return MatrixC

# =============================================================================
# end of function MultipyByScaler()
# =============================================================================



# =============================================================================
# start of the function WriteMatrix()
# =============================================================================
def WriteMatrix(data_to_be_written, file_path_name_and_extension):
    '''
    1. This function write a variable content into a file on hard disk, with a name of the user's choosing
    '''
    with open(file_path_name_and_extension, 'w') as output:
        num_of_rows = len(data_to_be_written)
        num_of_columns = len(data_to_be_written[0])
        matrix_dimenstions = "The matrix dimensions are " + str(num_of_rows) + " * " + str(num_of_columns)+"\n"
        
        output.write(matrix_dimenstions)
        output.write("Author: Ahmed E. F. R. Mohammed\n")
        output.write("Locker number: 385\n\n")
            
        for i, sublist in enumerate(data_to_be_written):
            string = ' '.join(map(str, sublist))
            for item in string:
                output.write(item)
            output.write('\n')
# =============================================================================
# end of function WriteMatrix()
# =============================================================================


# =============================================================================
# start of the function CheckSymmetry()
# =============================================================================
def CheckSymmetry(matrix):
    '''
    1. This function takes a matrix as an input.
    2. It checks whether the matrix is symmetrical or not.
    3. It return the checking result.
    '''
    #create a list that will include the outcome of testing the match between a(ij) and b(ji)
    Checklist = []
    #Since symmetric matrices are square, it checks if the number of rows matches the number of columns
    if len(matrix) == len(matrix[0]):
        #if True, it loops over the rows anc columns in the matrix respectively
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                #if a(ij) NOT equal to b(ji), it appends a False to the "Checklist" list...Otherwise, it appends a True boolean
                if matrix[i][j] != matrix[j][i]:
                    Checklist.append(False)
                else:
                    Checklist.append(True)
    #if the first test of matrix dimension fails, it return a statement that the matris is non-symmetric.
    else:
        return print("The Matrix is NON-SYMMETRIC")
                
    #if there is any False value in the "Checklist" list, this implies that there was a mismatch between one 
    #or more of the a(ij) values and their counterparts of b(ji)
    if False in Checklist:
        return print("The Matrix is NON-SYMMETRIC")
    else:
        return print("The Matrix is SYMMETRIC")
# =============================================================================
# end of function ReadMatrices()
# =============================================================================

#asks the user to provide the folder path, as it is and without adding a "\" at the end of it, as this was taken care of in the algorithm
FolderPath = input("Enter the File Path in which the two Matrices are stored: ")
#asks the user to provide the file name and extension of Matrix A
file_matrix_A = input("Enter the file name and extension of Matrix A: ")
#asks the user to provide the file name and extension of Matrix B
file_matrix_B = input("Enter the file name and extension of Matrix B: ")
#asks the user to provide the desired file name and extension of the produced Matrix
file_matrix_C = input("Enter the name for the output Matrix: ")

Mat_A = FolderPath + "\\" + file_matrix_A

Mat_B = FolderPath + "\\" + file_matrix_B

Mat_C = FolderPath + "\\" + file_matrix_C

#calling the ReadMatrices() function
A, B = ReadMatrices(Mat_A, Mat_B)

#calling the CheckSymmetry() function on Matrix A
CheckSymmetry(A)

#calling the MultiplyMatrices() function
C = MultiplyMatrices(A, B)

#calling the WriteMatrix() function
WriteMatrix(C, Mat_C)

def matrix_addition(m1,m2):
    result=[]
    for row in range(len(m1)):
        result.append([])#yeni satir acar
        for column in range(len(m1[0])):
            #print(m1[row][column],end=" ")
            result[row].append(m1[row][column]+m2[row][column])
        #print()
    return result
    
def matrix_substraction(m1,m2):
    result=[]
    for row in range(len(m1)):
        result.append([])#yeni satir acar
        for column in range(len(m1[0])):#1 ise x[0->burdaki sayilar][1->burdaki sayilar]  
            #print(m1[row][column],end=" ")
            result[row].append(m1[row][column]-m2[row][column])
        #print()
    return result    
    
def my_matrix_scalar_product(alpha,m1):
    my_result=[]
    for row in range(len(m1)):
        my_result.append([])
        for column in range(len(m1[0])):
            my_result[row].append(m1[row][column]*alpha)
    return my_result
    
def f_1(matrix_1,i):
    return matrix_1[i]

def f_2(matrix_1,j):
    my_j_th_col=[]
    for row in matrix_1:
        for indis in range(len(row)):
            if(indis==j):
                my_j_th_col.append(row[indis])
    return my_j_th_col

    
def my_vector_inner_product(v,w):
    size=len(v)
    my_result=[]
    for i in range(size):
        my_result.append(0)
    
    for i in range(size):
        my_result[i]=v[i]*w[i]

    t=0
    for i in range(size):
        t=t+my_result[i]

    return t
    
    
def my_matrix_multiply(m1,m2):
    my_result=[]
    for row in range(len(m1)):
        my_result.append([])
        for column in range(len(m2[0])):
            a=f_1(m1,row)#m1 in satirini getirir
            b=f_2(m2,column)#m2 in sutununu getirir
            c=my_vector_inner_product(a,b)
            my_result[row].append(c)
    return my_result
    
matrix_1=[[4,6],[8,5]]
matrix_2=[[4,6,3],[8,5,6]]
alpha=10

print("f1->",f_1(matrix_1,1))#1 ise x[0->burdaki sayilar][1->burdaki sayilar]  
print("f2->",f_2(matrix_1,0))

matrix_1=[[1,2],[3,4]]
matrix_2=[[5,6,7],[8,9,10]]
print("matris carpim->",my_matrix_multiply(matrix_1,matrix_2))

print(matrix_addition(matrix_1,matrix_2))
print(matrix_substraction(matrix_1,matrix_2))
print(my_matrix_scalar_product(alpha,matrix_1))



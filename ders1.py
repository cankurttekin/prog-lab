import random
def generate_array (n):
    #Generate an array with n elements.
    arr = []
    for i in range (n):
        arr.append(random.randint(0,100))
    return arr

##################################

def bubble_sort(array):
    #Sorts an array with Bubble Sort Algorithm
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j]>array[j+1]:
                array[j+1],array[j] = array[j],array[j+1]
    return array

##################################

def selection_sort(array):
    #Sorts an array with Selection Sort Algorithm
    for i in range (len(array)-1):
        min = i
        for j in range (i+1,len(array)):
            if (array[j] < array[min]):
                min = j
        array[i],array[min] = array[min],array[i]

##################################

def search_in_array(array, item):
    #Checks if item in array
    for i in range(len(array)):
        if array[i]==item:
            return i
    else:
        return "NOT FOUND"

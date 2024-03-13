
def bubble_sort(list): 
    
    for i in range(0,len(list)-1): 
        for j in range(len(list)-1): 
            if(list[j]>list[j+1]): 
               list[j],list[j+1] = list[j+1], list[j] 

    return list 
 
list = [15, 5, 8, 6, 7, 2] 
print("The unsorted list is: ", list) 
print("The sorted list is: ", bubble_sort(list)) 

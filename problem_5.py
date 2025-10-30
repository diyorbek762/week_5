# calculate the average of every consecutive “window” of window_size elements in the list.
# For example, if window_size is 3, you first average elements at indices 0, 1, 2, 
# then average elements at 1, 2, 3, then 2, 3, 4, and so on, until you reach the end of the list.
# Return a new list containing these calculated averages.
def calculate_moving_average(data, window_size):
    result_list=[]
    if len(data)<window_size:
            return result_list
    else:
        for i in range(len(data)-window_size+1):
        # if len(data)==1 or len(data)<window_size:
        #     print('error')
           average = (sum(data[i:window_size+i]))/window_size
           result_list.append(average)
        return result_list


print(calculate_moving_average([10, 20, 30, 40, 50], 3))
print(calculate_moving_average([1, 2, 3, 4, 5], 2))
print(calculate_moving_average([10, 20, 30, 40, 50], 3))
print(calculate_moving_average([5, 10, 15], 5))
print(calculate_moving_average([8, 12], 1)) 
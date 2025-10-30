#  Write a Python function called find_longest_run(data)
#  that takes a single list of items (data) as an argument.
#  The function should find the longest “run” of consecutive, identical elements and 
# return the length of that run.

# def remove_outliers(data, min_val, max_val):
#     current_index=0
#     while current_index<len(data):
#         if data[current_index]>max_val or data[current_index]<min_val:
#             data.pop(current_index)
#         else:
#             current_index+=1



# measurements = [8, 5, 12, 1, 9, 20, 15]
# print(measurements)
# remove_outliers(measurements,5,15)
# print(measurements)
# def zigzag_merge(list1, list2):
#     result_list = []
#     min_list_len = min(len(list1), len(list2))
#     for i in range(min_list_len):
#         result_list.append(list1[i])
#         result_list.append(list2[i])
#     max_list_len = max(len(list1), len(list2))

#     # longer_list = list1 if len(list1) > len(list2) else list2

#     if len(list1) > len(list2):
#         longer_list = list1
#     else:
#         longer_list = list2

#     for j in range(min_list_len, max_list_len):
#         result_list.append(longer_list[j])
#     return result_list

# list_c = [1, 2]
# list_d = ['A', 'B', 'C', 'D']
# # [1, 'A', 2, 'B', 'C', 'D']
# print(zigzag_merge(list_c, list_d))

def consecutive_run(data):
    # if not data:
    #     return 0
    if len(data)==0:
        return 0
    longest_run=1
    current_streak=1
    for i in range(1,len(data)):
        if data[i-1] == data[i]:
            current_streak+=1
            if current_streak>longest_run:
                longest_run=current_streak
        else:
            current_streak=1
    return longest_run           


print(consecutive_run([1,1,12,3,5,5,5,8,8,8,8,8,8]))
print(consecutive_run([1,5,8,8,8,8]))
print(consecutive_run([1, 2, 2, 3, 3, 3, 2, 2]))
print(consecutive_run(['A', 'A', 'A', 'B', 'C', 'C']))
print(consecutive_run([5, 5, 5, 5, 5]))
print(consecutive_run([1, 2, 3, 4, 5]))
print(consecutive_run([]))

# def find_longest_run(data):
#     first_streak=data[0]
#     current_streak=1
#     while 



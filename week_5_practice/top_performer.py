# Write a Python function called find_best_student(student_names, student_scores) 
# that takes these two lists as arguments.
def find_best_student(student_names, student_scores):
    if len(student_names)<1:
        return None
    high_index= 0
    high_score= student_scores[0]
    for i in range(len(student_scores)):
        if student_scores[i] >high_score:
            high_score=student_scores[i]
            high_index=i
    return student_names[high_index]

names = ["Alice", "Bob", "Charlie", "David"]
scores = [88, 92, 99, 95]
print(find_best_student(names, scores))
# scores = [88, 92, 99, 95]
# print(scores)
# find_best_student(scores)
# print(scores)
names = ["Eve", "Frank", "Grace"]
scores = [95, 85, 95]
print(find_best_student(names, scores))


names = []
scores = []
print(find_best_student(names, scores))
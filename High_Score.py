# High Score
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

#Write your code
big = student_scores[0]
for i in range(0, len(student_scores)):
    if student_scores[i] > big:
        big = student_scores[i]
print(f"The highest score in the class is: {big}")
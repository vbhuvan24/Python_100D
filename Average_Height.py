# Average Height
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

#Write your code

total_height = 0
for height in student_heights:
    total_height += height
# print(total_height)

total_member = 0
for height in student_heights:
    total_member += 1
# print(total_member)

average_height = round(total_height / total_member)
print(average_height)
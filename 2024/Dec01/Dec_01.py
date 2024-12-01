
with open('note.txt', 'r') as file:
    lines = file.readlines()

left_numbers = []
right_numbers = []

for line in lines:
    numbers = line.strip().split()
    left_numbers.append(int(numbers[0]))
    right_numbers.append(int(numbers[1]))

sorted_left = sorted(left_numbers)
sorted_right = sorted(right_numbers)

print("Sorterte tall på venstere side", sorted_left)
print("Sorterte tall på høyre side", sorted_right)
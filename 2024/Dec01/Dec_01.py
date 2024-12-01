
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

print("Sorted numbers left side", sorted_left)
print("Sorted number right side", sorted_right)

differences = []

for left, right in zip(sorted_left, sorted_right):
    differences.append(abs(left - right))

total_distance = sum(differences)

print("Differences in distance", differences)
print("Total distance", total_distance)

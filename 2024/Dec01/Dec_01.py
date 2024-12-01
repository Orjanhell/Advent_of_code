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

print("Sorted numbers on the left side:", sorted_left)
print("Sorted numbers on the right side:", sorted_right)

similarity_score = 0

for left in sorted_left:
    count_in_right = right_numbers.count(left)
    print(f"Number {left} appears {count_in_right} times in the right list.")
    similarity_score += left * count_in_right

print("Similarity score between the lists:", similarity_score)

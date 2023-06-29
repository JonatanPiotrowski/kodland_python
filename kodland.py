# 1
def shrink_list(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        while left < right and nums[left] != 0:
            left += 1

        while left < right and nums[right] == 0:
            right -= 1

        nums[left], nums[right] = nums[right], nums[left]

    return nums


input_data = [4, 0, 5, 0, 3, 0, 0, 5]
result = shrink_list(input_data)
print(result)


# 2
def count_vowels_consonants(line):
    vowels = 0
    consonants = 0
    for char in line:
        if char.isalpha():
            if char.lower() in 'aeiou':
                vowels += 1
            else:
                consonants += 1
    return vowels, consonants


def count_poem_stats(lines):
    total_vowels = 0
    total_consonants = 0

    for line in lines:
        line_vowels, line_consonants = count_vowels_consonants(line)
        total_vowels += line_vowels
        total_consonants += line_consonants
        print("Line:", line)
        print("Vowels:", line_vowels)
        print("Consonants:", line_consonants)
        print()

    print("Total Vowels:", total_vowels)
    print("Total Consonants:", total_consonants)


num_lines = int(input("How many lines will there be? "))
poem_lines = []

for i in range(num_lines):
    line = input("Enter line {}: ".format(i + 1))
    poem_lines.append(line)

count_poem_stats(poem_lines)


# 3
def can_queen_move(col1, row1, col2, row2):
    if col1 == col2 or row1 == row2 or abs(col1 - col2) == abs(row1 - row2):
        return "YES"
    else:
        return "NO"


col1 = int(input("Enter the column of the first square (1-8): "))
row1 = int(input("Enter the row of the first square (1-8): "))
col2 = int(input("Enter the column of the second square (1-8): "))
row2 = int(input("Enter the row of the second square (1-8): "))

result = can_queen_move(col1, row1, col2, row2)
print(result)

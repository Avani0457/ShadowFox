# for loop Task1
'''yimport random

rolls = 20
count_6 = 0
count_1 = 0
two_6_in_row = 0

previous_roll = None

for i in range(rolls):
    roll = random.randint(1, 6)
    print(f"Roll {i+1}: {roll}")

    if roll == 6:
        count_6 += 1
        if previous_roll == 6:
            two_6_in_row += 1

    if roll == 1:
        count_1 += 1

    previous_roll = roll

print("\n--- Statistics ---")
print(f"Total rolls: {rolls}")
print(f"Number of 6s rolled: {count_6}")
print(f"Number of 1s rolled: {count_1}")
print(f"Two 6s in a row occurred: {two_6_in_row} times")'''

#Task2
total_jumping_jacks = 100
completed = 0

while completed < total_jumping_jacks:
    completed += 10
    print(f"You completed {completed} jumping jacks")

    if completed >= total_jumping_jacks:
        print("Congratulations! You completed the workout!")
        break

    tired = input("Are you tired? (yes/y or no/n): ").strip().lower()

    if tired in ("yes", "y"):
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").strip().lower()
        if skip in ("yes", "y"):
            print(f"You completed a total of {completed} jumping jacks.")
            break
        else:
            remaining = total_jumping_jacks - completed
            print(f"{remaining} jumping jacks remaining. Continue!\n")

    else:
        remaining = total_jumping_jacks - completed
        print(f"{remaining} jumping jacks remaining. Continue!\n")


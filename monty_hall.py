import random as r

# Variable declaration
total_trials = 100000
total_doors = 3
doors = []
correct_count = 0
fail_count = 0

# Insert 2 zeros and 1 one into the list
def create_monty_hall(total_doors):
    for i in range(total_doors - 1):
        doors.append(0)
    doors.append(1)
    r.shuffle(doors)

def choice_and_remove():
    random_choice = r.randrange(3)
    # Remove random choice index
    doors.pop(random_choice)
    # Find and remove index with a value of 0
    doors.pop(doors.index(0))

def record_count():
    # Correct
    if 1 in doors:
        global correct_count
        correct_count += 1
    # Fail
    else:
        global fail_count
        fail_count += 1

for i in range(total_trials):
    create_monty_hall(total_doors)
    choice_and_remove()
    record_count()
    doors.clear()

# Print total result
print(f"돌린 횟수는 {total_trials}회입니다.")
print(f"성공 횟수는 {correct_count}. 틀린 횟수는 {fail_count}입니다.")
print(f"성공 확률은 {correct_count / total_trials * 100:.1f}%, 실패 확률은 {fail_count / total_trials * 100:.1f}% 입니다.")
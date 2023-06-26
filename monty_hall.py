import random as r
from typing import Final

# Variable declaration
total_trials: int = 10000
TOTAL_DOORS: Final = 3

def create_monty_hall() -> list:
    # Reset and create monty hall list
    doors = []
    for i in range(TOTAL_DOORS - 1):
        doors.append(0)
    doors.append(1)
    r.shuffle(doors)
    return doors

def choice_and_remove(doors: list) -> list:
    # Remove random one -> remove other fail.
    random_choice = r.randrange(len(doors))
    doors.pop(random_choice)
    doors.pop(doors.index(0))
    return doors

def record_count(doors:list) -> tuple:
    # Return is result correct or fail.
    if 1 in doors:
        return 1, 0
    else:
        return 0, 1

def simulate_monty_hall():
    correct_count = 0
    fail_count= 0
    for i in range(total_trials):
        doors = create_monty_hall()
        doors = choice_and_remove(doors)
        result = record_count(doors)
        correct_count += result[0]
        fail_count += result[1]
        
    # Print total result
    print(f"돌린 횟수는 {total_trials}회입니다.")
    print(f"성공 횟수는 {correct_count}. 틀린 횟수는 {fail_count}입니다.")
    print(f"성공 확률은 {correct_count / total_trials * 100:.1f}%, 실패 확률은 {fail_count / total_trials * 100:.1f}% 입니다.")
    
simulate_monty_hall()
import random
from database import task_list

def shuffle_tasks(task_list):
    random.shuffle(task_list)
    return task_list

def personalize_task_order(task_list,mood,energy):
    new_order = []
    for task in task_list:
        if task['mood'] == mood and task['energy'] == energy:
            new_order.append(task)
    return new_order



def main():
    # organized_tasks = shuffle_tasks(task_list)
    organized_tasks = personalize_task_order(task_list,'Creative','Medium')
    count = 1

    for task in organized_tasks:
        print(f"Task {count}: {task['title']}")
        count += 1






if __name__ == '__main__':
    main()
import random

task_list = [
    {

        "title": "Prepare monthly report",
        "description": "Compile sales and performance data for the team.",
        "priority": "High",
        "type": "Office",
        "energy": "Medium",
        "mood": "Stressful"
    },
    {
        "title": "Clean your room",
        "description": "Organize books, clothes, and workspace.",
        "priority": "Low",
        "type": "Home",
        "energy": "Low",
        "mood": "Relaxing"
    },
    {
        "title": "Read a chapter from business book",
        "description": "Focus on leadership and decision-making.",
        "priority": "Medium",
        "type": "Education",
        "energy": "Medium",
        "mood": "Creative"
    },
    {
        "title": "Fix UI bug in QUICK_B2B",
        "description": "Resolve padding issue in mobile view.",
        "priority": "High",
        "type": "Office",
        "energy": "High",
        "mood": "Stressful"
    },
    {
        "title": "Go for a nature walk",
        "description": "Spend 30 minutes walking in fresh air.",
        "priority": "Low",
        "type": "Personal",
        "energy": "Low",
        "mood": "Relaxing"
    },
    {
        "title": "Sketch new landing page design",
        "description": "Try a minimalistic layout with bold typography.",
        "priority": "Medium",
        "type": "Office",
        "energy": "High",
        "mood": "Creative"
    },
    {
        "title": "Cook a healthy meal",
        "description": "Try a new recipe with vegetables and protein.",
        "priority": "Low",
        "type": "Personal",
        "energy": "Medium",
        "mood": "Relaxing"
    },
    {
        "title": "Watch a documentary",
        "description": "Choose something educational or inspiring.",
        "priority": "Low",
        "type": "Education",
        "energy": "Low",
        "mood": "Relaxing"
    },
    {
        "title": "Write blog post about NOORIX journey",
        "description": "Share lessons learned and future vision.",
        "priority": "Medium",
        "type": "Office",
        "energy": "Medium",
        "mood": "Creative"
    },
    {
        "title": "Review deep learning notes",
        "description": "Revise key concepts and architectures.",
        "priority": "High",
        "type": "Education",
        "energy": "High",
        "mood": "Stressful"
    }
]

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

# Unittesting

'''
- Code was mainly tested throughly in the console with various checks to ensure functionality
- Error handling if something is entered incorrectly
- Tested some edge cases below; paste accordingly 
'''

import unittest
from datetime import datetime

# =============================================================================

#Inheritance and Polymorphism
'''
Different tasks will inherit from base task
'''
class Task: # class DoubleNode
    def __init__(self, name, dueDate, category, urgency): 
        self.name = name # Base Task Classes will store name/description of the task, the due date if applicable, set category, and urgency
        self.dueDate = dueDate
        self.category = category
        self.urgency = urgency
        self.next = None
        self.prev = None
    
    def displayTask(self): # Default task display
        return f"{self.name} (Due: {self.dueDate}, Urgency: {self.urgency}, Category: {self.category})"
    
class workTask(Task):
    '''
    Work tasks are set to have sections on projects, for instance one may be working on:
    - System Engineering TRL 1.3.1 on a technical proposal 
    While another individual may be working on: 
    - Team Management 1.9.1
    Meeting schedules or times should be listed in this section as well
    '''
    def __init__(self, name, dueDate, urgency, section): # Future: Individual or team task?, start date (to keep track of project timelines)
        super().__init__(name, dueDate, "Work", urgency)
        self.section = section

    def displayTask(self): # display Work
        return super().displayTask() + f", Section: {self.section}" # Task search does NOT include the "self.section or inputs" besides the name
        
class personalTask(Task): # Added inherit from this class, different types of personal tasks
    '''
    Personal tasks should be set if they are regarding miscellaneous duties, family tasks, events, and more
    '''
    def __init__(self, name, dueDate, urgency, recurring): 
        super().__init__(name, dueDate, "Personal", urgency) # Free time task miscellaneous?, (if not recurring, delete when done)
        self.recurring = recurring
    
    def displayTask(self): # display Personal
        return super().displayTask() + f", Recurring: {self.recurring}"
    
class dailyImportantTask(personalTask):  # Subclass implemented Daily Important (Tax filing, Cooking, groceries, etc)
    '''
    Subclass of more specific personal tasks
    '''
    def __init__(self, name, dueDate, urgency, recurring):
        super().__init__(name, dueDate, urgency, recurring)
        self.subcategory = "Daily Important"

    def displayTask(self): 
        return super().displayTask() + f", Subcategory: {self.subcategory}"

class otherTask(personalTask):  # Subclass for Other (Vacation, Birthday Party, Son's Baseball game, etc)
    '''
    Sublcass of more specific personal tasks
    '''
    def __init__(self, name, dueDate, urgency, recurring):
        super().__init__(name, dueDate, urgency, recurring)
        self.subcategory = "Other"  

    def displayTask(self): 
        return super().displayTask() + f", Subcategory: {self.subcategory}"
        
class schoolTask(Task):
    '''
    School tasks should be set if they relate in school or is in regards of academia
    '''
    def __init__(self, name, dueDate, urgency, subject): # Potential future feature: Add school department, class or course name, subject | papers, labs
        super().__init__(name, dueDate, "School", urgency)
        self.subject = subject

    def displayTask(self): #display School
        return super().displayTask() + f", Subject: {self.subject}"
    
# Linked Lists Implementation (Doubly)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Used recursive loop to count tasks | task lists will not be super long for those using this application

    def addTask(self, newTask):
        '''
        This function is designed to add tasks
        '''
        # Fixed Error: Check to prevent duplicate dasks
        current = self.head
        while current:
            if current.name.lower() == newTask.name.lower():  # case-insensitive comparison
                print(f"⚠️ Task with the name '{newTask.name}' already exists. Please use a different name.")
                return
            current = current.next
        # Regular add task
        if not self.head:
            self.head = self.tail = newTask
        else:
            self.tail.next = newTask
            newTask.prev = self.tail
            self.tail = newTask
        print(f"✅ Task '{newTask.name}' has been added successfully.")

    def deleteTask(self, name):
        '''
        This function is designed to remove tasks
        '''
        current = self.head
        while current:
            if current.name == name:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                print(f"✅ Task '{name}' has been deleted successfully.")
                return
            current = current.next
        print(f"⚠️ Task '{name}' not found.")

    def display(self): # Displays all tasks inserted (refer to the project proposal)
        current = self.head
        if not current:
            print("\n⚠️  No tasks available. Please enter tasks .")
            return
        print("\n📜 Task List:")
        while current:
            print("- " + current.displayTask()) # Insert number for simplicity future; auto delete by #?
            current = current.next

    # Implement recursive method here --> moved to sort/count
    # Searching Algorithm Implementation
    def searchTask(self, keyword):
        '''
        Dependent search function on base task display
        '''
        current = self.head
        found = False
        while current:
            if keyword.lower() in current.name.lower() or keyword.lower() in current.category.lower(): # all instances shown
                print("Found: " + current.displayTask())
                found = True
            current = current.next
        if not found:
            print("❌ No matching tasks found.")

    # Sorting Algorithm Implementation; Merge sort (recursion) more efficient than Insertion
    # Learned through Stack Overflow/Google/AI --> YouTube
    def mergeSort(self, head):
        if not head or not head.next:
            return head
        mid = self.getMiddle(head)
        midNext = mid.next
        mid.next = None
        left = self.mergeSort(head)
        right = self.mergeSort(midNext)
        return self.sortedMerge(left, right)
    
    def getMiddle(self, head):
        if not head:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def sortedMerge(self, left, right):
        if not left:
            return right
        if not right:
            return left
        if left.dueDate < right.dueDate:
            left.next = self.sortedMerge(left.next, right)
            left.next.prev = left
            left.prev = None
            return left
        else:
            right.next = self.sortedMerge(left, right.next)
            right.next.prev = right
            right.prev = None
            return right

    def sortTasks(self): # Sort by due date | sortDueDate() implementation equivalent on proposal, sortLargeDataset to be added potentially in the future
        #if not self.head or not self.head.next: # fixed to print instead of error
        #   return
        if not self.head:
            print("⚠️ No tasks to sort.")
            return
        if not self.head.next:
            print("⚠️ Nothing to sort, one task.")
            return
        self.head = self.mergeSort(self.head)
        print("✅ Tasks sorted by due date.")


    def sortAlphabetically(self): # Insertion
        '''
        Sorts tasks alphabetically
        '''
        #if not self.head or not self.head.next:
        #    return
        if not self.head:
            print("⚠️ No tasks to sort.")
            return
        if not self.head.next:
            print("⚠️ Nothing to sort, one task.")
            return
        sortedList = None
        current = self.head
        while current:
            nextNode = current.next
            sortedList = self.sortedAlpha(sortedList, current)
            current = nextNode
        self.head = sortedList
        print("✅ Tasks sorted alphabetically.")

    def sortedAlpha(self, headReference, newNode):
        if not headReference or newNode.name.lower() < headReference.name.lower():
            newNode.next = headReference
            return newNode

        current = headReference
        while current.next and current.next.name.lower() < newNode.name.lower():
            current = current.next

        newNode.next = current.next
        current.next = newNode
        return headReference
    
    def sortUrgency(self):
        '''
        Sorts tasks by urgency
        '''
        if not self.head: # Fixed printing bug
            print("⚠️ No tasks to sort.")
            return
        if not self.head.next:
            print("⚠️ Nothing to sort, one task.")
            return
    
        # Applied merge sort to sort tasks by urgency
        self.head = self.mergeSortUrgency(self.head)
        print("✅ Tasks sorted by urgency.")

    def mergeSortUrgency(self, head):
        if not head or not head.next:
            return head
        mid = self.getMiddle(head)
        midNext = mid.next
        mid.next = None
        left = self.mergeSortUrgency(head)
        right = self.mergeSortUrgency(midNext)
        return self.sortedUrgent(left, right)

    def sortedUrgent(self, left, right): # sorted merge
        if not left:
            return right
        if not right:
            return left
        if left.urgency < right.urgency:  # lower urgency value = more urgent
            left.next = self.sortedUrgent(left.next, right)
            left.next.prev = left
            left.prev = None
            return left
        else:
            right.next = self.sortedUrgent(left, right.next)
            right.next.prev = right
            right.prev = None
            return right
    
    # Recursion Implementation
    def taskCounter(self, node): # Time complexity: O(n) | fast enough since millions of data sets are not being stored
        '''
        Keeps a count of the tasks
        '''
        if not node:
            return 0
        return 1 + self.taskCounter(node.next)

    def countTasks(self):
        return self.taskCounter(self.head)
    
class Stack: 
    # --> Use stack to display; (Urgent tasks, or JUST Most recently tasks do those first)
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self, task):
        self.stack.append(task)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
    
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        
    def display(self):
        if self.isEmpty(): # --> Check
            print("\n⚠️  There are no recently entered tasks. Please enter tasks.")
            return
        print("\n⏳ Urgent/Recently Task Stack (Most Recently Entered):")
        print("**REMOVE TASK WHEN COMPLETE**")
        for i, task in enumerate(reversed(self.stack), 1): # 1 at a time, reverse; check method; report add why regular stack not linkedlist stack
            print(f"{i}. {task.displayTask()}")

            # Individual implements
            userInput = input("→ Press \"Enter\" to display next task or enter \"q\" to quit: ")
            if userInput.lower() == "q":
                break # exit loop if quit called

class Queue: # Very efficient check the notes
    # --> Use Queue to display task 1 at a time so people dont have to look at a bunch (daily tasks start to bottom easy simple); sorted or unsorted
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, task):
        self.queue.append(task)

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        
    def peek(self):
        if not self.isEmpty():
            return self.queue[0]
        
    def display(self):
        if self.isEmpty(): # --> Check
            print("\n⚠️  There are no tasks inserted. Please enter tasks.")
            return
        print("\n📅 Task Queue (Oldest Entered to Newly Entered):")
        print("**REMOVE TASK WHEN COMPLETE**")
        for i, task in enumerate(self.queue, 1): # vice versa of stack implementation
            print(f"{i}. {task.displayTask()}")

            # Individual implements
            userInput = input("→ Press \"Enter\" to display next task or enter \"q\" to quit: ") # Future: Make it more simple by asking if individuals want to remove tasks after continue (suggestions?)
            if userInput.lower() == "q":
                break

# Sources Used: https://docs.python.org/3/library/datetime.html | https://www.w3schools.com/python/python_datetime.asp
def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d") # strptime(date_string, format) --> Parse a string into a datetime object given a corresponding format
        return True
    except ValueError:
        return False

def main():
    taskList = DoublyLinkedList()
    queueOld = Queue()
    stackRecent = Stack()
    print("==========================================================")
    print("░██████╗░████████╗░█████╗░░██████╗██╗░░██╗███████╗██████╗░")
    print("██╔═══██╗╚══██╔══╝██╔══██╗██╔════╝██║░██╔╝██╔════╝██╔══██╗")
    print("╚██████╔╝░░░██║░░░██╔══██║░╚═══██╗██╔═██╗░██╔══╝░░██╔══██╗")
    print("░╚═██╔═╝░░░░██║░░░██║░░██║██████╔╝██║░╚██╗███████╗██║░░██║")
    print("░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝")
    print("==========================================================\n")
    while True:
        print("\n--------------------------") # Emoji Format at end for better visualization than front, possible errors depending on the device that is viewing the emojis such as spacing or potential question marks
        print("\n💡 Menu:💡")
        print("1. Add Tasks ➕") # Merge with 3 other task types
        print("2. Delete Tasks ➖")
        print("3. Display Tasks 📋")
        print("4. Search Task 🔍")
        print("5. Sort Tasks 📚") # Merge with 3 other sort types 
        print("6. Count Total Tasks 🔢")
        print("7. Queue by Oldest Tasks First (1 at a time) 📖⬅️")
        print("8. Display most recently entered tasks first (1 at a time) 📖➡️")
        print("9. Exit Application 👋") 
        print("\n--------------------------")
        choice = input("\nEnter your choice: ") 
        if choice == "1": # break out of loop; reset prompt
            print("\nTask Type Options: 1. Work  2. Personal  3. School")
            taskType = input("Select task type (Please enter value 1-3): ")
            name = input("Enter task name: ")
            dueDate = input("Enter due date (YYYY-MM-DD): ")
            while not is_valid_date(dueDate):
                print("❌ Invalid date format. Please follow the format used YYYY-MM-DD.")
                dueDate = input("Enter due date (YYYY-MM-DD): ")
            urgency = input("Enter urgency (Lower the number, more urgent the task [Ex. High = 1, Medium = 2, Low = 3]): ")
            if not urgency.isdigit() or int(urgency) < 1: # fixed to int digits only
                print("❌ Invalid urgency. Please enter a valid integer (Ex. High = 1, Medium = 2, Low = 3)")
                continue  
            urgency = int(urgency)
            if taskType == "1":
                section = input("Enter work section: ") # Work task
                task = workTask(name, dueDate, urgency, section)
            elif taskType == "2":
                recurring = input("Is this recurring? (Yes/No): ") # Personal Task (Default)
                while recurring.lower() not in ['yes', 'no']:
                    print("❌ Please enter Yes or No.")
                    recurring = input("Is this recurring? (Yes/No): ")
                print("Personal Task Subcategory: 1. Daily Important  2. Other")
                subcategoryChoice = input("Please select (1-2): ")
                if subcategoryChoice == "1":
                    task = dailyImportantTask(name, dueDate, urgency, recurring.capitalize())
                elif subcategoryChoice == "2":
                    task = otherTask(name, dueDate, urgency, recurring.capitalize())
                else:
                    print("❌ Invalid choice. Defaulting to 'Other'.") # default setting to other task fits in (other; to be updated in the future)
                    task = otherTask(name, dueDate, urgency, recurring.capitalize())
                    # task = personalTask(name, dueDate, urgency, recurring.capitalize()) # put back if removing subclasses for simplicity in the future
            elif taskType == "3":
                subject = input("Enter subject: ") # School task
                task = schoolTask(name, dueDate, urgency, subject)
            else:
                print("❌ Invalid task type. Task not added.")
                continue # skip remaining loop for interation
            taskList.addTask(task)
            queueOld.enqueue(task) # add to queue
            stackRecent.push(task) # add to stack
        elif choice == "2":
            name = input("Enter task name to delete: ") 
            taskList.deleteTask(name) # Delete task
        elif choice == "3":
            taskList.display() # Display tasks
        elif choice == "4":
            keyword = input("Enter search keyword: ")
            taskList.searchTask(keyword) # Search for task
        elif choice == "5":
            print("\nSort Type Options: 1. Due Date  2. Alphabetically  3. Urgency")
            sortType = input("Select sort type (Please enter value 1-3): ")
            if sortType == "1": # Sort by due date
                taskList.sortTasks()
            elif sortType == "2": # Sort by alphabetically 
                taskList.sortAlphabetically()
            elif sortType == "3": # Sort by urgency (priority)
                taskList.sortUrgency()
            else:
                print("Invalid sort type. Please enter a number between 1-3.")
        elif choice == "6":
            count = taskList.countTasks()
            print(f"Total number of tasks: {count}") # Task counter
        elif choice == "7":
            queueOld.display() # Will have to reset application once done to reset queues
        elif choice == "8":
            stackRecent.display() # Will have to reset application once done to reset stack
        elif choice == "9":
            print("🌐 Exiting application.") # Add print tasks at the end
            taskList.display()
            break
        else:
            print("❌ Invalid choice. Please try again.")

# Tester

# https://docs.python.org/3/library/unittest.html
# https://docs.python.org/3/library/unittest.html#assert-methods

# Some test edgecases | Feel free to test more/Test any errors you may have on the console
class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.task1 = workTask("Technical Proposal Overview 1.2.1 Programmatic", "2025-04-20", 1, "Proposal for Venus Aerobot")
        self.task2 = personalTask("Shop for Groceries", "2025-04-18", 4, "Yes")
        self.task3 = schoolTask("Submit Assignment", "2025-04-17", 3, "Math")
        self.taskList = DoublyLinkedList()
        self.taskList.addTask(self.task1)
        self.taskList.addTask(self.task2)
        self.taskList.addTask(self.task3)

    def test_display_task(self):
        self.assertIn("Technical Proposal Overview 1.2.1 Programmatic", self.task1.displayTask())
        self.assertIn("Recurring: Yes", self.task2.displayTask())
        self.assertIn("Subject: Math", self.task3.displayTask())

    def test_add_duplicate(self):
        duplicate = workTask("Technical Proposal Overview 1.2.1 Programmatic", "2025-04-21", 1, "Testing")
        self.taskList.addTask(duplicate)
    
    def test_delete_task(self):
        self.taskList.deleteTask("Shop for Groceries")
        self.assertEqual(self.taskList.countTasks(), 2)
    
    def test_task_counter(self):
        self.assertEqual(self.taskList.countTasks(), 3)

    def test_sort_by_due_date(self):
        self.taskList.sortTasks()
        self.assertEqual(self.taskList.head.name, "Submit Assignment")  # Should be the earliest date listed

    def test_sort_by_urgency(self):
        self.taskList.sortUrgency()
        self.assertEqual(self.taskList.head.name, "Technical Proposal Overview 1.2.1 Programmatic")  # Should be most urgent task

    def test_sort_alphabetically(self):
        self.taskList.sortAlphabetically()
        self.assertEqual(self.taskList.head.name, "Shop for Groceries")
    
if __name__ == "__main__": # unittest.main(argv=['first-arg-is-ignored'], exit=False)
    unittest.main() 

# HW 10.1, pg. 304 - 311, # 10 - 34 (odds)

# =============================================================================

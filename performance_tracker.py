class Student:
    def __init__(self, name, marks):
        """Initialize student with a name and list of marks."""
        self.name = name
        self.marks = marks
    
    def calculate_average(self):
        """Calculate the average marks of the student."""
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

def calculate_averages(students):
    """Calculate average marks for all students."""
    averages = {}
    for name, marks in students.items():
        student = Student(name, marks)
        averages[name] = round(student.calculate_average(), 2)
    return averages

def find_top_performer(averages):
    """Identify the top performer based on the highest average marks."""
    top_student = max(averages, key=averages.get)
    return top_student

def main():
    students = {}
    
    print("Enter student data (type 'done' when finished):")
    while True:
        name = input("Enter student's name (or 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        
        try:
            marks = input(f"Enter marks for {name} (comma-separated, e.g., 85,78,92): ").strip()
            marks = [float(mark) for mark in marks.split(',')]
            students[name] = marks
        except ValueError:
            print("Invalid input. Please enter marks as numbers separated by commas.")
    
    if not students:
        print("No student data entered.")
        return
    
    # Calculate averages
    averages = calculate_averages(students)
    print("\nAverage Marks:")
    for name, avg in averages.items():
        print(f"{name}: {avg}")
    
    # Find top performer
    top_performer = find_top_performer(averages)
    print(f"\nTop Performer: {top_performer}")
main()

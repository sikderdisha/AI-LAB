import os
import random

def read_student_ids(file_path):
    """Reads student IDs from a file and returns them as a list."""
    try:
        with open(file_path, 'r') as file:
            students = [line.strip() for line in file if line.strip()]
        return students
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []

def viva_selection(students):
    """Randomly selects students for viva until all have been selected."""
    viva_counter = 1
    selected_students = []
    while students:
        student = random.choice(students)
        print(f"Viva #{viva_counter}: {student}")
        students.remove(student)
        selected_students.append(student)
        viva_counter += 1
    return selected_students

def main():
    file_path = 'student_ids.txt'
    students = read_student_ids(file_path)

    if not students:
        return

    while True:
        # Randomly select students for viva
        selected_students = viva_selection(students.copy())

        # Reset students list once all have been selected
        students = selected_students

        # Ask user if they want to repeat the viva selection
        repeat = input("\nAll students have been selected. Would you like to run the viva selection again? (yes/no): ")
        if repeat.lower() != 'yes':
            break

if __name__ == "__main__":
    main()

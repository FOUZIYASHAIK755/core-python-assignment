class Patient:
    """Class to represent a patient."""
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

    def to_dict(self):
        """Convert patient data to a dictionary."""
        return {"Name": self.name, "Age": self.age, "Disease": self.disease}

def add_patient(patients):
    """Add a new patient to the list."""
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    disease = input("Enter disease: ")
    patient = Patient(name, age, disease)
    patients.append(patient.to_dict())
    print(f"Patient {name} added successfully.")

def search_by_disease(patients, disease):
    """Search for patients with a specific disease."""
    matching_patients = [p["Name"] for p in patients if p["Disease"].lower() == disease.lower()]
    if matching_patients:
        return f"Patients with {disease}: {', '.join(matching_patients)}"
    else:
        return f"No patients found with {disease}."

def display_patients(patients):
    """Display all patient records."""
    if not patients:
        print("No patient records available.")
    else:
        print("Patient Records:")
        for patient in patients:
            print(f"Name: {patient['Name']}, Age: {patient['Age']}, Disease: {patient['Disease']}")

def main():
    patients = [
        {"Name": "Alice", "Age": 30, "Disease": "Flu"},
        {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
        {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
    ]

    while True:
        print("\nHospital Patient Management System")
        print("1. Add Patient")
        print("2. Search by Disease")
        print("3. Display All Patients")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid option.")
            continue

        if choice == 1:
            add_patient(patients)
        elif choice == 2:
            search_disease = input("Enter disease to search for: ")
            print(search_by_disease(patients, search_disease))
        elif choice == 3:
            display_patients(patients)
        elif choice == 4:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
main()

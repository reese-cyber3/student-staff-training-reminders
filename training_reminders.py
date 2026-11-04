
from datetime import date, timedelta

# STUDENT STAFF TRAINING REMINDER AUTOMATION
# Summer and Fall Training Demonstration
# Fictional student employee records

training_records = [
    {
        "name": "Jordan Smith",
        "email": "jordan@example.com",
        "semester": "Summer",
        "training": "Summer Staff Orientation",
        "due_date": "2026-06-15",
        "completed": False
    },
    {
        "name": "Taylor Johnson",
        "email": "taylor@example.com",
        "semester": "Summer",
        "training": "Summer Safety Training",
        "due_date": "2026-06-20",
        "completed": False
    },
    {
        "name": "Morgan Lee",
        "email": "morgan@example.com",
        "semester": "Fall",
        "training": "Fall Staff Orientation",
        "due_date": "2026-11-05",
        "completed": False
    },
    {
        "name": "Alex Rivera",
        "email": "alex@example.com",
        "semester": "Fall",
        "training": "Inclusion and Community Training",
        "due_date": "2026-11-10",
        "completed": True
    },
    {
        "name": "Casey Brown",
        "email": "casey@example.com",
        "semester": "Fall",
        "training": "Role Expectations Training",
        "due_date": "2026-11-04",
        "completed": False
    }
]

today = date.today()

print("=" * 50)
print("UNIVERSITY HOUSING")
print("STUDENT STAFF TRAINING REMINDERS")
print("SUMMER AND FALL TRAINING")
print("=" * 50)

for record in training_records:

    if record["completed"]:
        continue

    due_date = date.fromisoformat(record["due_date"])

    if due_date < today:
        status = "OVERDUE"
    elif due_date <= today + timedelta(days=7):
        status = "DUE SOON"
    else:
        continue

    print("\nSemester:", record["semester"])
    print("Student Staff:", record["name"])
    print("Training:", record["training"])
    print("Status:", status)

    message = (
        f"Hello {record['name']},\n\n"
        f"Our records indicate that your "
        f"{record['training']} for the "
        f"{record['semester']} semester "
        f"is not yet complete.\n\n"
        f"Please complete this training by "
        f"{record['due_date']}.\n\n"
        "Thank you for your contributions "
        "to University Housing!"
    )

    print("\nEMAIL REMINDER PREVIEW:")
    print(message)
    print("-" * 50)

print("\nTraining reminder review complete.")

#.py	Instructions	Employee following a procedure
#.json	Stored information	Employee's tracking spreadsheet
# A Python (.py) file contains instructions that tell the automation what to do.
# A JSON (.json) file stores information the automation needs to remember, such as previously generated training reminders

# =====================================================
# UNIVERSITY HOUSING
# STUDENT STAFF TRAINING REMINDER AUTOMATION
# =====================================================

import json
from datetime import date
from pathlib import Path

# -----------------------------------------------------
# 1. STUDENT STAFF TRAINING RECORDS
# -----------------------------------------------------

# Fictional records for testing.
# Replace these with approved data when authorized.

training_records = [
    {
        "name": "Jordan Smith",
        "email": "jordan@example.com",
        "supervisor_email": "supervisor@example.com",
        "semester": "Summer",
        "training": "Summer Staff Orientation",
        "due_date": "2026-06-15",
        "completed": False
    },
    {
        "name": "Taylor Johnson",
        "email": "taylor@example.com",
        "supervisor_email": "supervisor@example.com",
        "semester": "Summer",
        "training": "Summer Safety Training",
        "due_date": "2026-06-20",
        "completed": False
    },
    {
        "name": "Morgan Lee",
        "email": "morgan@example.com",
        "supervisor_email": "supervisor@example.com",
        "semester": "Fall",
        "training": "Fall Staff Orientation",
        "due_date": "2026-11-10",
        "completed": False
    },
    {
        "name": "Alex Rivera",
        "email": "alex@example.com",
        "supervisor_email": "supervisor@example.com",
        "semester": "Fall",
        "training": "Inclusion and Community Training",
        "due_date": "2026-11-10",
        "completed": True
    },
    {
        "name": "Casey Brown",
        "email": "casey@example.com",
        "supervisor_email": "supervisor@example.com",
        "semester": "Fall",
        "training": "Role Expectations Training",
        "due_date": "2026-11-04",
        "completed": False
    }
]

# -----------------------------------------------------
# 2. AUTOMATION SETTINGS
# -----------------------------------------------------

# Send student reminders 7, 3, and 1 day before deadlines.
REMINDER_DAYS = [7, 3, 1]

# Store notification history in a separate JSON file.
history_file = Path("reminder_history.json")

# -----------------------------------------------------
# 3. LOAD PREVIOUS REMINDER HISTORY
# -----------------------------------------------------

if history_file.exists():
    with open(history_file, "r") as file:
        reminder_history = json.load(file)
else:
    reminder_history = []

# Get today's date.
today = date.today()

# Count generated notifications.
student_reminders = 0
supervisor_notifications = 0

# -----------------------------------------------------
# 4. BEGIN AUTOMATED REMINDER CHECK
# -----------------------------------------------------

print("=" * 55)
print("UNIVERSITY HOUSING")
print("STUDENT STAFF TRAINING REMINDER SYSTEM")
print("=" * 55)

for record in training_records:

    # Skip employees who have completed their training.
    if record["completed"]:
        continue

    # Calculate how many days remain until the deadline.
    due_date = date.fromisoformat(record["due_date"])
    days_remaining = (due_date - today).days

    # Create a unique identifier for this requirement.
    training_id = (
        f"{record['email']}|"
        f"{record['semester']}|"
        f"{record['training']}|"
        f"{record['due_date']}"
    )

    # -------------------------------------------------
    # 5. STUDENT REMINDERS: 7, 3, AND 1 DAYS
    # -------------------------------------------------

    if days_remaining in REMINDER_DAYS:

        reminder_key = f"{training_id}|student-{days_remaining}"

        # Check whether this reminder was already generated.
        if reminder_key not in reminder_history:

            print("\nSTUDENT REMINDER")
            print("-" * 40)

            print("To:", record["email"])
            print("Student:", record["name"])
            print("Semester:", record["semester"])
            print("Training:", record["training"])
            print("Days remaining:", days_remaining)

            print("\nEMAIL PREVIEW:")
            print(f"Hello {record['name']},")

            print(
                f"\nOur records show that your "
                f"{record['training']} for the "
                f"{record['semester']} semester "
                f"is not yet complete."
            )

            print(
                f"Please complete this training by "
                f"{record['due_date']}."
            )

            print("\nThank you for supporting University Housing!")

            # Save this reminder so it is not duplicated.
            reminder_history.append(reminder_key)
            student_reminders += 1

    # -------------------------------------------------
    # 6. SUPERVISOR NOTIFICATIONS: OVERDUE TRAINING
    # -------------------------------------------------

    elif days_remaining < 0:

        supervisor_key = f"{training_id}|supervisor-overdue"

        # Check whether the supervisor was already notified.
        if supervisor_key not in reminder_history:

            print("\nSUPERVISOR OVERDUE NOTIFICATION")
            print("-" * 40)

            print("To:", record["supervisor_email"])
            print("Student:", record["name"])
            print("Training:", record["training"])
            print("Original deadline:", record["due_date"])

            print("\nNOTIFICATION PREVIEW:")

            print(
                f"{record['name']} has not completed "
                f"{record['training']}."
            )

            print(
                f"This training was due on "
                f"{record['due_date']}."
            )

            print("Please follow up with the student.")

            # Save this notification to prevent duplicates.
            reminder_history.append(supervisor_key)
            supervisor_notifications += 1

# -----------------------------------------------------
# 7. SAVE REMINDER HISTORY
# -----------------------------------------------------

with open(history_file, "w") as file:
    json.dump(reminder_history, file, indent=4)

# -----------------------------------------------------
# 8. AUTOMATION SUMMARY
# -----------------------------------------------------

print("\n" + "=" * 55)
print("AUTOMATION SUMMARY")
print("=" * 55)

print("Date checked:", today)
print("Student reminders generated:", student_reminders)
print("Supervisor notifications generated:", supervisor_notifications)

print("\nReminder history saved:", history_file)

print("\nAutomation check complete.")
print("NOTE: These are simulated messages, not actual emails.")

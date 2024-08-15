# Staff Time Off Management System

This project is a simple staff management system for a village, implemented in Python. It allows you to manage staff members, import staff data from a CSV file, sort staff members based on their experience, and generate a schedule for staff members over a number of days.

## Features

- **Add Staff Member**: Add a new staff member with their name and years of experience.
- **Import Staff**: Import staff members from a CSV file.
- **Delete Staff Member**: Remove a staff member by their name.
- **Sort Members**: Sort staff members based on their years of experience.
- **Set Schedule**: Generate a schedule for staff members over a specified number of days, with a specified number of people per day.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/village-staff-management.git
    cd village-staff-management
    ```

2. Ensure you have Python installed on your system.

## Usage

1. Create a `staff.csv` file in the root directory with the following format:
    ```csv
    Finn Bergquist,8
    Will Stienfield,6
    Rory Sargent,7
    Seth Turk,3
    ```

2. Run the script:
    ```sh
    python village.py
    ```

## Example

```python
from village import Village

# Create a Village instance
village = Village()

# Import staff from CSV
village.importStaff()

# Sort staff members by years of experience
village.sortMembers()

# Print sorted staff members
print(village.staff)

# Set a schedule for 5 days with 2 people per day
village.setSchedule(numDays=5, peoplePerDay=2)

# Print the generated schedule
print(village.schedule)

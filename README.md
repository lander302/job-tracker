# Job Application Tracker (CLI)

A lightweight, database-backed command-line interface (CLI) application built in Python to help job seekers organize, track, and manage their career opportunities. 

This project demonstrates core **CRUD (Create, Read, Update, Delete)** operations, database persistence, secure SQL parameterization, and clean terminal state management.

## Features

- **Create:** Easily add new job applications with key details (Company, Role, Date, and Status).
- **Read:** View a formatted table of all active applications with a manual screen-pause to prevent terminal buffer overrun.
- **Update:** Modify the status of any application instantly using its unique database ID.
- **Delete:** Remove accidental entries with built-in user confirmation checks.
- **Dynamic Search:** Query the database using SQL wildcards to instantly filter by Company, Role, or Status keywords.

## Tech Stack & Concepts Demonstrated

- **Language:** Python 3
- **Database:** SQLite3 (Embedded relational database)
- **Data Integrity:** Implemented parameterization (`?` placeholders) in SQL queries to inherently prevent SQL Injection attacks.
- **Error Handling:** Utilized `try-except` blocks to handle invalid data inputs (e.g., non-numerical IDs) without crashing the application.
- **Version Control:** Managed completely via Git/GitHub with structured semantic commit histories.

## Installation & How to Run

### Prerequisites
Ensure you have Python 3 installed on your machine.

### Setup Instructions
1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/lander302/job-tracker.git]

2. ```bash
    cd job-tracker

3. ```bash
    python main.py

### Future Enhancements

Graphical User Interface (GUI): Transition the project from a CLI to a desktop application using Tkinter or CustomTkinter.

Analytics Dashboard: Add visual summaries (charts/graphs) showing the percentage of applications resulting in interviews versus rejections.

Automated Reminders: Integrate email notifications to follow up on applications after 14 days of inactivity.
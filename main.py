import sqlite3
# This imports our database setup function from database.py
from database import initialize_db

def add_application(company, role, date_applied, status):
    """Inserts a new job application into the SQLite database."""
    conn = sqlite3.connect("applications.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO applications (company, role, date_applied, status)
        VALUES (?, ?, ?, ?)
    """, (company, role, date_applied, status))
    
    conn.commit()
    conn.close()
    print(f"\n[SUCCESS] Added {role} position at {company}!")

def view_applications():
    """Fetches and displays all tracked job applications."""
    conn = sqlite3.connect("applications.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM applications")
    rows = cursor.fetchall()
    conn.close()
    
    if not rows:
        print("\n[INFO] No applications tracked yet! Time to apply for some jobs.")
        return
        
    print("\n=================== CURRENT APPLICATIONS ===================")
    for row in rows:
        print(f"ID: {row[0]} | Company: {row[1]} | Role: {row[2]} | Date: {row[3]} | Status: {row[4]}")
    print("=============================================================")

def main():
    # Automatically ensure the database table exists when the app starts
    initialize_db()
    
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Add New Application")
        print("2. View All Applications")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == "1":
            company = input("Enter Company Name: ")
            role = input("Enter Job Title/Role: ")
            date_applied = input("Enter Date Applied (DD/MM/YYYY): ")
            status = input("Enter Status (e.g., Applied, Interview, Rejected, Offer): ")
            add_application(company, role, date_applied, status)
            
        elif choice == "2":
            view_applications()
            
        elif choice == "3":
            print("\nExiting tracker. Good luck with your job search!")
            break
        else:
            print("\n[ERROR] Invalid option. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
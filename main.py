import sqlite3
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
        print("\n[INFO] No applications tracked yet!")
        return
        
    print("\n=================== CURRENT APPLICATIONS ===================")
    for row in rows:
        print(f"ID: {row[0]} | Company: {row[1]} | Role: {row[2]} | Date: {row[3]} | Status: {row[4]}")
    print("=============================================================")

def update_status(app_id, new_status):
    """Updates the status of a specific application using its ID."""
    conn = sqlite3.connect("applications.db")
    cursor = conn.cursor()
    
    # Check if the ID actually exists first
    cursor.execute("SELECT * FROM applications WHERE id = ?", (app_id,))
    if not cursor.fetchone():
        print(f"\n[ERROR] Application ID {app_id} not found.")
        conn.close()
        return

    cursor.execute("""
        UPDATE applications 
        SET status = ? 
        WHERE id = ?
    """, (new_status, app_id))
    
    conn.commit()
    conn.close()
    print(f"\n[SUCCESS] Application #{app_id} status updated to '{new_status}'!")

def delete_application(app_id):
    """Deletes a specific application using its ID."""
    conn = sqlite3.connect("applications.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM applications WHERE id = ?", (app_id,))
    if not cursor.fetchone():
        print(f"\n[ERROR] Application ID {app_id} not found.")
        conn.close()
        return

    cursor.execute("DELETE FROM applications WHERE id = ?", (app_id,))
    conn.commit()
    conn.close()
    print(f"\n[SUCCESS] Application #{app_id} has been deleted.")

def main():
    initialize_db()
    
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Add New Application")
        print("2. View All Applications")
        print("3. Update Application Status")
        print("4. Delete Application")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "1":
            company = input("Enter Company Name: ")
            role = input("Enter Job Title/Role: ")
            date_applied = input("Enter Date Applied (DD/MM/YYYY): ")
            status = input("Enter Status: ")
            add_application(company, role, date_applied, status)
            
        elif choice == "2":
            # adding in text so that the user only sees the applications and must return to menu on their own accord (cleaner)
            view_applications()
            print("\n-------------------------------------------------------------")
            input("Press Enter to return to the Main Menu...")
            
        elif choice == "3":
            view_applications() # Show them the IDs first so they know what to pick
            try:
                app_id = int(input("\nEnter the ID of the application to update: "))
                new_status = input("Enter new status (e.g., Interview, Rejected, Offer): ")
                update_status(app_id, new_status)
            except ValueError:
                print("\n[ERROR] Please enter a valid numerical ID.")
                
        elif choice == "4":
            view_applications()
            try:
                app_id = int(input("\nEnter the ID of the application to DELETE: "))
                confirm = input(f"Are you sure you want to delete #{app_id}? (yes/no): ").lower()
                if confirm == "yes":
                    delete_application(app_id)
                else:
                    print("\nDeletion cancelled.")
            except ValueError:
                print("\n[ERROR] Please enter a valid numerical ID.")
            
        elif choice == "5":
            print("\nExiting tracker. Good luck with your job search!")
            break
        else:
            print("\n[ERROR] Invalid option. Please enter 1-5.")

if __name__ == "__main__":
    main()
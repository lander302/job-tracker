import sqlite3

def initialize_db():
    # Connects to the database file (it creates it automatically if it doesn't exist)
    conn = sqlite3.connect("applications.db")
    
    # A cursor lets us execute SQL commands
    cursor = conn.cursor()
    
    # Create a table to hold our job applications if it's not already there
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            role TEXT NOT NULL,
            date_applied TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)
    
    # Save (commit) the changes and close the connection
    conn.commit()
    conn.close()

# run initialize_db() ONLY if we run this file directly
if __name__ == "__main__":
    initialize_db()
    print("Database initialized successfully!")
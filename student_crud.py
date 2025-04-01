import psycopg2

DB_NAME = "postgres"
DB_USER = "postgres.rjhowuutbhmkezoowfpj"
DB_PASSWORD = "9cPciV0bF0uPYbdT"
DB_HOST = "aws-0-us-east-1.pooler.supabase.com"
DB_PORT = "5432"

def db_connection():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def create_tables():
    conn = db_connection()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS teacher (
            id SERIAL PRIMARY KEY, 
            name VARCHAR(100) NOT NULL,
            age INT NOT NULL
        );
        """)
        conn.commit()
        cursor.close()
        conn.close()
        print("TABLE CREATED")

def insert_teacher(name, age):
    conn = db_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO teacher (name, age) VALUES (%s, %s) RETURNING id", (name, age))
            teacher_id = cursor.fetchone()[0]  # Get the ID of the inserted row
            conn.commit()
            cursor.close()
            print(f"TABLE DATA INSERTED, Teacher ID: {teacher_id}")
        except Exception as e:
            print(f"Error inserting data: {e}")
        finally:
            conn.close()

def update_teacher():
    conn = db_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE teacher SET age = 20 WHERE id = 1")
            conn.commit()
            cursor.close()
            print("TABLE UPDATED")
        except Exception as e:
            print(f"Error updating data: {e}")
        finally:
            conn.close()
    else:
        print("Unable to update table, database connection failed.")

def delete_teacher():
    conn = db_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM teacher WHERE id = 1")
            conn.commit()
            cursor.close()
            print("TABLE DELETED")
        except Exception as e:
            print(f"Error deleting data: {e}")
        finally:
            conn.close()
    else:
        print("Unable to delete table, database connection failed.")

if __name__ == "__main__":
    create_tables()
    insert_teacher("Ram", 121)
    update_teacher()
    delete_teacher()

import redis
import json
import os

# Connect to the Redis database
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Check the Redis connection
try:
    if r.ping():
        print("Successfully connected to Redis!")
except redis.ConnectionError:
    print("Could not connect to Redis.")
    
# Import JSON data into Redis
def import_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            count = 0
            pipe = r.pipeline()

            for line in file:
                data = json.loads(line)
                key = f"{filename}:{count}"

                pipe.set(key, json.dumps(data))
                count += 1
                if count % 1000 == 0:
                    pipe.execute()

            pipe.execute()
            
        print(f"Successfully imported {count} records from {filename}.")

    except FileNotFoundError:
        print(f"File not found: {filename}")

    except json.JSONDecodeError:
        print(f"Invalid JSON data in {filename}")
        

# CREATE - Add a new record to Redis
def create_record(key, value):
    r.set(key, json.dumps(value))
    print(f"Record '{key}' created successfully.")

# READ - Retrieve a record from Redis
def read_record(key):
    value = r.get(key)

    if value:
        print(json.loads(value))
    else:
        print(f"Record '{key}' not found.")

# UPDATE - Modify an existing record in Redis
def update_record(key, value):
    if r.exists(key):
        r.set(key, json.dumps(value))
        print(f"Record '{key}' updated successfully.")
    else:
        print(f"Record '{key}' not found.")


# DELETE - Remove a record from Redis
def delete_record(key):
    if r.exists(key):
        r.delete(key)
        print(f"Record '{key}' deleted successfully.")
    else:
        print(f"Record '{key}' not found.")

# Display the main menu
def display_menu():
    print("\nGitHub Activity Tracker")
    print("1. Import JSON Data")
    print("2. Create a Record")
    print("3. Read a Record")
    print("4. Update a Record")
    print("5. Delete a Record")
    print("6. Exit")

# Allow users to select an option
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            filename = input("Enter JSON filename: ")
            import_json(filename)

        elif choice == "2":
            key = input("Enter record key: ")

            try:
                value = json.loads(input("Enter record value as JSON: "))
                create_record(key, value)

            except json.JSONDecodeError:
                print("Invalid JSON format. Please try again.")

        elif choice == "3":
            key = input("Enter record key: ")
            read_record(key)

        elif choice == "4":
            key = input("Enter record key: ")

            try:
                value = json.loads(input("Enter new record value as JSON: "))
                update_record(key, value)

            except json.JSONDecodeError:
                print("Invalid JSON format. Please try again.")
        elif choice == "5":
            key = input("Enter record key: ")
            delete_record(key)

        elif choice == "6":
            print("Exiting application.")
            break

        else:
            print("Invalid choice. Please try again.")

# Start the application
if __name__ == "__main__":
    main()
    

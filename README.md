# Redis Integration Group Project



## Application Description



The GitHub Activity Tracker is a Python application that uses Redis, a NoSQL key-value database, to store and manage data from the GitHub Archive dataset.



The application allows users to import JSON-formatted data and perform basic CRUD operations (Create, Read, Update, and Delete) through an interactive menu.



The application uses Redis pipelines to import large amounts of data more efficiently.



## Technologies Used



\- Python 3

\- Redis

\- redis-py (Python Redis library)

\- JSON

\- Ubuntu Linux

\- GitHub



## Installation and Setup



1\. Install Python 3 on your computer.

2\. Install and start the Redis server.

3\. Install the Python Redis library using:



&#x20;  pip install redis



4\. Download or clone this GitHub repository.

5\. Download and extract the GitHub Archive dataset.

6\. Place the JSON dataset files in the same folder as redis\_app.py.

7\. Open redis\_app.py in Python IDLE.

8\. Select Run > Run Module (F5) to start the application.



## Application Menu



The application provides the following options:



1\. Import JSON Data - Import records from a JSON file into Redis.

2\. Create a Record - Add a new record using a key and JSON value.

3\. Read a Record - Retrieve an existing record using its key.

4\. Update a Record - Modify an existing record.

5\. Delete a Record - Remove a record from Redis.

6\. Exit - Close the application.



## Current Features



\- Connects Python to a Redis database.

\- Imports JSON-formatted GitHub Archive data.

\- Uses Redis pipelines to process records in batches of 1,000.

\- Supports Create, Read, Update, and Delete operations.

\- Provides an interactive menu.

\- Handles invalid JSON input during Create and Update operations.



## Future Development



The group will implement at least three additional features to analyze and display information from the GitHub Archive dataset.






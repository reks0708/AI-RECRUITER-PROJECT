# AI Recruiter

A lightweight command-line tool that extracts recognised skills, technologies, and programming languages from resume text using a MySQL reference database.

## Overview

AI Recruiter reduces the effort required to scan resumes for known keywords. The current implementation uses a simple, database-backed keyword lookup:

1. The user enters resume text at the command line.
2. The program connects to the local `recruiter` MySQL database.
3. It loads values from the `skills`, `technologies`, and `languages` tables.
4. It compares each whitespace-separated input token with those database values.
5. It prints the matches in three categories.

This is a keyword extraction prototype, not a machine-learning or conversational AI system.

## Features

- Interactive command-line input
- MySQL-backed keyword lists
- Separate extraction of skills, technologies, and languages
- JSON-style output for easy inspection
- Seed database schema and keyword data included in [`DATABASE.sql`](DATABASE.sql)

## Project Structure

| File | Description |
| --- | --- |
| [`AI RECRUITER.py`](AI%20RECRUITER.py) | Main Python command-line program |
| [`DATABASE.sql`](DATABASE.sql) | Creates the `recruiter` database and keyword tables |
| [`REQUIREMENTS.txt`](REQUIREMENTS.txt) | Python dependency list |
| `Demo video/` | Project demonstration materials |

## Prerequisites

- Python 3.x
- MySQL Server
- A MySQL user that can create and read the `recruiter` database

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd AI-RECRUITER-PROJECT-main
```

If the repository was downloaded as a ZIP file, open a terminal in the folder containing `AI RECRUITER.py` instead.

### 2. Install the Python dependency

```bash
python -m pip install -r REQUIREMENTS.txt
```

The program requires `mysql-connector-python` to connect Python to MySQL.

### 3. Create and seed the database

Run [`DATABASE.sql`](DATABASE.sql) in MySQL Workbench or the MySQL command-line client:

```bash
mysql -u root -p < DATABASE.sql
```

The script creates the `recruiter` database and populates the `skills` and `technologies` tables. The Python program also queries a `languages` table, so create that table and add language values before running the program if it is not already present in your MySQL database.

### 4. Configure the database connection

The current connection settings are defined directly in [`AI RECRUITER.py`](AI%20RECRUITER.py):

```python
mysql.connector.connect(
    host="localhost",
    user="root",
    password="reks",
    database="recruiter",
    use_pure=True,
)
```

Update the `user`, `password`, or other connection values to match your local MySQL installation. For a real deployment, move the password to an environment variable instead of keeping it in source code.

## Usage

Start the program from the project directory:

```bash
python "AI RECRUITER.py"
```

Paste or type the resume text when prompted. Use values that exist in the database as separate whitespace-delimited words:

```text
Enter the resume info: TensorFlow MySQL Git
```

The program prints the extracted result, for example:

```text
{'skills': [], 'technologies': ['TensorFlow', 'MySQL', 'Git'], 'languages': []}
```

The exact output depends on the values stored in the database. Matching is case-insensitive, while matched input text is printed using the casing entered by the user.

## Current Limitations

- Input is split on whitespace, so multi-word entries such as `machine learning` or `data science` are not matched as complete phrases.
- The code expects the MySQL database and tables to exist before it starts.
- Database credentials are currently hard-coded in the Python file.
- The SQL file defines `skills` and `technologies`; the `languages` table must also exist for the current Python code to run successfully.
- There is no PDF/DOCX upload, graphical interface, ranking, candidate recommendation, or machine-learning model yet.

## Future Improvements

- Support phrase-aware matching for multi-word skills and technologies
- Add the missing `languages` table to the database script
- Load credentials from environment variables
- Add PDF and DOCX resume parsing
- Improve extraction with NLP and entity recognition
- Add candidate scoring and recommendation features
- Add automated tests and clearer database error handling

## Demo And Screenshots

- [Screenshots](https://drive.google.com/drive/folders/1uZ1cKru9T1TsVAZ2bKL2DMG)
- [Demo video 1](https://drive.google.com/file/d/1aZ1drLeG30Fi7Vj6V1wamjkMVoBSRI0D/view?usp=drivesdk)
- [Demo video 2](https://drive.google.com/file/d/1xirv_GrsNy5_b0EgWHrXBXp7fEUDwToJ/view?usp=drivesdk)

## Technology Stack

- Python
- MySQL
- SQL
- `mysql-connector-python`

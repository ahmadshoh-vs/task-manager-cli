# Task Manager CLI

A simple console task manager built with Python and MySQL.

## Features

- Add tasks
- List all tasks
- Mark tasks as done
- Delete tasks

## Tech Stack

- Python 3
- MySQL
- mysql-connector-python
- python-dotenv

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/ahmadshoh-vs/task-manager-cli.git
   cd task-manager-cli
   ```

2. Install dependencies:
   ```
   pip install mysql-connector-python python-dotenv
   ```

3. Create a MySQL database:
   ```sql
   CREATE DATABASE task_manager;
   ```

4. Copy `.env.example` to `.env` and fill in your MySQL password.

5. Run the app:
   ```
   python main.py
   ```

## Project Structure

- `main.py` - menu and app logic
- `database.py` - MySQL connection and queries
- `.env.example` - environment variables template
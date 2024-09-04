# Test Management System

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Database Setup](#database-setup)
- [How to Use](#how-to-use)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The **Test Management System** is a command-line application designed for managing and conducting tests. Teachers can create and manage tests with multiple-choice questions, while students can log in, take tests, and receive automatic feedback on their performance. This system facilitates efficient test administration and grading.

## Features

### Teacher Mode
- **Create Tests**: Define new tests with multiple-choice questions.
- **Manage Tests**: View and organize existing tests.

### Student Mode
- **Login and Take Tests**: Students can log in, select tests, and submit their answers.
- **Automatic Grading**: Answers are graded immediately, and results are displayed.

### Database Interaction
- **Persistent Storage**: Stores tests, questions, and student scores.
- **User Authentication**: Ensures secure access for both teachers and students.

## Technologies Used

- **Programming Language**: Python
- **Database**: MySQL
- **Database Connector**: MySQL Connector for Python

## Prerequisites

Before you begin, make sure you have the following installed:

- **Python 3.x**: Download and install Python from [Python.org](https://www.python.org/downloads/).
- **MySQL**: Install MySQL from [MySQL.com](https://dev.mysql.com/downloads/).
- **MySQL Connector for Python**: Install via pip (`pip install mysql-connector-python`).

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/test-management-system.git
cd test-management-system
```

### Step 2: Set Up the Virtual Environment

1. **Activate the Virtual Environment**:

   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```

2. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

### Step 3: Set Up MySQL Database

1. **Open MySQL Workbench or Command-Line Interface**:
2. **Create the Database**:
   ```sql
   CREATE DATABASE quiz;
   USE quiz;
   ```

3. **Create Required Tables**:
   ```sql
   CREATE TABLE accounts (
       name VARCHAR(100) PRIMARY KEY,
       pass INT NOT NULL
   );

   CREATE TABLE tests_available (
       s_no INT PRIMARY KEY AUTO_INCREMENT,
       test_name VARCHAR(100) UNIQUE NOT NULL
   );
   ```

## Usage

### Step 1: Run the Program

```bash
python code.py
```

### Step 2: Choose an Option

On starting the program, you will see the following menu:

- **Create Account**: To create a new student account.
- **Login**: To log in as a teacher or a student.
- **Exit**: To exit the application.

### Step 3: Teacher Functions

- **Create Tests**: After logging in as a teacher, you can create new tests by entering a test name, questions, options, and the correct answer.

### Step 4: Student Functions

- **Take Tests**: After logging in as a student, select a test from the list and answer the questions.
- **View Results**: Your score will be displayed immediately after submission.

## Database Setup

- **Database Structure**:
  - **`accounts` Table**: Stores student account information.
  - **`tests_available` Table**: Stores available tests.
  - **Dynamic Test Tables**: Each test has its own table for storing questions and answers, created dynamically when a test is added.

## How to Use

1. **Creating an Account**:
   - Select "Create Account" from the main menu.
   - Enter your name and password.
   - Log in to take tests.

2. **Logging In**:
   - Select "Login" from the main menu.
   - Choose between teacher or student mode.
   - Use `admin` with `2022` as credentials for teacher login.
   - Students can log in with their name and password created during account setup.

3. **Creating a Test (Teacher Only)**:
   - Log in as a teacher.
   - Follow the prompts to enter a test name, questions, options, and correct answers.

4. **Taking a Test (Student Only)**:
   - Log in as a student.
   - Choose a test and answer the questions.
   - Submit the test to view your results.

## Future Enhancements

- **Web Interface**: Develop a web-based user interface for better usability.
- **Advanced Question Types**: Add support for different question types such as true/false or fill-in-the-blank.
- **Analytics**: Provide performance analytics for teachers.

## Contributing

Contributions are welcome! To contribute, please fork the repository and submit a pull request with your changes. For larger changes or feature requests, please open an issue to discuss.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). 

import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('quiz_questions.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table to store the questions and answers

cursor.execute('''
CREATE TABLE IF NOT EXISTS DS3860 (
    id INTEGER PRIMARY KEY,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    answer TEXT NOT NULL
)
''')


# List of questions and answers
#questions = [
#    ("What is the output of the following code? print(3 + 4 * 2)", "14", "11", "10", "7", "B"),
#    ("Which of the following is a valid variable name in Python?", "2nd_variable", "first-variable", "first_variable", "first variable", "C"),
#    ("What data type is the result of type(5)?", "int", "float", "str", "None", "A"),
#    ("Which of the following methods can be used to convert a string to an integer?", "int()", "str()", "float()", "convert()", "A"),
#    ("What will be the output of the following code? x = [1, 2, 3]; x.append(4); print(x)", "[1, 2, 3]", "[1, 2, 3, 4]", "[4]", "[1, 2, 3, 4, 4]", "B"),
#    ("What is the purpose of the def keyword in Python?", "To define a variable", "To define a function", "To define a class", "To define a loop", "B"),
#    ("Which of the following will create a list in Python?", "list = (1, 2, 3)", "list = [1, 2, 3]", "list = {1, 2, 3}", "list = 1, 2, 3", "B"),
#    ("What does the len() function do?", "Returns the last element of a list", "Returns the number of elements in a list or string", "Returns the length of a string in characters", "Both B and C", "D"),
#    ("Which statement is used to stop a loop in Python?", "exit", "break", "stop", "end", "B"),
#    ("What is the correct syntax for an if statement in Python?", "if x > 5 then:", "if (x > 5):", "if x > 5:", "if x > 5 then", "C")
#]

ds3850questions = [
    ("What is the output of the following code? print('Hello' + ' World')", "Hello World", "HelloWorld", "Error", "None", "A"),
    ("Which of the following is used to define a function in Python?", "function", "def", "method", "define", "B"),
    ("What keyword is used to create a loop in Python?", "repeat", "while", "loop", "foreach", "B"),
    ("Which of the following data types is immutable?", "list", "dict", "set", "tuple", "D"),
    ("How do you start a comment in Python?", "#", "//", "/*", "--", "A"),
    ("What will be the output of the following code? print(bool(''))", "True", "False", "None", "Error", "B"),
    ("Which of the following is the correct way to create a dictionary?", "dict = []", "dict = {}", "dict = ()", "dict = ''", "B"),
    ("What function is used to read input from the user?", "input()", "read()", "scan()", "get()", "A"),
    ("What does the range() function do?", "Creates a list of numbers", "Creates a tuple of numbers", "Generates a sequence of numbers", "None of the above", "C"),
    ("Which operator is used to check if two values are equal?", "==", "=", "equals", "===", "A")
]
questions = [
    ("What function is used to calculate the average of a range of cells in Excel?", "SUM()", "AVG()", "AVERAGE()", "MEAN()", "C"),
    ("Which Excel feature allows you to visually represent data trends?", "Conditional Formatting", "Data Validation", "Charts", "Pivot Tables", "C"),
    ("What does the VLOOKUP function do?", "Looks up values in the same row", "Looks up values in the same column", "Looks up values in a table vertically", "Looks up values in a table horizontally", "C"),
    ("Which of the following is NOT a valid Excel data type?", "Text", "Number", "Boolean", "DateTimeStamp", "D"),
    ("What is the purpose of a Pivot Table in Excel?", "To sort data", "To create charts", "To summarize large data sets", "To filter data", "C"),
    ("What does the CONCATENATE function do?", "Adds numbers together", "Combines text strings", "Finds the maximum value", "None of the above", "B"),
    ("Which function would you use to count the number of cells that contain numbers?", "COUNTA()", "COUNT()", "COUNTIF()", "COUNTBLANK()", "B"),
    ("What is the shortcut key for opening the Format Cells dialog box?", "Ctrl + F", "Ctrl + 1", "Ctrl + Shift + F", "Alt + F1", "B"),
    ("Which of the following allows you to filter data in a table?", "Data Sorting", "Conditional Formatting", "Filters", "Data Validation", "C"),
    ("What does the term 'data validation' mean in Excel?", "Ensuring data is accurate", "Formatting data", "Creating charts", "Sorting data", "A")
]

# Insert questions into the database
cursor.executemany('''
INSERT INTO DS3860 (question, option_a, option_b, option_c, option_d, answer)
VALUES (?, ?, ?, ?, ?, ?)
''', questions)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database created and questions inserted successfully.")

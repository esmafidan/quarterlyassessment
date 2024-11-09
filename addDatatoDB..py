import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('quiz_questions.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table to store the questions and answers

cursor.execute('''
CREATE TABLE IF NOT EXISTS DS4220 (
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
ds4210questions = [
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
ds4210questions = [
    ("Which chart type is best for showing the relationship between two numerical variables in Tableau?", 
     "Bar Chart", "Scatter Plot", "Pie Chart", "Line Chart", "B"),
    
    ("What is the purpose of a 'Dashboard' in Tableau?", 
     "To create calculated fields", "To visualize a single chart", "To combine multiple sheets and views", "To import data sources", "C"),
    
    ("Which of the following is not an aggregate function in Tableau?", 
     "SUM", "COUNT", "GROUP", "AVG", "C"),
    
    ("What feature in Tableau enables the user to quickly swap between different views on the dashboard?", 
     "Filter", "Parameter", "Calculated Field", "Set", "B"),
    
    ("In Tableau, which feature allows you to group multiple values into a single category?", 
     "Hierarchy", "Group", "Filter", "Set", "B"),
    
    ("Which chart type is best for showing the percentage distribution of a categorical variable?", 
     "Bar Chart", "Pie Chart", "Scatter Plot", "Heat Map", "B"),
    
    ("In Tableau, what is the 'Pages' shelf used for?", 
     "Creating calculated fields", "Animating data changes over time", "Applying filters", "Grouping data", "B"),
    
    ("What is a 'Story' in Tableau?", 
     "A collection of dashboards and sheets that tells a data narrative", 
     "A single worksheet", 
     "An extension to import new data sources", 
     "A data extraction method", "A"),
    
    ("Which Tableau file type is a standalone file that contains data and all dependencies for sharing?", 
     ".tde", ".twb", ".twbx", ".tbm", "C"),
    
    ("Which Tableau function allows you to show data changes over a continuous range, such as time?", 
     "Trend Analysis", "Forecasting", "Pages Shelf", "Parameter", "C")
]

questions = [
    ("Which function in R is used to calculate the mean of a numeric vector?", 
     "sum()", "mean()", "avg()", "average()", "B"),
    
    ("What is the purpose of the 'lm()' function in R?", 
     "To calculate the mean", "To perform a t-test", "To fit a linear model", "To calculate the median", "C"),
    
    ("Which R function would you use to create a histogram?", 
     "histogram()", "barplot()", "hist()", "plot_hist()", "C"),
    
    ("What function in R provides the structure of an object, such as the data type and length?", 
     "summary()", "structure()", "str()", "typeof()", "C"),
    
    ("In R, what does the 'head()' function do?", 
     "Calculates the mean", "Displays the first few rows of a data frame", "Shows summary statistics", "Deletes the first row", "B"),
    
    ("What is the output of the R code 'seq(1, 10, by = 2)'?", 
     "A sequence of numbers from 1 to 10 with step size of 2", 
     "A sequence from 1 to 5", 
     "A random sequence", 
     "A sequence of 2s from 1 to 10", "A"),
    
    ("Which function in R would you use to perform a t-test?", 
     "t.test()", "ttest()", "t_test()", "tt()", "A"),
    
    ("Which command in R would you use to read a CSV file into a data frame?", 
     "import_csv()", "read.csv()", "csv_read()", "load_csv()", "B"),

    ("What is the purpose of the 'mutate()' function in the dplyr package?", 
     "To modify a data frame by adding or transforming variables", 
     "To delete rows", 
     "To summarize data", 
     "To merge data frames", "A"),

    ("What does the function 'install.packages()' do in R?", 
     "Loads a package into the session", 
     "Installs a package from CRAN", 
     "Updates a package", 
     "Lists all available packages", "B"),
    
]


# Insert questions into the database
cursor.executemany('''
INSERT INTO DS4220 (question, option_a, option_b, option_c, option_d, answer)
VALUES (?, ?, ?, ?, ?, ?)
''', questions)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database created and questions inserted successfully.")

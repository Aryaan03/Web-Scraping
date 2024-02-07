# cis6930sp24 -- Assignment0

Name: Aryaan Shaikh
Student ID: 3020-2476

# Assignment Descriptiom
This main aim of ths assignment is to practice extracting data from an online source, reformatting the data, and working with Python3, SQL, regular expressions, and Linux command-line tools. Specifically, the task involves extracting incident data from PDF files provided by the Norman, Oklahoma police department's website, formatting it, storing it in an SQLite database, and analyzing the data. This is a great assignment to kick start our Data Engineering course and was helped us learn more about extracting, loading and formatting of data.

# How to install
pipenv install 

## How to run
pipenv run .\assignment0\main.py --incidents "url"

![video] 
(DE-A0.gif)
The video is attached in the the repository

## Functions
#### main.py \
1. DownloadIncidents(`url`)
    • Description: 
        - Downloads/Fetches incident data from a given URL.
        - The `urllib.request` module is used to execute an HTTP request and retrieve the data.
        - Constructs a request with a custom user agent to access the provided URL.
    • Parameters: 
        - `url`(str), The URL from which the incident data is to be fetched.
    • Returns:
        - The fetched incident data.

2. ExtractData(`IncidentData`)
    • Description: 
        - This function extracts incident information from the incident PDF file.
        - Reads the incident data from a PDF using `pypdf.PdfReader` and `io.BytesIO`.
        - Extracts text from each page of the PDF and concatenates it into a single string.
    • Parameters: 
        - `IncidentData`(bytes), The incident data in PDF format.
    • Returns:
        - The extracted text from the incident data PDF.

3. CreateDB(`Normanpd`, `Tab`, `Header`)
    • Description: 
        - This function creates a new SQLite database and a table based on the provided parameters using the `sqlite3` module.
        - It will Create an SQLite table named "Tab" with specific columns for incident details like time, number, location, nature, and origin.
        - It Drops the table if it already exists and Creates a new table with the schema based on the provided header information.
    • Parameters: 
        - `Normanpd`(str); The name of the SQLite database file.
        - `Tab`(str); The name of the table to be created.
        - `Header`(list); The header information for the table.
    • Returns:
        - None

4. PopulateDB(`Normanpd`, `Tab`, `Con`)
    • Description: 
        - This function populates the SQLite database with the provided data using the `sqlite3` module.
        - Constructs an SQL query to insert the provided data into the specified table.
        - Executes the query for each set of data to be inserted into the table.
    • Parameters: 
        - `Normanpd`(str); The name of the SQLite database file.
        - `Tab`(str); The name of the table to be created.
        - `Header`(list); The data to be inserted into the table.
    • Returns:
        - None

5. Insert(`Information`)
    • Description: 
        - This function Inserts incident information into the database.
        - Handles cases where incomplete or erroneous data is encountered.
    • Parameters: 
        - `Information` (list); List of incident information.
    • Returns:
        - The filtered and inserted information.

6. Status(`Normanpd`, `Tab`):
    • Description: 
        - This function retrieves and displays the status of incidents in the database using SQL queries and the `sqlite3` module.
        - Retrieves and prints a list of incidents and their occurrence count, sorted alphabetically by nature, from the specified database table.
    • Parameters: 
        - `Normanpd`(str); The name of the SQLite database file.
        - `Tab`(str); The name of the table to be created.
    • Returns:
        - None

7. Calculate(`Normanpd`, `Tab`):
    • Description: 
        - This function cexecutes an SQL query to count the number of entries in the specified database table and returns the count.
        - This function also displays all the rows in the incident table by executing a SQL query using the `sqlite3` module.
        - It retrieves and prints all rows from the specified database table.
    • Parameters: 
        - `Normanpd`(str); The name of the SQLite database file.
        - `Tab`(str); The name of the table to be created.
    • Returns:
        - `Count`(int); The number of entries in the incident table.

8. main(`url`):
    • Description: 
        - Calls the `RetrieveIncidents(url)` function to download incident data from the provided URL.
        - Calls the `ExtractData()` function to extract text from the downloaded incident data PDF.
        - Parses the extracted text to obtain relevant information such as incident time, number, location, nature, and origin.
        - Creates a new SQLite database using the `CreateDB` function Populates the database with the parsed information using the `PopulateDB` function.
        - Calls the `Status` function to retrieve and display the status of incidents in the populated database.
        - Defines a command-line interface using `argparse`.
        - Parses the command-line arguments, specifically the `--incidents` argument for the URL.
    • Parameters: 
        - `url`(str); The URL from which the incident data is to be fetched.
   
## Database Development

    1. Connect to the Database (`CreateDB()`):
        - Establish a connection to an SQLite database named "normanpd.db" using the `sqlite3` module.
        - Create a cursor to interact with the database.

    2. Database Creation:
        - A SQLite database is created to store the incident data.
        - The structure of the incident table is defined based on the extracted header information.

    3. Data Population:
        - The extracted incident data is inserted into the SQLite database.
        - Each row of incident data corresponds to an entry in the database table.

    4. Data Analysis:
        - The script provides functionality to query the database for statistical analysis of incident data.
        - Users can retrieve counts of incidents based on their nature.

    5. Command-line Interface:
        - The script can be executed from the command line.
        - Users provide the URL of the incident summary PDF file as a command-line argument.
        

Below is a breif overiew on how to estabish connection, take data, insert, query and close the connection to database:
        
    - Begin by establishing a connection to the "normanpd.db" SQLite database using the sqlite3 module and create a cursor to interact with it.

    - Next, craft an SQL statement to generate a table named "incidents" within the database, outlining the columns like incident_time, incident_number, incident_location, nature, and incident_ori, assigning suitable data types to each, such as TEXT.

    - Proceed to populate the "incidents" table by iterating through each incident entry in the extracted data. For each entry, formulate an SQL INSERT statement to add the data into the table, executing it with the cursor, and confirming the changes.

    - Utilize an SQL query to gather the incident count grouped by nature from the "incidents" table. Arrange the results by count in descending order and then alphabetically by nature.

    - Display the sorted incident data in the format "nature | count," providing a clear overview of the incident nature alongside the corresponding count.

    - Retrieve all incident data by executing an SQL query to fetch all information from the "incidents" table, returning a list of tuples representing each incident.

    - Finally, if the "incidents" table already exists, execute an SQL statement to remove it, preventing conflicts when creating a new table.



## Bugs and Assumptions
...

1. There should be some entry in atleast one column of the every row.
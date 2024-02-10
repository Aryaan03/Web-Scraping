# CIS6930sp24 -- Assignment0

Name: Aryaan Shaikh <br>
Student ID: 3020-2476

## Contact

Email - am.shaikh@ufl.edu <br>
Project Link: https://github.com/Aryaan03/cis6930sp24-assignment0


## Assignment Description
This is the 1st project assignment for the CIS6930 Data Engineering course. The main aim of this assignment is to practice precise extraction of data from an online source, reformatting it, store it in a SQLite database. The expected outcome of this assignment is printing a list with a selected columnar entity along with the number of times the entity has occurred in the source document. More specifically, this assignment involves extracting incident data from PDF files provided by the Norman, Oklahoma police department's [website](https://www.normanok.gov/public-safety/police-department/crime-prevention-data/department-activity-reports). The incident data like Date/Time, Incident Number, Location, Nature, Incident ORI should be extracted from the pdf file and stored into a SQLite database according to their respective fields. Resulting output, the list of all the data in the 'Nature' (Fight, Stroke, Hit and Run, etc) should be sorted by the total number of incidents and printed in alphabetical order along with the number of times it has happened separated by the pipe character. (example: Hit and Run|7). <br> 

This assignment underscores the importance of data extraction in the data engineering domain, as it lays the groundwork for understanding how to manipulate and organize raw data for analysis and interpretation. By categorizing incidents, students gain insight into how data can be structured and utilized effectively. This assignment serves as a foundational step toward mastering the multifaceted skills essential in data engineering, encompassing data collection, validation, storage, security, and processing to ensure data accessibility, reliability, and timeliness for end-users. To Conclude, this is a great assignment to kick start our Data Engineering course and has helped us to learn more about extracting, loading and formatting of data.<br>

## How to install
```
pipenv install 
```

## How to run
Project can be run by using any of the given commands:
```
pipenv run python assignment0/main.py --incidents "<url>"
```
```
python assignment0/main.py --incidents "<url>"
```

For testing use command:
```
python -m unittest .\tests\test_download.py

```

## Demo Implementation 

video link: [Data Engineering Assignment0 demo](https://github.com/Aryaan03/cis6930sp24-assignment0/blob/main/DE-A0_demo.mp4) <br>
![](https://github.com/Aryaan03/cis6930sp24-assignment0/blob/main/DE-A0_demo.gif)
The video is also available in the repository.

## Functions
#### main file
1. `RetrieveIncidents(url)`<br>
    • Description: <br>
        &emsp;- Downloads/Fetches incident data from a given URL.<br>
        &emsp;- The `urllib.request` module is used to execute an HTTP request and retrieve the data.<br>
        &emsp;- Data is stored locally in a local variable and not at any specific location (tmp folder) for using it for both making a SQL database and also for retreiving data.<br>
        &emsp;- Constructs a request with a custom user agent to access the provided URL.<br>
    • Parameters: <br>
        &emsp;- `url`(str), The URL from which the incident data is to be fetched.<br>
    • Returns:<br>
        &emsp;- The fetched incident data.<br>

2. `ExtractData(IncidentData)`<br>
    • Description: <br>
        &emsp;- This function extracts incident information from the incident PDF file using Pypdf.<br>
        &emsp;- Reads the incident data from a PDF using `pypdf.PdfReader` and `io.BytesIO`.<br>
        &emsp;- Extracts text from each page of the PDF using the layout mode and concatenates it into a single string.<br>
    • Parameters: <br>
        &emsp;- `IncidentData`(bytes), The incident data in PDF format.<br>
    • Returns:<br>
        &emsp;- The extracted text from the incident data PDF.<br>

3. `CreateDB(Normanpd, Tab, Header)`<br>
    • Description: <br>
        &emsp;- This function creates a new SQLite database and a table based on the provided parameters using the `sqlite3` module.<br>
        &emsp;- It will create an SQLite table named "Tab" with specific columns for incident details like known previously like time, number, location, nature, and origin.<br>
        &emsp;- It Drops the table if it already exists and Creates a new table with the schema based on the provided header information.<br>
    • Parameters: <br>
        &emsp;- `Normanpd`(str); The name of the SQLite database file.<br>
        &emsp;- `Tab`(str); The name of the table to be created.<br>
        &emsp;- `Header`(list); The header information for the table.<br>
    • Returns:<br>
        &emsp;- None<br>

4. `PopulateDB(Normanpd, Tab, Con)`<br>
    • Description: <br>
        &emsp;- This function populates the SQLite database with the provided data using the `sqlite3` module.<br>
        &emsp;- Constructs an SQL query to insert the provided data using the `INSERT` query into the specified table.<br>
        &emsp;- Executes the query for each set of data to be inserted into the table.<br>
    • Parameters: <br>
        &emsp;- `Normanpd`(str); The name of the SQLite database file.<br>
        &emsp;- `Tab`(str); The name of the table to be created.<br>
        &emsp;- `Header`(list); The data to be inserted into the table.<br>
    • Returns:<br>
        &emsp;- None<br>

5. `Insert(Information)`<br>
    • Description: <br>
        &emsp;- This function processes the incident information into the database.<br>
        &emsp;- It initializes a list and appends the rows in it.<br>
    • Parameters: <br>
        &emsp;- `Information` (list); List of incident information.<br>
    • Returns:<br>
        &emsp;- The filtered and inserted information.<br>

6. `Status(Normanpd, Tab)`<br>
    • Description: <br>
        &emsp;- This function retrieves and displays the status of incidents in the database using SQL queries and the `sqlite3` module.<br>
        &emsp;- It Retrieves and prints a list of incidents and their occurrence count, sorted alphabetically by nature, from the specified database table.<br>
    • Parameters: <br>
        &emsp;- `Normanpd`(str); The name of the SQLite database file.<br>
        &emsp;- `Tab`(str); The name of the table to be created.<br>
    • Returns:<br>
        &emsp;- None<br>
        
7. `Calculate(Normanpd, Tab)`:<br>
    • Description: <br>
       &emsp;- This function executes an SQL query to count the number of entries in the specified database table and returns the count.<br>
       &emsp;- This function also iterstes through all the rows and prints it from the incident table by executing a SQL query using the `sqlite3` module.<br>
       &emsp;- It retrieves and prints all rows from the specified database table. <br>
    • Parameters: <br>
       &emsp;- `Normanpd`(str); The name of the SQLite database file.<br>
       &emsp;- `Tab`(str); The name of the table to be created.<br>
    • Returns:<br>
       &emsp;- `Count`(int); The number of entries in the incident table.<br>

8. `main(url)`:<br>
    • Description: <br>
        &emsp; - Invokes all other functions. <br>
        &emsp;- Calls the `RetrieveIncidents(url)` function to download incident data from the provided URL.<br>
        &emsp;- Calls the `ExtractData()` function to extract text from the downloaded incident data PDF.<br>
        &emsp;- Parses the extracted text to obtain relevant information such as incident time, number, location, nature, and origin. <br>
        &emsp;- Creates a new SQLite database using the `CreateDB` function Populates the database with the parsed information using the `PopulateDB` function.<br>
        &emsp;- Calls the `Status` function to retrieve and display the status of incidents in the populated database.<br>
        &emsp;- Defines a command-line interface using `argparse`.<br>
        &emsp;- Parses the command-line arguments, specifically the `--incidents` argument for the URL.<br>
    • Parameters:<br>
        &emsp; - `url`(str); The URL from which the incident data is to be fetched.<br>
    • Returns:<br>
         &emsp; - List of Nature of incidents along with the number of times it occurred long with the number of times it has happened separated by the pipe character.
        
   
## Database Development

    1. Database Creation:
        - A SQLite database is created to store the incident data.
        - Database is created using `CreateDB()` function.
        - The structure of the incident table is defined based on the extracted header information.
        - Data is stored in a local variable so that it can not only be used for retrieving data but also for populating the databse.

    2. Connect to the Database (`CreateDB()`):
        - Establish a connection to an SQLite database named "normanpd.db" using the `sqlite3` module.
        - Create a cursor to interact with the database.

    3. Data Population(`PopulatedDB()` and `Insert()`:
        - The extracted incident data is inserted into the SQLite database usind `PopulatedDB()` function.
        - Queries are used to execute SQL statements for creating table and headers.
        - For insertion INSERT statement is used.
        - Implementing the INSERT command using the cursor.
        - Each row of incident data corresponds to an entry in the database table.

    4. Data Status and Printing:
        - The script provides functionality to query the database for statistical analysis of incident data.
        - Running an SQL query to obtain the number of incidents categorized by nature from the 'incidents' table. 
        - Ordering results by count (descending) and then by alphabetically by nature.   
        - Display type of nature of incident along with their respective counts seperated by a pipe '|' symbol. 
        
    5. Command-line Interface:
        - The script can be executed from the command line.
        - Users provide the URL of the incident summary PDF file as a command-line argument.
  
    6. Delete and Create new table
        - Run an SQL command to delete the 'incidents' table if it's already exists and create a new table
        

Below is a brief overview on how to establish connection, take data, make table, insert, query and close the connection to database:
        
    -> Begin by establishing a connection to the "normanpd.db" SQLite database using the sqlite3 module and create a cursor to interact with it.
    -> Next, craft an SQL statement to generate a table named "incidents" within the database, outlining the columns like incident_time, incident_number, incident_location, nature, and incident_ori, assigning suitable data types to each, such as TEXT.
    -> Proceed to populate the "incidents" table by iterating through each incident entry in the extracted data. For each entry, formulate an SQL INSERT statement to add the data into the table, executing it with the cursor, and confirming the changes.
    -> Utilize an SQL query to gather the incident count grouped by nature from the "incidents" table. Arrange the results by count in descending order and then alphabetically by nature.
    -> Display the sorted incident data in the format "nature | count," providing a clear overview of the incident nature alongside the corresponding count.
    -> Retrieve all incident data by executing an SQL query to fetch all information from the "incidents" table, returning a list of tuples representing each incident.
    -> Finally, if the "incidents" table already exists, execute an SQL statement to drop it, preventing conflicts when creating a new table.

## Testing

Testing using pytest & mocking is done to make sure that all the functions are working independently and properly. Testing is crucial for early bug detection and maintaining code quality. Testing units of code encourages modular, understandable code and integrates seamlessly into continuous integration workflows, boosting integrity. Ultimately, all major functions like Retrieve, ExtractData, CreateDB and more are tested if they are functioning properly. For example. test_create verifies if a database and table is created or not. 


    1. `test_Retrieve`:
        - Utilizes mocking to validate individual functions.
        - Uses mock versions of urllib.request.urlopen to simulate fetching data from a URL.
        - Dummy data ('Some Dummy data') is provided instead of actual network requests.
        - The URL variable serves as input for testing the fetchIncidents function.

    2. `test_Extraction`:
        - Mocks the PDF library to control page content.
        - Creates dummy pages with predefined text for testing text extraction.
        - Ensures the extracted text matches expected output, validating correct text extraction without real PDFs.

    3. `test_Create`:
        - Uses mocking to verify the createdb function successfully creates a database and table.
        - Checks if sqlite3.connect is called with correct arguments.
        - Verifies expected SQL queries are executed on the mock cursor.
        - Ensures commit and close methods are called on the mock connection.

    4. `test_Populate`:
        - Mocks sqlite3.connect to verify data insertion calls and expected queries.
        - Validates if commit and close occur on the mock connection.
        - Verifies data insertion follows table format, ensuring correct function behavior without a real database.

    5. `test_Status`:
        - Mocks the database connection to return desired data.
        - Captures printed output of the status function.
        - Compares captured output to expected string, verifying correct output generation using mocked data.

## Bugs and Assumptions

• Assuming that the structure of the PDF files provided by the Norman, Oklahoma police department remains consistent across different reports. If the structure changes, it could break the extraction process. <br>
• A large PDF files or a high volume of data exceeding system memory or processing limits, can lead to performance degradation or application crashes.<br>
• Not all columns of a row can be empty at the same time. There should be some entry in atleast one cell of every row.<br>
• All fields, excluding the 'Nature' field will consist of alphanumeric characters.<br>
• Assuming that empty entries are only possible in the 'Nature' column. If there are empty entries in any other column it might break the extraction.
• Known bug: Some pdfs that have unsual formatting are not able to parse. 
• If there are multiple lines in a single cell, then only the first line will be parsed. There is no such cases where the 'Nature' column had multiple lines of text. So, it was not tested. But, if it has, this can be a potential bug.
• No bugs apart from those mentioned above are known/identified.


## Version History

• 0.1 <br>
   &emsp;&emsp; -> Initial Release

## License

This project is licensed by Aryaan Shaikh©2024.

## Acknowledgments

• [Christan Grant](https://github.com/cegme)- Providing the problem Statement <br>
• [Yifan Wang](https://github.com/wyfunique)- Testing our code<br>
• [Pipenv: Python Dev Workflow for Humans](https://pipenv.pypa.io/en/latest/)- Helped me in Installing Pipenv <br>
• [Extract Text from a PDF](https://pypdf.readthedocs.io/en/latest/user/extract-text.html)- Helped me in extracting text in a fixed width format and changing cells<br>

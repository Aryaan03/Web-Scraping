import re
import argparse
import pypdf
import urllib.request
import sqlite3
import io
## Import All the necessary Packages

def RetrieveIncidents(url):
# Function to Retive incident data from the given URL
    headers = {
        # Initialize headers to mimic user agent
        'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    }
    # Open the URL with the provided headers and request to read the data
    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()
    return data

def ExractData(IncidentData):
# Function to extract incidents from PDF file

    # Read PDF data from BytesIO object
    ReadPDF = pypdf.PdfReader(io.BytesIO(IncidentData))
    # Initialize empty string to store extracted text
    ExtractText = ""

    # Iterate through every page in PDF file
    for PageNo in range(len(ReadPDF.pages)):
        # Add a new line before each page's text
        ExtractText += "\n"
        page = ReadPDF.pages[PageNo]

        # Extracting text from the page
        page_text = page.extract_text(extraction_mode="layout")
        #Appending the result with the extracted text
        ExtractText += page_text
   
    # Return the extracted text
    return ExtractText

def CreateDB(Norman, Tab, Header):
# Function to create a new SQLite database and table
    
    con = sqlite3.connect(Norman) # Connect to SQLite database
    cur = con.cursor() # Create a cursor object for database operations
    
    # Drop the table if it already exists
    cur.execute("DROP TABLE IF EXISTS {};".format(Tab))

# Create a new table 
    MakeTable = "CREATE TABLE {} (incident_time TEXT, incident_number TEXT, incident_location TEXT, nature TEXT, incident_ori TEXT);".format(Tab)
    cur.execute(MakeTable)
    
    con.commit() # Commit changes to the database
    con.close() # Close the database connection

def PopulateDB(Norman, Tab, Line):
# Function to populate the SQLite database with incident parsed data
    
    con = sqlite3.connect(Norman) # Connect to SQLite database
    cur = con.cursor() # Create a cursor object for database operation

    #Insert data in table
    AddQ = "INSERT INTO {} VALUES ({});".format(Tab, ', '.join(['?']*len(Line[0])))

    # Iterate through each row of data and insert it into the table
    for DL in Line:
        if len(DL) < 5 :
            tmp = [''] * 5
            cur.execute(AddQ, tmp)
        else :
            cur.execute(AddQ, DL)

    cur.connection.commit() # Commit changes to the database

    con.commit()
    con.close() # Close the database connection


def Insert(Information):
# Function to insert and process information
    
    # Initialize a list to store latest table entry
    Latest = []
            
    for Row in Information:
        # Append rows with length greater than 1 to the Latest list
        if len(Row) > 1:
            Latest.append(Row)

    # Return the latest information
    return Latest

def Status(Norman, Tab):
# Function to display status
    
    con = sqlite3.connect(Norman) # Connect to SQLite database
    cur = con.cursor() # Create a cursor object for database operations
    
     # SQL query to select nature and count of incidents grouped by nature
    Qur = """
        SELECT Nature, COUNT(*) AS IncidentCount FROM {} GROUP BY Nature ORDER BY CASE WHEN Nature = '' THEN 1 ELSE 0 END,  IncidentCount DESC, Nature""".format(Tab)
    
    # Execute the SQL query
    cur.execute(Qur)
    
    rows = cur.fetchall() # Fetch all rows from the executed query
    
    con.close()
    
    for row in rows:
       print("{}|{}".format(row[0], row[1]))
        
def Calculate(Norman, Tab):
# Function to view database content
    con = sqlite3.connect(Norman) # Connect to SQLite database
    cur = con.cursor() # Create a cursor object for database operations
    
    # Execute SQL query to select all rows from the incident_table
    cur.execute('SELECT * FROM incident_table')

    rows = cur.fetchall() # Fetch all rows from the executed query
    
    # Iterate through each row and print it
    for row in rows:
        print(row)
    
    # Close the cursor and the database connection
    cur.close()
    con.close()

    db_connection = sqlite3.connect(Norman)
    cur = db_connection.cur()

    # Execute SQL query to get the count of rows in the incident_table
    cur.execute(f"SELECT COUNT(*) FROM {Tab};")
    
     # Fetch the count of rows
    count = cur.fetchone()[0]

    # Close the database connection
    db_connection.close()

    # Return the count of rows in the incident_table
    return count       

def main(url):
    
    # Call function for Retrieving incident data from the provided URL
    incident_data = RetrieveIncidents(url)

    # Call function for Extracting incident details from the PDF data
    incidents = ExractData(incident_data)
    
    # Split the extracted text into lines and extract header information
    Next = incidents.strip().split('\n')
    Header = re.split(r'\s{2,}', Next[2].strip())
    # Extract information from the remaining lines (excluding header and footer)
    Information = [re.split(r'\s{2,}', line.strip()) for line in Next[3:-1]]
    
    # Insert the extracted information into the database
    Latest = Insert(Information)
    
    
    Norman = "resources/normanpd.db"
    Tab = "incident_table"
    
    # Call function for creating new database
    CreateDB(Norman, Tab, Header)

    # Call function for inserting data
    PopulateDB(Norman, Tab, Latest)

    # Display the status of incidents stored in the database
    Status(Norman, Tab)

    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True, 
                         help="Incident summary url.")
     
    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)

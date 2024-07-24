import unittest
import io
import web.main as web
import sys
from unittest.mock import Mock, patch

## Import all the necessary libraries

class TestReterieve(unittest.TestCase):
# Define a test class that inherits from unittest.TestCase
   
    # Decorate the test method with patch to mock the 'urllib.request.urlopen' and 'urllib.request.Request' functions
    @patch('urllib.request.urlopen')
    @patch('urllib.request.Request')
    def test_Retrieve(me, ask, mdo):
        mdo.return_value.read.return_value = b'Dummy'
        # Mock the return value of the read function of the urlopen object

        url = 'https://www.normanok.gov/sites/default/files/documents/2024-02/2024-02-04_daily_incident_summary.pdf'
        out = web.RetrieveIncidents(url)

        # Verifying if urlopen was called with the provided URL and headers
        ask.assert_called_once_with(url, headers={'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"})
        # Verifying if Request was called with the return value of urlopen
        mdo.assert_called_once_with(ask.return_value)
     
        # Verifying if the output matches the expected 'Dummy' content
        me.assertEqual(out, b'Dummy')
        
    @patch('pypdf.PdfReader')
    def test_Extraction(me, check):
        """Is the Projct verfied for extracting text properly and independently"""
        # Setting up mocked PDFReader object and its return values for text extraction
        IncidentData = b'Tablular Information' 
        exp = "\nData from A\nData from B"

        Dummy1 = unittest.mock.MagicMock()
        Dummy1.extract_text.return_value = "Data from A"
        Dummy2 = unittest.mock.MagicMock()
        Dummy2.extract_text.return_value = "Data from B"

        check.return_value.pages = [Dummy1, Dummy2]
        
        # Calling ExtractData and comparing the output with expected text
        og = web.ExractData(IncidentData)
        me.assertEqual(og, exp)
    
    @patch('sqlite3.connect')
    def test_Create(me, dum):

        # Testing the creation of a database table
        Norman= 'check.db'
        Tab = 'verify'
        Header = 'incident_time TEXT, incident_number TEXT, incident_location TEXT, nature TEXT, incident_ori TEXT'

        web.CreateDB(Norman, Tab, Header)

        # Verifying if the connection to the database was established
        dum.assert_called_once_with(Norman)

        # Verifying if table creation and dropping statements were executed
        lat = dum.return_value
        look = lat.cursor.return_value

        # Assert that table creation SQL commands are executed
        look.execute.assert_has_calls([
            unittest.mock.call("DROP TABLE IF EXISTS {};".format(Tab)),
            unittest.mock.call("CREATE TABLE {} (incident_time TEXT, incident_number TEXT, incident_location TEXT, nature TEXT, incident_ori TEXT);".format(Tab))
        ])

        # Assert that changes are committed and connection is closed
        lat.commit.assert_called_once()
        lat.close.assert_called_once()
        
    @patch('sqlite3.connect')
    def test_Populate(self, dum):
        Norman = 'check.db'
        Tab = 'verify'
        # Data to be inserted into the database
        Line = [
            ['6/2/2024', 'id56', '4000 BLVD, Gnv, FL 32608', 'Big', 'Reitz'],
            ['2/2/2024', 'id78', 'Stonridge 38th Street, Gnv, FL 32608', 'Small', 'Hallway']
        ]

        web.PopulateDB(Norman, Tab, Line)

        lat = dum.return_value
        # Get the cursor object from the database connection
        look = lat.cursor.return_value

        # Assert that insertion SQL commands are executed for each data row
        exp = [
            unittest.mock.call("INSERT INTO {} VALUES (?, ?, ?, ?, ?);".format(Tab), Line[0]),
            unittest.mock.call("INSERT INTO {} VALUES (?, ?, ?, ?, ?);".format(Tab), Line[1])
        ]
        look.execute.assert_has_calls(exp)

        # Assert that changes are committed and connection is closed
        lat.commit.assert_called_once()
        lat.close.assert_called_once()
        
    @patch('sqlite3.connect')
    def test_Status(me, dum):
        """Is the Project verfied for calculating and printing nature properly and independently"""
        Norman = 'check.db'
        Tab = 'verify'
        # Sample output data from the database
        out = [('Fight', 89), ('Hit and Run', 56)]

        lat = dum.return_value.cursor.return_value # Get the cursor object from the database connection
        lat.fetchall.return_value = out # Mock the fetchall method to return sample output data

        # Redirect stdout to capture print output
        og = io.StringIO()
        sys.stdout = og

        # Call the function under test
        web.Status(Norman, Tab)

        sys.stdout = sys.__stdout__

        look = "Fight|89\nHit and Run|56\n"

        # Assert that the printed output matches the expected output
        me.assertEqual(og.getvalue(), look)
        

if __name__ == '__main__':
    unittest.main()

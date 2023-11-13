# Extracting Data from XML

# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.


# Actual data: http://py4e-data.dr-chuck.net/comments_1885212.xml (Sum ends with 69)
# You do not need to save these files to your folder since your program will read the data directly from the URL.
import urllib.request
import xml.etree.ElementTree as ET

url = input("Enter location: ")
if not url:
    url = (
        "http://py4e-data.dr-chuck.net/comments_42.xml"  # Use a default URL for testing
    )

print("Retrieving", url)
response = urllib.request.urlopen(url)
data = response.read()

tree = ET.fromstring(data)

# Initialize a variable to store the sum of counts
sum_counts = 0

# Iterate through all comment tags
for comment in tree.findall(".//comment"):
    # Find the count tag within each comment and extract its text
    count_text = comment.find("count").text

    # Convert the count text to an integer and add it to the sum
    sum_counts += int(count_text)

# Print the count and sum of counts
print("Count:", len(tree.findall(".//comment")))
print("Sum:", sum_counts)

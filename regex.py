import re
string ="web scraping in python web scraping in python"

result = re.match(r"web", string , re.IGNORECASE)
#print (result)

result2 = re.search( r"web" , string , re.MULTILINE)
print (result2)
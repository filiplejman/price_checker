import requests
from bs4 import BeautifulSoup


request_url = "http://www.google.com"
response = requests.get(request_url)

print(response.content)
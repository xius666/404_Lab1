import urllib.request
import requests
print(requests.__version__)
request_google= requests.get("https://www.google.com")
print("header of the google page:")
print(request_google.headers)


request=requests.get("https://raw.githubusercontent.com/xius666/404_Lab1/main/script.py") 
print(request.text)
urllib.request.urlretrieve("https://raw.githubusercontent.com/xius666/404_Lab1/main/script.py", "downloadfile.py")
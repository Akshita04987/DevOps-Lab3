from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def home():
    if os.getenv("NEW_FEATURE", "off") == "on":
        return "<h1>New Feature is ON</h1>"
    return "<h1>Old Version</h1>"

app.run(host="0.0.0.0", port=5000)

import datetime
from flask import Flask, render_template

app = Flask(__name__)
"""
template engines:
- IF statements, For loops, blocks (chaining of templates)
- NO BUSINESS LOGIC!!!!

HEROKU DEPLOYMENT
procfile - which server to run and which file to run
requirements.txt - which libraries to install
runtime.txt - which language version to run
"""


@app.route("/")
def Index():
    name = "Dejan"
    cities = ["Ljubljana", "Maribor", "Celje"]
    # cities = None
    year = datetime.datetime.now().year
    return render_template("index.html", name=name, cities=cities, year=year)


@app.route("/about")
def About():
    return render_template("about.html")


if __name__ == '__main__':
    app.run()

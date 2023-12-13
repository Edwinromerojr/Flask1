from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", content=["edwin", "popo", "wiwin"])

@app.route("/<name>")
def user(name):
    return render_template("index.html", content=name, r=2)

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin!"))

if __name__ == "__main__":
    app.run(debug=True)
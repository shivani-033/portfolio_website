from flask import Flask , render_template, request,redirect , url_for

app = Flask(__name__)
@app.route("/")
def home():
    return  render_template('home.html')
@app.route("/about.html" )
def about():
    return render_template("about.html")
@app.route("/contact.html" )
def contact():
    return render_template("contact.html")
@app.route("/project.html" )
def project():
    return render_template("project.html")

if __name__ == "__main__":
    from os import environ
    port = int(environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=port)


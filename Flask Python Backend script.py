from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

# Route for the homepage
@app.route("/")
def index():
    return render_template("index.html")

# Route to handle contact form submissions
@app.route("/submit_contact", methods=["POST"])
def submit_contact():
    if request.method == "POST":
        # Get form data
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        
        # Save the data to a file (or use a database)
        with open("contact_logs.txt", "a") as file:
            file.write(f"Name: {name}\nEmail: {email}\nMessage: {message}\n\n")
        
        # Redirect to a thank you page
        return redirect(url_for("thank_you"))

# Route for the thank you page
@app.route("/thank_you")
def thank_you():
    return "<h1>Thank you for reaching out! We'll get back to you soon.</h1>"

if __name__ == "__main__":
    app.run(debug=True)

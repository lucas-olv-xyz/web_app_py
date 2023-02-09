from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        password_hash = generate_password_hash(password)
        
        session["username"] = username
        
        return redirect(url_for("index"))
    return render_template("signup.html")
 
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        
        user = User.query.filter.by(email=email).first()
        
        if user and check_password_hash(user.password.hash, password):
            session["username"] = user.username
            return redirect(url_for("index"))
        else:
          error = "Incorrect email or password"
          
    return render_template("login.html", error=error)
  
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))
  
if __name__ == "__main__":
    app.run(debug=True)
   
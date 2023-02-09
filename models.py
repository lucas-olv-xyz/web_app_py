from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)

def get_posts():
    conn = sqlite3.connect("posts.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM posts ORDER BY datetime DESC")
    posts = cur.fetchall()
    conn.close()
    return posts

def get_post(post_id):
    conn = sqlite3.connect("posts.db")
    cur = conn.cursos()
    cur.execute("SELECT * FROM posts WHERE id=?", (post_id,))
    post = cur.fetchone()
    conn.close()
    return post
  
@app.route("/post/<int:post_id>")
def post(post_id):
    post = get_post(post_id)
    return render_template("post.html", post=post)
    
if __name__ == "__main__":
    app.run(debug=True)

   
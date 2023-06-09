from flask import Flask
from flask import request,redirect,url_for
from sqlalchemy import Column, ForeignKey, Integer, Unicode, LargeBinary
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String
from flask import render_template, request

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db=SQLAlchemy(app)

class PostDb(db.Model):
     __tablename__="PostDb"
     id=db.Column(db.Integer,primary_key=True)
     title=db.Column(db.String)
     body=db.Column(db.Text)
     image = db.Column(LargeBinary, nullable = True)


@app.route("/posts",endpoint="posts.get")
def get_all_posts():
      posts=PostDb.query.all()
      return render_template("posts/post.html",posts=posts)




@app.route("/post/<int:id>" ,endpoint="post.show")
def show_post(id):
     post=PostDb.query.get_or_404(id)
     return render_template("posts/show.html",post=post)

     

@app.route("/post/create",endpoint="post.create" ,methods = ["GET", "POST"])
def create_product():
    if request.method=="POST":
        print(request.form)
        post_title= request.form["title"]
        post_body = request.form["body"]
        post_image = request.form["image"]
        post = PostDb(title=post_title, body= post_body, image=post_image)
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('posts.get'))

    return render_template("posts/create.html")

@app.route("/post/<int:id>/delete", endpoint="post.delete")
def delete_product(id):
    post= PostDb.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('posts.get'))



@app.route("/post/<int:id>/update",endpoint="post.update" ,methods = ["GET", "POST"])
def update_product(id):
     post= PostDb.query.filter_by(id=id).first()
     if request.method=="POST":

       if post:
        db.session.delete(post)
        db.session.commit()
        title= request.form["title"]
        body = request.form["body"]
        post = PostDb(id=id,title= title,body=body)
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('posts.get'))

     return render_template("posts/update.html")

if __name__=='__main__':
     app.run(debug=True)

@app.errorhandler(404)
def page_not_found(error):
    return  f"<h1 style='color:red'> Enter A Valid Url </h1>"

from flask import Flask
from flask import render_template,request
from flask import request,redirect,url_for,session
from werkzeug.utils import secure_filename

from blog.models import Posts, db

from blog.post.postBlueprints import post_blueprint

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

@post_blueprint.route("", endpoint = "posts_get")
def get_all_posts():
      posts = Posts.getAllPosts()
      return render_template("posts/post.html", posts = posts)



@post_blueprint.route('/<int:id>/delete', endpoint = 'post_delete')
def delete_post(id):
    post = Posts.get_specific_object(id)
    post.deletePost()
    return redirect(url_for('posts_get'))


@post_blueprint.route("/<int:id>", endpoint = 'post_show')
def show_post(id):
    post = Posts.get_specific_object(id)
    return render_template("posts/show.html", post = post)


@post_blueprint.route("/create",endpoint="post_create", methods = ["GET", "POST"] )
def create_post():
    if request.method=="POST":
        id = request.form["id"]
        title = request.form["title"]
        body = request.form["body"]
        file = request.files['file']
        post = Posts(id = id, title = title, body = body , image = file.filename)
        
        post = Posts.get_specific_object(id)
        post.createPost()
        return redirect(url_for('posts_get'))

    return render_template("posts/create.html")


@post_blueprint.route("/<int:id>/update", endpoint = "post_update" , methods = ["GET", "POST"])
def update_post(id):
     post = Posts.query.filter_by(id=id).first()
     if request.method=="POST":
       if post:
        db.session.delete(post)
        db.session.commit()
        title= request.form["title"]
        body = request.form["body"]
        image = request.form["file"]
        post = Posts(id = id, title = title, image = image,body = body)
        
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('posts_get'))

 
     return render_template("posts/update.html",post = post)
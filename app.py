from flask import Flask, abort, render_template

from data import Books, Posts

app = Flask(__name__)

site_title = "Made by Shingen"
site_tagline = "Making Things Simple, Useful, & Impactful"


@app.context_processor
def inject_global():
    return dict(site_title=site_title, site_tagline=site_tagline)


@app.route("/")
def index():

    # Page Details
    page_title = "Index"

    return render_template("index.html", page_title=page_title)


@app.route("/zen/")
def zen():

    # Page Details
    page_title = "Zen"

    return render_template("zen.html", page_title=page_title)


@app.route("/bookshelf/")
def bookshelf():

    # Page Details
    page_title = "Bookshelf"

    return render_template("bookshelf.html", page_title=page_title, books=Books)


@app.route("/blog/")
def blog():

    # Page Details
    page_title = "Blog"

    return render_template("blog.html", page_title=page_title, posts=Posts)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    # Find the post with matching id
    post = next((p for p in Posts if p["id"] == post_id), None)
    if post is None:
        abort(404)  # or return "Not found", 404
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run()

from flask import Blueprint, abort, redirect, url_for, render_template
from datetime import datetime
from app import db, app
from app.blog.models import Post, Tag

blog = Blueprint('blog', __name__, url_prefix='/blog')

@blog.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

@blog.route('/', methods=['GET'])
def index():
    articles = Post.query.all()
    return render_template('blog/index.html', posts=articles)

@blog.route('/stitok/<string:slug>', methods=['GET'])
def tag(slug):

    tag = Tag.query.filter_by(slug=slug).first()

    if tag is None:
        abort(404)

    articles = Post.query.filter(Tag.slug == slug)


    return render_template('blog/tag.html', posts=articles, tag=tag)


@blog.route('/<string:slug>', methods=['GET'])
def show(slug):

    article = Post.query.filter_by(slug=slug).first()

    if article is None:
        abort(404)

    return render_template('blog/show.html', post=article)

@blog.route('/<int:id>', methods=['GET'])
def short_link(id):

    article = Post.query.filter_by(id=id).first()

    if article is None:
        abort(404)

    return redirect(url_for('blog.show', slug=article.slug))

@blog.route('/rss.xml', methods=['GET'])
def rss():
    articles = Post.query.all()
    return render_template('blog/rss.xml', posts=articles), 200, {'Content-Type': 'application/rss+xml'}

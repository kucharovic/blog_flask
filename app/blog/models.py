from app import db

tags = db.Table('post_tag',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'))
)

class Base(db.Model):

    __abstract__  = True

    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(255), nullable=False)
    slug        = db.Column(db.String(255), nullable=False, unique=True)

class Tag(Base):

    __tablename__ = 'tag'

    def __repr__(self):
        return self.title

class Post(Base):

    __tablename__ = 'post'

    description  = db.Column(db.String(255), nullable=False)
    perex        = db.Column(db.Text(), nullable=False)
    content      = db.Column(db.Text(), nullable=False)
    published_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified_at  = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=True)
    tags         = db.relationship('Tag', secondary=tags, backref=db.backref('posts', lazy='dynamic'))

    def __repr__(self):
        return '<Post %r>' % (self.title)

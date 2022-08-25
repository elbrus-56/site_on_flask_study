from app import db
from datetime import datetime
import re


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)


post_tags = db.Table('post_tags',
                    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
                    )


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    # Если будут скобки у datetime.now(), то дефолтное значение будет задаваться в момент запуска программы и будет для новых постов одним и тем же. Если же убрать скобки, то функция передастся как параметр, и будет вызываться каждый раз при добавлении нового поста
    created = db.Column(db.DateTime, default=datetime.now)


    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args,**kwargs)
        self.generate_slug()


    tags = db.relationship('Tag', secondary=post_tags, backref=db.backref('posts', lazy='dynamic'))


    
    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)


    def __repr__(self):
        return f'<Post id: {self.id}, title: {self.title}>'


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100))

    def __init__(self, *args, **kwargs) -> None:
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)
    

    def __repr__(self):
        return f'Tag id: {self.id}, name: {self.name}'



# from app import db
# >>> from models import Tag
# >>> tag = Tag(name='python')
# >>> tag
# Tag id: None, name: python
# >>> db.session.add(tag)
# >>> db.session.commit

# >>> from models import Post
# >>> post = Post.query.all()
# >>> post
from models import db, Post
from app import app

with app.app_context():
    db.create_all()
    post1 = Post(title="bimba", content="bimba is very cool")
    post2 = Post(title="bimbaultra", content="bimbaultra eto kak bimba v stepeni")
    post3 = Post(title="bimba.", content="bimba eto Denis (vi ne poimete)")
    db.session.add_all([post1, post2, post3])
    db.session.commit()
    print("Happy happy happy")
    print("Happy happy happy")
    print("Happy happy happy")
    print("Happy happy happy")
    print("Happy happy happy")
    print("Happy happy happy")
    print("Happy happy happy")

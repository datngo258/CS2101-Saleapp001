from app.__init__ import db, app
from sqlalchemy import Column, String, Integer, Float, BOOLEAN, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

class Category(db.Model):
    __tablename__ = "category"
    name = Column(String(50),nullable=False, unique=True)
    id = Column(Integer,primary_key=True,autoincrement=True )

    products = relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    __tablename__ = "products"
    name = Column(String(50), nullable=False, unique=True)
    id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Float, default=0 )
    image = Column(String(100))
    active = Column(BOOLEAN, default=True)

    category_id = Column(Integer, ForeignKey(Category.id),nullable=True)


if __name__ == "__main__":
    with app.app_context():

        p1 = Product(name="iphone 13",price=20000000,image='https://cdn.fastcare.vn/fastcare/2022/05/thay-vo-iphone-13-pro-fc.jpg', active=1, category_id=1)
        p2 = Product(name="ipad Pro 2023", price=20000000,
                     image='https://cdn.fastcare.vn/fastcare/2022/05/thay-vo-iphone-13-pro-fc.jpg', active=1,
                     category_id=1)
        p3 = Product(name="Galaxy Tab  S9", price=20000000,
                     image='https://cdn.fastcare.vn/fastcare/2022/05/thay-vo-iphone-13-pro-fc.jpg', active=1,
                     category_id=1)
        p4 = Product(name="Galaxy S23", price=20000000,
                     image='https://cdn.fastcare.vn/fastcare/2022/05/thay-vo-iphone-13-pro-fc.jpg', active=1,
                     category_id=1)
        p5 = Product(name="iphone 15", price=20000000,
                     image='https://cdn.fastcare.vn/fastcare/2022/05/thay-vo-iphone-13-pro-fc.jpg', active=1,
                     category_id=1)
        db.session.add(p1)
        db.session.add(p2)
        db.session.add(p3)
        db.session.add(p4)
        db.session.add(p5)
        db.session.commit()



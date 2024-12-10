import json, os
from bookseller import app,db
from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import  current_user
<<<<<<< HEAD
from bookseller.models import Category, Product, User, UserRole
=======

from bookseller.index import products_detail
from bookseller.model import Category,Product, User,ProductDetail
>>>>>>> 7f43e9d (Initial commit)

import hashlib

def read_json(path):
    with open(path,"r") as f:
        return json.load(f)


def load_categories():
    return Category.query.order_by("id").all()
<<<<<<< HEAD


def load_products(cate_id=None,kw=None,from_price=None,to_price=None,page=1):
    products = Product.query
=======
def get_products_by_id(products_id):
    return Product.query.get(products_id)
def get_products_detail_by_id(products_id):
    return ProductDetail.query.get(products_id)
def load_products(cate_id=None, kw=None, price=None, page=1):
    products = Product.query  # Truy vấn sản phẩm ban đầu


>>>>>>> 5b3aaea (commit to pull)
    if kw:
        products = products.filter(Product.name.contains(kw))


    if cate_id:
        products = products.filter(Product.category_id == int(cate_id))

    if price:
        price_ranges = {
            '1': (0, 15000),
            '2': (15000, 30000),
            '3': (30000, 50000),
            '4': (50000, 70000),
            '5': (70000, 999999)
        }
        price_range = price_ranges.get(str(price))
        if price_range:
            products = products.filter(
                Product.price >= price_range[0],
                Product.price < price_range[1]
            )

    # Phân trang
    page_size = app.config.get('PAGE_SIZE', 10)
    start = (page - 1) * page_size
    end = start + page_size

    return products.slice(start, end).all()

    return products.slice(start,end).all()


def cout_products():
    return Product.query.count()


def check_login(username,password):
    if username and password :
        password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
        return User.query.filter(User.username.__eq__(username.strip()),User.password.__eq__(password)).first()


def get_user_by_id(user_id):
    return User.query.get(user_id)


def add_user(name,username,password,**kwargs):
    password=str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    user= User(name=name.strip() ,username=username.strip(),password=password,avatar=kwargs.get('avatar'))
    db.session.add(user)
    db.session.commit()


def count_cart(cart):
    total_quantity,total_amount=0,0
    if cart:
        for c in cart.values():
            total_quantity+=c['quantity']
            total_amount+=c['quantity']*c['price']
    return {
        "total_amount":total_amount,
        "total_quantity":total_quantity
    }


def auth_user(username, password):
    password = hashlib.md5(password.strip().encode('utf-8')).hexdigest()

    return User.query.filter(User.username.__eq__(username.strip()), User.password.__eq__(password)).first()


def get_user_by_id(user_id):
    return User.query.get(user_id)


def auth_admin(username, password):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username),
                             User.password.__eq__(password), User.user_role.__eq__(UserRole.ADMIN)).first()
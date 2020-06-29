#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
import config
from db import db
from model.Article import Article
from model.User import User


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    with app.app_context():
        # db.create_all(bind=None)
        db.create_all(bind='db_iris')
        db.create_all(bind='test')

    @app.route('/add_user')
    def add_user():
        te = User(username='haha')
        db.session.add(te)
        db.session.commit()
        return "add user"

    @app.route('/add_article')
    def add_article():
        te = Article(title='xixi', content='ininininininin')
        db.session.add(te)
        db.session.commit()
        return "add article"

    @app.route('/query_user')
    def query_user():
        s = User.query.all()
        for i in s:
            print(i.username)
        return 'haha'

    @app.route('/query_article')
    def query_article():
        s = Article.query.all()
        for i in s:
            print(i.title)
        return 'xixi'

    return app


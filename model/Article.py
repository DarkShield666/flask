#!/usr/bin/python
# -*- coding: utf-8 -*-
from db import db


class Article(db.Model):
    __tablename__ = 'article'
    __bind_key__ = 'db_iris'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

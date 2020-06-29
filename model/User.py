#!/usr/bin/python
# -*- coding: utf-8 -*-
from db import db


class User(db.Model):
    __bind_key__ = 'test'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
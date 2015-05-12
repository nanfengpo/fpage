﻿# coding:utf-8

import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db = create_engine(config.DATABASE_URI)
Model = declarative_base()
Session = sessionmaker(bind=db)

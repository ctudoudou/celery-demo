#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/14 上午10:05
# @Author  : tudoudou
# @File    : tasks.py
# @Software: PyCharm

import time
# Celery settings
from celery import Celery

celery_app = Celery('tasks', backend='redis://localhost', broker='redis://localhost')


@celery_app.task
def add(a, b):
    time.sleep(5)
    return a + b

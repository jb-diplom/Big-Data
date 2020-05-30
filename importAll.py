# -*- coding: utf-8 -*-
"""
Created on Tue May 19 18:27:52 2020

@author: Janice
"""


import importlib
importlib.import_module("reader")
importlib.import_module("topicmap")
importlib.import_module("similarity")
importlib.import_module("scatterplots")
importlib.import_module("sentiment3d")

from reader import loadAllFeedsFromFile
from scatterplots import displayTags

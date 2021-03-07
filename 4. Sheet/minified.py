#!/usr/bin/env python3
# -*- coding:utf-8 -*-
rujGomsJxc=tuple
rujGomsJxz=sum
rujGomsJxf=isinstance
rujGomsJxM=print
rujGomsJxt=SyntaxError
rujGomsJxB=AttributeError
rujGomsJhW=True
rujGomsJhx=enumerate
rujGomsJhN=int
rujGomsJhH=str
rujGomsJhF=len
rujGomsJhi=ord
rujGomsJhe=set
rujGomsJhT=False
rujGomsJhE=list
rujGomsJhn=None
rujGomsJhQ=range
rujGomsJhb=open
rujGomsJhK=zip
rujGomsJhA=dict
rujGomsJhO=next
rujGomsJhC=StopIteration
import ast
import inspect
import os
import pickle
import shutil
import sys
from functools import partial,wraps
import matplotlib.pyplot as plt
import numpy as np
def no_imports(func):
 try:
  rujGomsJWx=ast.walk(ast.parse(inspect.getsource(func)))
  rujGomsJWh=(ast.Import,ast.ImportFrom)
  rujGomsJWN=rujGomsJxc(rujGomsJWx)
  rujGomsJWH=rujGomsJxz(rujGomsJxf(node,rujGomsJWh)for node in rujGomsJWN)
  if rujGomsJWH>0:
   rujGomsJxM("Your function contains {} import".format(rujGomsJWH)+" statements which is not allowed")
 except rujGomsJxt:
  rujGomsJWH=-1
 @wraps(func)
 def wrapper(*args,**kwargs):
  return func(*args,**kwargs)
 def assert_no_imports():
  assert rujGomsJWH==0,"No import statements allowed"
 wrapper.assert_no_imports=assert_no_imports
 return wrapper
def max_allowed_loops(rujGomsJWT):
 def get_ast_Call_name(node):
  try:
   rujGomsJWF=node.func.id
  except rujGomsJxB:
   rujGomsJWF=node.func.attr
  return rujGomsJWF
 def decorator(func):
  try:
   rujGomsJWi=(ast.For,ast.While,ast.AsyncFor,ast.ListComp,ast.DictComp,ast.SetComp,ast.GeneratorExp,)
   rujGomsJWx=ast.walk(ast.parse(inspect.getsource(func)))
   rujGomsJWN=rujGomsJxc(rujGomsJWx)
   rujGomsJWe=rujGomsJxz(rujGomsJxf(node,rujGomsJWi)for node in rujGomsJWN)
   if rujGomsJWe>rujGomsJWT:
    rujGomsJxM("Your function uses more loops than allowed" "\nMax allowed: {}\nYour function: {}".format(rujGomsJWT,rujGomsJWe),file=sys.stderr,)
  except rujGomsJxt:
   rujGomsJWe=-1
  @wraps(func)
  def wrapper(*args,**kwargs):
   return func(*args,**kwargs)
  def assert_not_too_many_loops():
   assert rujGomsJWT>=rujGomsJWe,("Function uses too many loops: allowed: {},".format(rujGomsJWT)+" used: {}".format(rujGomsJWe))
  wrapper.assert_not_too_many_loops=assert_not_too_many_loops
  return wrapper
 return decorator
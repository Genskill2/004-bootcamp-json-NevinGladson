# Add the functions in this file

import sys
import json

def load_journal(f):
  f = open(f,)
  data = json.load(f)
  return data

def compute_phi(f, example):
    data=load_journal(f)
    z=0
    x=0
    c=0
    v=0
    a=0
    s=0
    d=0
    f=0
    for i in range(0,91):
        if example in data[i]['events'] and data[i]['squirrel']:
            z=z+1
        if example not in data[i]['events'] and not data[i]['squirrel']:
            x=x+1
        if example in data[i]['events'] and not data[i]['squirrel']:
            c=c+1
        if example not in data[i]['events'] and data[i]['squirrel']:
            v=v+1
        if example in data[i]['events']:
            a=a+1
        if example not in data[i]['events']:
            s=s+1
        if data[i]['squirrel']:
            d=d+1
        if not data[i]['squirrel']:
            f=f+1
    
    req=(z*x-c*v)/(a*s*d*f)**(0.5)
    return req

  

def compute_correlations(f):
  data = load_journal(f)
  ret = {}
  for i in range(len(data)):
    for j in data[i]['events']:
     if j not in ret:
      ret[j] = compute_phi(f, j)
      
  return ret     
  

def diagnose(f):
  data = compute_correlations(f)
  max_positive = 0
  min_negative=0
  for i in data.keys():
    if data[i] > max_positive:
      max_positive = data[i]
      max_event = i
    elif data[i] < min_negative:
      min_negative = data[i]
      min_event = i
  return max_event, min_event


# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vB-Y2JiQmoDYVtBTPIsOTPTGz1upMDiz
"""

import requests
import json
#the required first parameter of the 'get' method is the 'url':
def getPulls(path: str):
  endpoint =  'https://immense-retreat-96686.herokuapp.com/pulls/' + path
  info = requests.get(endpoint)
  info = info.json()
  print('Repository' + path + "top 10 issues are : ")
  x = 0
  for i in range(len(info)):
    print('#'+ str(info[i]['number']) + '-' + info[i]['title'] )
    print('Created by ' + info[i]['user']['login'] + " at " + info[i]["created_at"])
    print("PR is" + info[i]['state'] +'\n')
    if x > 9:
      break
def getIssues(path: str):
  endpoint =  'https://immense-retreat-96686.herokuapp.com/issues/' + path
  info = requests.get(endpoint)
  info = info.json()
  print('Repository' + path + "top 10 issues are :")
  x = 0
  for i in range(len(info)):
    print('#'+ str(info[i]['number']) + '-' + info[i]['title'])
    print('Created by ' + info[i]['user']['login'] + " at " + info[i]["created_at"])
    print("Issue is" + info[i]['state'] +'\n')
    if x > 9:
      break
#print the response text (the content of the requested file):
while True:
  path = input("Enter the repository name (format: owner/repository) : ")
  if len(path.split('/')) != 2:
    print("please enter the correct format, try again") 
    continue
  req_type = input("Enter the information type (pull-requests, issues : ")
  if req_type not in ('pull-requests', 'issues'):
    print("please enter the correct format, try again") 
    continue
  if req_type == 'pull-requests':
    data = getPulls(path)
    getPulls(path)
  else:
    data = getPulls(path)
    getIssues(path)


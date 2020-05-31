import json
import matplotlib.pyplot as plt
import pickle

with open('./arxivData.json') as file:
  obj = json.load(file)

author = {}
title = {}

def get_acronym(title):
  acronym = ""
  words = title.split(" ")
  for w in words:
    if (len(w) > 0) and (w[0].isalpha()):
      acronym += w[0]
  return acronym.upper()

def get_surname(name):
  name = name.split(" ")
  for n in name:
    if "}" in n:
      return(n[0:-3])
  return("NULL")

for c in obj:
  acronym = get_acronym(c['title'])
  
  if acronym in ["SC", "POTTCOUIAI", "POTFCOUIAI", "CF"]:
    print(c['title'])

  last_name = get_surname(c["author"])
  try:
    author[last_name] = author[last_name] + 1
  except KeyError:
    author[last_name] = 1
  try:
    title[acronym] = title[acronym] + 1
  except KeyError:
    title[acronym] = 1

'''
with open("author.json", "r+") as file:
  author = {k: v for k, v in sorted(author.items(), key=lambda item: item[1])}
  json.dump(author, file, indent=4) 

with open("title.json", "r+") as file:
  title = {k: v for k, v in sorted(title.items(), key=lambda item: item[1])}
  json.dump(title, file, indent=4) 
'''

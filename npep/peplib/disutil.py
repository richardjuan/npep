#!/usr/bin/env python2.7
# -*- coding: utf-8 -*- 

'''---------------------------------------------------------------------------|
                                                              _____           |
      Autor: Notsgnik                                       /||   /           |
      Email: Labruillere gmail.com                         / ||  /            |
      website: notsgnik.github.io                         /  || /             |
      License: GPL v3                                    /___||/              |
      																		  |
---------------------------------------------------------------------------!'''

from array import *

from pestruct import *

msgs = {
	"0" : "type unandled by binary buffer",
	"1" : "cannot open the file",
	"2" : "buffer options are not valid",
	"3" : "the struct suplied must be a dictionary",
	"4" : "the option suplied is not supported",
	"5" : "invalid PE File",
	"6" : "invalid PE Optional Header Size",
	"7" : "invalid PE magic",
	"8" : "structure syntax error within a list",
	"9" : "unable to execute custom function",
	"10": "custom function ruturn garbage",
	"11": "uniun options take only strings",
	"12": "first option must be integer"
}
debug_lvl = 0
def debug_msg(msg_nb, lvl = 1):
	print debug_lvl
	if msgs == {}:
		error = "Error " + msg_nb
	else:
		try:
			error =  msgs[msg_nb]
		except :
			error = "Unknow"
	if debug_msg < 0 or lvl < 0:
		raise Exception(error)
	elif debug_lvl >= lvl:
		print error

def bleStrToHex(string):
	return string[::-1].encode("hex")

def bleStrToInt(string):
	return int(bleStrToHex(string),16)
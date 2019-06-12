#!/usr/bin/python3
import datetime

var=datetime.datetime.now()

name=input("enter your name")

if(var.hour>=0 and var.hour<4):
	print("good night "+name)

if(var.hour>=4 and var.hour<12):
	print("good morning "+name)

if(var.hour>=12 and var.hour<16):
	print("good afternoon "+name)

if(var.hour>=16 and var.hour<24):
	print("good evening "+name)


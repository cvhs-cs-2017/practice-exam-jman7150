""" Create a Turtle, name it, make it BLUE and draw a Smiley Face"""
import turtle
smileyface = turtle.Turtle()
smileyface.color('Blue')

smileyface.penup()
smileyface.goto(-75,150)
smileyface.pendown()
smileyface.circle(10)

smileyface.penup()
smileyface.goto(75,150)
smileyface.pendown()
smileyface.circle(10)

smileyface.penup()
smileyface.goto(0,0)
smileyface.pendown()
smileyface.circle(100,90)

smileyface.penup()
smileyface.goto(0,0)
smileyface.pendown()
smileyface.circle(-100,90)

smileyface.penup()
smileyface.goto(0,-100)
smileyface.pendown()
smileyface.circle(300)

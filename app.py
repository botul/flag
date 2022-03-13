from unicodedata import name
from flask import Flask, render_template
from my_apps.wiki_character import character
import random
app=Flask(__name__)

@app.route('/')
def index():
    text = open('dane/xd.txt').read()
    return render_template("index.html", text=text)

@app.route('/xd')
def xd():
    return render_template("xd.html")

@app.route('/ua')
def ua():
    text = "Dużo siły i wytrwałości dla Ukrainy"
    text2 = "Jesteśmy z Wami!"
    return render_template("ua.html", text=text, text2=text2)

@app.route('/brudnopis')
def brudnopis():
    name = "Kłapouchy"
    super_heroes = ['Sowa', 'Tygrysek', 'Kubuś']
    chosen_hero = random.choice( super_heroes)
    hero = character(name)
    return render_template("brudnopis.html", hero=hero, super_heroes=super_heroes)

if __name__=="__main__":
    app.run()

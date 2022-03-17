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

@app.route('/heroes')
def heroes():
    super_heroes = ['Skiba', 'Queen', 'The Prodigy']
    content_list = []
    # for i in range(3):
    #     interesting_character = choice(super_heroes)
    #     interesting_character_index = super_heroes.index(interesting_character)
    #     super_heroes.pop(interesting_character_index)

    #     character_desc = character(super_heroes)

    #     word_list = character_desc.split(' ')
    #     word_list_len = len(word_list)

    #     content = [interesting_character, character_desc, word_list_len]

    # chosen_hero = random.choice( super_heroes)
    # hero = character(name)
    # return render_template("brudnopis.html", hero=hero, super_heroes=super_heroes)

posts = [
    {
        'author': 'Botul',
        'title': 'Wpis w blogu',
        'content': 'Taki sobie wpis w blogu',
        'date_posted': '15 marca 2022'
    },
    {
        'author': 'Botul',
        'title': 'Drugi wpis',
        'content': 'Taki sobie wpis w blogu',
        'date_posted': '17 marca 2022'
    }
        ]
@app.route('/blog')
def blog():
    return render_template("blog.html", posts=posts)

@app.route('/about')
def about():
    return render_template("about.html")


if __name__=="__main__":
    app.run()

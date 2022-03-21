from unicodedata import name
from flask import Flask, render_template, url_for
from my_apps.wiki_character import character
import random
app=Flask(__name__)

@app.route('/')
def index():
    text = open('dane/xd.txt').read()
    return render_template("index.html", text=text)


@app.route('/heroes')
def heroes():
    super_heroes = ['Krzysztof Skiba', 'Queen', 'The Prodigy']
    for i in range(3):
        interesting_character = random.choice(super_heroes)
        character_index = super_heroes.index(interesting_character)
        super_heroes.pop(character_index)

        character_desc = character(interesting_character)

        word_list = character_desc.split(' ')
        word_list_len = len(word_list)

        content = [interesting_character, character_desc, word_list_len]

    return render_template("hero.html", super_heroes=super_heroes)

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

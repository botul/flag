@app.route('/xd')
def xd():
    return render_template("xd.html")

@app.route('/ua')
def ua():
    text = "Dużo siły i wytrwałości dla Ukrainy"
    text2 = "Jesteśmy z Wami!"
    return render_template("ua.html", text=text, text2=text2)


# @app.route('/brudnopis')
# def brudnopis():
#     name = "Kłapouchy"
#     super_heroes = ['Sowa', 'Tygrysek', 'Kubuś']
#     chosen_hero = random.choice( super_heroes)
#     hero = character(name)
#     return render_template("brudnopis.html", hero=hero, super_heroes=super_heroes)



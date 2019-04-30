from flask import render_template, Flask, redirect, flash
from form import LoginForm
import os
from mail import mail, mail_for_me
import sqlite3


#объявление переменных
Ingredients = 'Вы ничего не указали'
feedback_time_list = []
eat = " "




app = Flask(__name__) #создаем экземпляр объекта Flask
app.config['SECRET_KEY'] = 'lEay3xpXwDHOMQG0tYTKAiYQlbQ2pl0BS78RtiFQOdwrW7jgU7TleH8qLLr7'



@app.route('/recipes', methods=['POST', 'GET'])
#функция страницы с рецептами
def recipes():
    form = LoginForm()
    recipes_list = []
    recipes_list1 = []
    recipes_list2 = []
    con = sqlite3.connect('feedback.db')
    cur = con.cursor()
    cur.execute("Select name from main")
    time = cur.fetchall()
    for i in time:
        for j in i:
            recipes_list.append(j)

    for i in range(len(recipes_list)):
        if i % 2 == 0:
            recipes_list1.append(recipes_list[i])
        else:
            recipes_list2.append(recipes_list[i])
    con.commit()
    con.close()
    return render_template('recipes.html', recipes_list1=recipes_list1, recipes_list2=recipes_list2, form=form)


@app.route('/finish', methods=['POST', 'GET'])
def finish():
#функция, которая выдает подходящие рецепты
    return render_template('finish.html', Ingredients=Ingredients)


@app.route('/help',  methods=['POST', 'GET'])
def help():
    form = LoginForm()
    if form.validate_on_submit():
        con = sqlite3.connect('feedback.db')
        cur = con.cursor()
        if form.FeedbackForm.data != "":
            cur.execute("INSERT INTO feedback VALUES (?, ?)", (form.email.data, form.FeedbackForm.data))
            if form.email.data == "":
                mail_for_me(form.FeedbackForm.data)
            if form.email.data != "":
                mail(form.email.data)
                mail_for_me(form.FeedbackForm.data)
        con.commit()
        con.close()

    return render_template('help.html', form=form)


@app.route("/", methods=['POST', 'GET'])
def main():
    id_counter = 0
    eat = " "
    form = LoginForm()
    time_list = []
    Ingredients = 'Вы ничего не указали'


    con = sqlite3.connect('feedback.db')
    cur = con.cursor()

    cur.execute("Select name from main")
    time = cur.fetchall()
    time = time[0:5]
    for i in time:
        time_list.append(i[0])

    if form.validate_on_submit():
        count = 0
        finishList = []
        superList = []
        max_count = 0

    #    if form.textareafield.data != "":
    #       cur.execute("INSERT INTO recipes VALUES (?, ?)", (id_counter, form.textareafield.data))

        Ingredients = form.textareafield.data

#каким-то хуем работает
        #обработка крч
        if Ingredients == "":
            eat = "Из этого ничего нельзя приготовить."
            Ingredients = 'Вы ничего не указали'
        else:
            #в этом словаре храним ингридиенты
            inhredients = Ingredients.replace(",", " ").split()
            for i in inhredients:
                i.lower()
            max_count = int(len(inhredients)/4)
            if max_count < 1:
                max_count = 1
            cur.execute("Select Ingredients from main ")
            f = cur.fetchall()
            for i in range(len(f)):
                a = f[i][0]
                for j in inhredients:
                    if j in a:
                        count += 1
                if count >= max_count:
                    cur.execute("Select name from main where Ingredients = ? ", [(a)])
                    finishList.append(cur.fetchall())
            for i in finishList:
                for j in i:
                    for k in j:
                        superList.append(k)
        con.commit()
        con.close()
        return render_template('finish.html', Ingredients=Ingredients, eat=eat, superList=superList)

    con.commit()
    con.close()
    return render_template('main.html', form=form, time_list=time_list)


@app.route('/advertising', methods=['POST', 'GET'])
def advertising():
    return render_template("advertising.html")


@app.route('/sentence', methods=['POST', 'GET'])
def sentence():
    form = LoginForm()
    if form.validate_on_submit():
        con = sqlite3.connect('feedback.db')
        cur = con.cursor()
        if form.name_recipe.data != "" and form.main_recipe.data != "" and form.Ingredients_main_recipe.data != "":
            cur.execute("INSERT INTO main_help(name,description,Ingredients ) VALUES (?, ?, ?)", (form.name_recipe.data, form.main_recipe.data, form.Ingredients_main_recipe.data))
        con.commit()
        con.close()
    return render_template("sentence.html", form=form)


@app.route('/<n>')
def n(n):
    discription = ""
    con = sqlite3.connect('feedback.db')
    cur = con.cursor()
    cur.execute("Select description from main where name = ? ", [(n)])
    time = cur.fetchall()
    for i in time:
        for j in i:
            discription = j
    con.commit()
    con.close()
    if discription != "":
        return render_template('n.html', n=n, discription=discription)
    if discription == "":
        return "такого рецепта не существует"


@app.route('/6IfG4aaUaVKMEuYCxGR6JLEsczNVfoFcXKKWLLGNwhs7Ejy7Ph', methods=['POST', 'GET'])
def admin():
    form = LoginForm()
    con = sqlite3.connect('feedback.db')
    cur = con.cursor()
    cur.execute("Select * from main_help")
    db = cur.fetchall()
    if form.validate_on_submit():
        cur.execute(form.sql.data)
        con.commit()
    con.commit()
    con.close()
    return render_template('admin.html', form=form, db=db)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

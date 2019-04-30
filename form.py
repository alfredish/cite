from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField('Введите ваш Email (для ответа вам)')
    textareafield = TextAreaField('Что-то')
    submit = SubmitField('Найти подходящий рецепт')
    FeedbackForm = TextAreaField("Ваше сообщение")
    submit_help = SubmitField("Отправить отзыв")

    #sentence
    name_recipe = StringField('Название блюда')
    submit_name_recipe = SubmitField("Добавить рецепт")
    main_recipe = TextAreaField('Напишите рецепт')
    Ingredients_main_recipe = TextAreaField('Напишите ингредиенты')

    # admin
    admin_name_recipe = StringField('Название блюда')
    admin_submit_name_recipe = SubmitField("Добавить рецепт")
    admin_main_recipe = TextAreaField('Напишите рецепт')
    admin_Ingredients_main_recipe = TextAreaField('Напишите ингредиенты')

    #запроск бд
    sql = StringField('Запрос к  бд main')
    sql_submit = SubmitField("Отправить запрос")

    #поиск рецептов
    find = StringField('Найти рецепт')
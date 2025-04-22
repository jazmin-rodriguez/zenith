from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, validators, ValidationError


class CalorieIntakeForm(FlaskForm):
    ingredients = TextAreaField("Grams & ingredients.",  [validators.InputRequired("Please enter the grams and ingredients(100g chicken, 15g rice etc.).")])
    submit = SubmitField("Total Calories")
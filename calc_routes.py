from flask import Blueprint, render_template, session,redirect,url_for
from .calc_form import CalorieIntakeForm
from .edamam_calc import get_calories_from_edamam

calc_blueprint = Blueprint('calc', __name__)

@calc_blueprint.route('/calorie-calc', methods=["GET", "POST"])
def calc():
    form = CalorieIntakeForm()
    if 'user_id' in session:
        user_logged_in = 'user_id' in session
    else:
        return redirect(url_for('auth.login'))
    # return render_template("calorie-calc.html")
    if form.validate_on_submit():
        # Handle form submission (e.g., call get_calories_from_edamam)
        ingredients = form.ingredients.data
        calorie_data = get_calories_from_edamam(ingredients)
        # Render the result or handle accordingly
        return render_template("calorie-calc.html", form=form, calorie_data=calorie_data,user_logged_in=user_logged_in)
    return render_template("calorie-calc.html", form=form)
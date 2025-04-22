from flask import Blueprint, render_template, session, redirect, url_for
from google.cloud import firestore

progress_blueprint = Blueprint('progress', __name__)

# Firestore client
db = firestore.Client()

@progress_blueprint.route('/progress')
def progress():
    if 'user_id' in session:
        user_id = session['user_id']
        user_ref = db.collection('users_example').document(user_id)
        user_doc = user_ref.get()
        
        saved_workouts = []
        if user_doc.exists:
            user_data = user_doc.to_dict()
            saved_workouts = user_data.get('saved_generated_workouts', [])
        
        user_logged_in = True
        return render_template("progress.html", user_logged_in=user_logged_in, workouts=saved_workouts)
    else:
        return redirect(url_for('auth.login'))

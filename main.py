from flask import Flask, render_template
from flask_login import login_user, logout_user, current_user, login_required
from dotenv import load_dotenv
import os

app = Flask(__name__, static_url_path="/static")

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

google_form_url = os.getenv('YOUR_GOOGLE_FORM_URL')

@app.context_processor
def inject_user():
    return dict(current_user=None)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/contact')
def contact():
     return render_template('contact.html', google_form_url=google_form_url)

@app.route('/fleetiq')
def fleetiq():
    return render_template('fleetiq.html')

@app.route('/bots')
def bots():
    return render_template('bots.html')

@app.route('/terms-of-service')
def terms_of_service():
    return render_template('terms_of_service.html')

@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy_policy.html')

@app.route('/cancel-policy')
def cancel_policy():
    return render_template('cancel_policy.html')

@app.route('/ark-guardian')
def ark_guardian():
    return render_template('ark-guardian.html')

@app.route('/ark-pop')
def ark_pop():
    return render_template('ark-pop.html')

@app.route('/guardian')
def guardian():
    return render_template('guardian.html')

@app.route('/tickets')
def tickets():
    return render_template('tickets.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False, use_reloader=False)
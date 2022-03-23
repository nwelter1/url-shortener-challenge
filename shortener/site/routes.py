from flask import Blueprint, render_template, request
from shortener.forms import URLInputForm

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/', methods=['GET','POST'])
def home():
    form = URLInputForm()
    if request.method == 'POST' and form.validate_on_submit():
        link = form.link.data
        print(link)
        return render_template('home.html', form = form)

    return render_template('home.html', form = form)
from flask import Blueprint, render_template, request, redirect
from shortener.forms import URLInputForm
from shortener.models import db, Link

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/', methods=['GET','POST'])
def home():
    form = URLInputForm()
    if request.method == 'POST' and form.validate_on_submit():
        link = form.link.data
        # checking for duplicates
        check = Link.query.filter_by(link=link)
        if check.first() is not None:
            return render_template('home.html', form = form, created_link = f'{request.base_url}' + check.first().id, already = True)
        new_link = Link(link)
        db.session.add(new_link)
        db.session.commit()
        print('Success!')
        return render_template('home.html', form = form, created_link = f'{request.base_url}' + new_link.id)

    return render_template('home.html', form = form)

@site.route('/<id>',methods=['GET','POST'])
def go_to_link(id):
    try:
        record = Link.query.get(id)
        web_address = record.link
        return redirect(web_address)
    except:
        return f'This is not a valid shortlink! Please visit {request.base_url.rstrip(id)} to create one!'
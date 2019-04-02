from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
    eating = TextField('Eating:', validators=[validators.required()])

    @app.route("/", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)
        print (form.errors)
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            eating = request.form['eating']
            print (name)
            print (email)
            print (eating)

        if form.validate():
        # Save the comment here.
            flash('Hello ' + name)
        else:
            flash('Error: All the form fields are required. ')

        return render_template('hello.html', form=form)

if __name__ == "__main__":
    app.run()

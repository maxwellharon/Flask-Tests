from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
import unittest
import MathFunctions



app = Flask(__name__)
app.config['SECRET_KEY'] = '892efa8fc9ddf9648be1fc9fe7c16a93'
app.config['SQLALCHEMY_DATABSE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)



posts = [
	{
		'author': 'Wega Irungu',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'November 22 2018'
	},
	{
		'author': 'Martha Irungu',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'November 21 2018'
	}
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'wegairungum21@gmail.com' and form.password.data == 'wegairungu123':
			flash('You have successfuly logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Failed. Please check username and password', 'danger')
	return render_template('login.html', title='Login', form=form)

@app.route("/signout", methods=['GET', 'POST'])
def signout():
			flash('You have successfuly signed out!', 'success')
			return redirect(url_for('home'))

if __name__ == '__main__':
	app.run()
#TestMathFunctions.py
#By YourNameHere

# Import Statemants

class KnowValues(unittest.TestCase):
    # Test areaCircle() pi r^2
    def test_areaCircle_for_10radius(self):
        # Capture the results of the function
        result = MathFunctions.areaCircle(10)
        # Check for expected output
        answer = 314.1592653589793
        self.assertEqual(answer, result)

        # Capture the results of the function
    def test_areaCircle_for_2radius(self):
        # Capture the results of the function
        result = MathFunctions.arealive(2)
        # Check for expected output
        expected = 12.566370614359172
        self.assertEqual(expected, result)
        # Capture the results of the function

        # Capture the results of the function
    def test_areaCircle_for_3radius(self):
        # Capture the results of the function
        result = MathFunctions.areanive(3)
        # Check for expected output
        expected = 28.274333882308138
        self.assertEqual(expected, result)
        # Capture the results of the function


    def test_areaCircle_for_9radius(self):
        # Capture the results of the function
        result = MathFunctions.areasive(9)
        # Check for expected output
        expected = 254.46900494077323
        self.assertEqual(expected, result)
        # Capture the results of the function

    def test_areaCircle_for_4radius(self):
        # Capture the results of the function
        result = MathFunctions.areavive(4)
        # Check for expected output
        expected = 78.53981633974483
        self.assertEqual(expected, result)
        # Capture the results of the function

# Run the Test
if __name__ == '__main__':
    unittest.main()
	


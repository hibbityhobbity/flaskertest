from flask import Flask, render_template

#Create a Flask Instance
app = Flask(__name__)

#Create a route decorator
@app.route('/')

def index():
	first_name = "Robert"
	stuff = "This is bold text"

	favourite_pizza = ["Pepperoni", "Cheese", "Mushrooms", 41]
	return render_template("index.html", 
		first_name=first_name, stuff=stuff, favourite_pizza=favourite_pizza)

#def index():
#	return render_template("index.html")

#localhost:5000/Robert
@app.route('/user/<name>')

def user(name):
	return render_template("user.html", user_name=name)

#Custom error pages
#Page not found
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

#Internal server error
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500




#Jinga filters

#safe
#capitalize
#lower
#upper
#title
#trim
#striptags

#flask run for server

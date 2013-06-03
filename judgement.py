from flask import Flask, render_template, redirect, url_for, request, flash, session, request, g
import model

app = Flask(__name__)
app.secret_key = "w3\xf9j\x89\x97\xfe\xa6C\xde\xe9dF\x07\xf0\xa9\n2\xfb*n\xa2\xdb\xf4"

@app.route("/", methods=["GET"])
def login():
	return render_template("login.html")

@app.route("/ratings/<int:id>", methods=["GET"])
def ratings_by_user(id=None):
	user_ratings = model.session.query(model.Rating).filter_by(user_id=id).all()
	return render_template("user_ratings.html", ratings=user_ratings)

@app.route("/new_user")
def new_user():
	return render_template("new_user.html")

@app.route("/save_user", methods=["POST"])
def save_user():
	email = request.form["email"]
	password = request.form["password"]
	new_user = model.User(email = email, password = password)
	model.session.add(new_user)
	model.session.commit()
	session["new"] = new_user.id
	return redirect("/")

@app.route("/authenticate", methods=["POST"])
def authenticate():
	email = request.form["email"]
	password = request.form["password"]
	
	user_auth = model.session.query(model.User).filter_by(email = email, password = password) 
	if user_auth.first():
		user = user_auth.first()
		session["user_id"]=user.id
		flash("You are now logged in.") 
		return redirect("/")
	else:
		flash("Unable to authenticate the email and password. Try again.")
		return redirect("/")

@app.route("/logout")
def logout():
	# TODO fix logout so it appears as an option on the website.
	session.pop("user_id", None) 
	flash("You've been logged out.")
	return redirect("logout.html")

@app.route("/user_list")
def user_list():
	user_list = model.session.query(model.User).limit(20).all()
	return render_template("user_list.html", users=user_list)

@app.route("/movie_lookup", methods=["GET"])
def movie_lookup():
	return render_template("movie_lookup.html")

@app.route("/movie_results", methods=["POST"])
def movie_results():
	lookup = request.form["lookup"]

	movie_results = model.session.query(model.Movie).filter(model.Movie.title.like("%" + lookup + "%")).limit(20).all()
	return render_template("movie_results.html", movies = movie_results)	


if __name__ == "__main__":
	app.run(debug = True)
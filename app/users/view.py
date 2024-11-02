from flask import render_template, request, url_for, redirect
from app.users import users_bp

@users_bp.route("/hi/<string:name>")
def greetings_user(name):
    name = name.upper()
    age = request.args.get("age", None, int)
    return render_template("users/hi_user.html", name=name, age=age)

@users_bp.route("/admin")
def admin():
    return redirect(url_for("users.greetings_user", name="admin") + "?age=45")
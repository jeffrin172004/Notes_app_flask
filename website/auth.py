from flask import Blueprint,render_template,request,flash

auth= Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    data= request.form
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return render_template("logout.html")

@auth.route('/sign-up', methods=['GET','POST'])
def signup():
    if request.method =='POST':
        email=request.form.get("email")
        firstName=request.form.get("firstName")
        password1=request.form.get("password1")
        password2=request.form.get("password2")
        if len(email) < 5:
            flash("Email must be of length atleast 4.",category="failed")
        elif len(firstName) < 4:
            flash("First name must be of length atleast 3.",category="failed")
        elif password1 != password2:
            flash("The passwords do not match.",category="failed")
        elif len(password1) < 8:
            flash("The password must be of length atleast 7.",category="failed")
        else:
            flash("Successfully created account.",category="success")
            



    return render_template("signup.html")

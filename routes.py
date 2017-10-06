from flask import render_template, Flask, request
from forms import SignupForm
from models import db, Contact

app = Flask(__name__)
db.init_app(app)

app.secret_key="development-key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@localhost/contacts'


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    form=SignupForm()
    if request.method=='GET':
        return render_template('createnew.html', form=form)
    else:
        if form.validate() == True:
            contact = Contact(form.name.data, form.email.data, form.phone.data)
            db.session.add(contact)
            db.session.commit()
            return 'Success!'
        else:
            return 'Validation failed'

if __name__ == "__main__":
  app.run(debug=True)
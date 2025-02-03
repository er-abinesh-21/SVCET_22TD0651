from flask import Flask, render_template, request
from form import Nameform

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = Nameform()
    if form.validate_on_submit():
       return f"Hello, {form.name.data}!"
    return render_template('form.html', form=form)

@app.errorhandler(404)
def not_found(error):
    return "PAGE NOT FOUND", 404

@app.errorhandler(500)
def internal_error(error):
    return "Internal Server Error", 500

if __name__ == '__main__':
    app.run(debug=True)

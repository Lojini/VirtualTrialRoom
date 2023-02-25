import os
from flask import *

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('login.html')


@app.route('/home')
def home_page():
    hists = os.listdir('static/img/product')
    hists = [file for file in hists]
    print(hists)
    return render_template("index.html", hists=hists)


@app.route("/productsByCategory", methods=["GET"])
def post():
    gender = request.args["Gender"]
    category = request.args["Category"]
    hists = os.listdir('static/img/product/'+gender+"/"+category)
    hists = [file for file in hists]
    return hists


@app.route('/product')
def product_page():
    product_name = request.args["product_name"]
    gender = request.args["gender"]
    category = request.args["category"]
    return render_template("shop-details.html", product_name=product_name, gender=gender, category=category)


@app.route('/upload', methods=['POST'])
def success():
    if request.method == 'POST':
        print(request)
        gender = request.form['gender']
        category = request.form['category']
        f = request.files['file']
        f.save(os.path.join("static/img/product/", gender, category, f.filename))
        return redirect(url_for('home_page'))


if __name__ == '__main__':
    app.run(debug=True)

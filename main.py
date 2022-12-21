import os
from distutils.log import debug
from fileinput import filename
from flask import *

app = Flask(__name__)


@app.route('/')
def main():
    hists = os.listdir('static/img/product')
    hists = [ file for file in hists]
    return render_template('index.html', hists=hists)


@app.route('/product')
def product_page():
    product_name = request.args["product_name"]
    return render_template("shop-details.html", product_name=product_name)


@app.route('/upload', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join("static/img/product/", f.filename))
        return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(debug=True)

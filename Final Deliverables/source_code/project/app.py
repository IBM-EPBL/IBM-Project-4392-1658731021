from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='Templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/404')
def error():
    return render_template('404.html')

if __name__=='__main__':
     port = int(os.environ.get('PORT', 5000))
     app.run(debug=True, host='0.0.0.0', port=port)

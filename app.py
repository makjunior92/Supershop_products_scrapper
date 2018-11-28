from flask import Flask,request,Response
from flask import render_template
from shwapno import Shwapno
from flask_cors import CORS
app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def hello_world():
    return 'Hello World! <a href="/search_products">Search</a>'


@app.route('/search_products')
def search_products_func():
   return render_template('search_products.html')

@app.route('/find_products')
def find_products_func():
    pname = request.args.get('pname')
    swapno_app = Shwapno(pname, 'Uttara')
    list = swapno_app.prod_list
    return render_template('results.html',result = list)



if __name__ == '__main__':
    app.run()

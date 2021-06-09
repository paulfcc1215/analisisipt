import sys
from typing import ContextManager
from flask import Flask, render_template, jsonify, make_response, request, json

from utils import *

app = Flask(__name__)

@app.route('/', methods=['GET', ])
def home():
    return render_template('index.html')


@app.route('/graficas', methods=['GET','POST'])
def graficas():
    industrias = get_industrias()
    test_data = test()
    return render_template('graficas.html', test_data=test_data, industrias=industrias)


@app.route('/ajax', methods=['POST', ])
def ajax_test():
    
    desde = request.form.get("fecha_desde")
    hasta = request.form.get("fecha_hasta")
    industrias = json.loads(request.form.get("industrias"))
    print(industrias)
    #data = get_model(5,desde,hasta)
    for i in industrias:
        data = get_model(i,desde,hasta)
    
    # data = {
    #     'Feb-2016' : 93.82, 
    #     'Mar-2016' : 93.82,
    #     'Abr-2016' : 93.05,
    #     'May-2016' : 93.45,
    #     'Jun-2016' : 92.54,
    #     'Jul-2016' : 92.20
    # }
    response = make_response(jsonify(data), 200)
    response.headers["Content-Type"] = "application/json"
    return response
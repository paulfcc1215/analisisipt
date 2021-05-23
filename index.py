import sys
from typing import ContextManager
from flask import Flask, render_template
from utils import get_industrias, get_model

def app(environ, start_response):
	test_data = get_model()
	industrias = get_industrias()
	#data=str(render_template('index.html', test_data=test_data, industrias=industrias))
	status = '200 OK'
	response_headers = [
		('Content-type', 'text/plain'),
		('Content-Length', str(len(data)))
	]
	start_response(status, response_headers)
	data="fer"
	return iter([data])

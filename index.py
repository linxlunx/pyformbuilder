#!/usr/bin/env python

from flask import Flask, request, Response, render_template, session, redirect
from config import config
from formbuilder import formLoader
import json

app = Flask(__name__, static_folder='src')

app.secret_key = 'Sh3r1n4Mun4F'

@app.route('/')
def index():

	return render_template('index.html', base_url=config['base_url'])

@app.route('/save', methods=['POST'])
def save():
	if request.method == 'POST':
		formData = request.form.get('formData')

		if formData == 'None':
			return 'Error processing request'

		session['form_data'] = formData

		return 'tes'

@app.route('/render')
def render():
	if not session['form_data']:
		redirect('/')

	form_data = session['form_data']
	session['form_data'] = None

	form_loader = formLoader(form_data, '{0}/submit'.format(config['base_url']))
	render_form = form_loader.render_form()

	return render_template('render.html', render_form=render_form)

@app.route('/submit', methods=['POST'])
def submit():
	if request.method == 'POST':
		form = json.dumps(request.form)

		return form

if __name__ == '__main__':
	app.debug = True
	app.run()
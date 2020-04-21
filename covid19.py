from flask import Flask, render_template, abort
import requests
import json

app = Flask(__name__)

api = 'https://api.covid19api.com/summary'
r = requests.get(api).content
data = json.loads(r)
data_by_country = data['Countries']



@app.route('/<variable>')
def output(variable):
	for country in data_by_country:
		if variable.lower() == country['Slug']:
			country_name = country['Country']
			country_slug = country['Slug']
			total_cases = "{:,}".format(country['TotalConfirmed'])
			total_deaths = "{:,}".format(country['TotalDeaths'])
			total_recovered = "{:,}".format(country['TotalRecovered'])
			return render_template('index2.html', country=country_name, country_slug=country_slug, total_cases=total_cases, total_deaths=total_deaths, total_recovered=total_recovered)
	return abort(404)

if __name__ == '__main__':
	app.run(debug=True)
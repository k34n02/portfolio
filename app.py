from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'London',
  'salary': '£10,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'London',
  'salary': '£12,000'
}, {
  'id': 3,
  'title': 'Data Engineer',
  'location': 'London',
  'salary': '£13,000'
}]


@app.route('/')
def hello_world():
  return render_template("home.html", jobs=JOBS)


@app.route('/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

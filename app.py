from flask import Flask, render_template , jsonify
# flask is the module with small f letter and Flask is the class of this module with capital F and now we will create an object for this class as python is a object oriented programming language.

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title' : 'Data Analyst',
  'location' : 'Bengaluru India',
  'salary' : 'Rs 1,50,000'
  
        },
        {
          'id': 1,
          'title' : 'Data Analyst',
          'location' : 'Bengaluru India',
          'salary' : 'Rs 1,50,000'

        },
        {
          'id': 2,
          'title' : 'Frontend Engineer',
          'location' : 'Remote',
          'salary' : 'Rs 12,00,000'

        },
        {
          'id': 3,
          'title' : 'Data Scientist',
          'location' : 'Delhi India',
          'salary' : 'Rs 15,00,000'

        },
        {
          'id': 4,
          'title' : 'Backend Engineer',
          'location' : 'San Francisco USA',
          'salary' : '$ 120,000'

        },
       ]

@app.route("/")
def hello():
  return render_template('home.html', jobs = JOBS , company_name = 'Jobophia')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
 app.run(host='0.0.0.0' , debug=True)
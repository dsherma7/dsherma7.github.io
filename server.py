from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('template.html')

@app.route('/my-link/')
def my_link():
  print ('I got clicked!')
  return ('Click.')

@app.route('/temp/index.html')
def github_io():
  print ('My Github.io')
  return('click')

if __name__ == '__main__':
  app.run(debug=True)
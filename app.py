from flask import Flask, request, render_template
from logic.algorithm import *
from waitress import serve


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
  r= ''
  if request.method=='POST':
    data = [request.form['a'], request.form['b'], request.form['c'], request.form['d'], request.form['e'], request.form['f'], request.form['g'], request.form['h'], request.form['i'], request.form['j'], request.form['k'], request.form['l']] 
    data2 = [float(i) for i in data]

    res = getResult(data2)
    if res==0:
      r = "Good"
    elif res==1:
      r ="Poor"
    else:
      r = "Standard"
  return render_template('index.html', result=r)

if __name__=='__main__':
  # app.run(debug=True)
  serve(app, host='0.0.0.0', port=50100)
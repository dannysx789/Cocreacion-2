from flask import Flask, request, render_template
import requests

app= Flask(__name__)


@app.route('/')
def index():
   boyaca_url="https://wttr.in/boyaca?format=2"
   boyaca_answer = requests.get(boyaca_url);
   cundinamarca_url="https://wttr.in/cundinamarca?format=2"
   cundinamarca_answer = requests.get(cundinamarca_url);
   if (boyaca_answer.status_code == 200 and cundinamarca_answer.status_code == 200):
      
    return render_template('index.html', boyaca_temperature=boyaca_answer.text, cundinamarca_temperature=cundinamarca_answer.text);
   else:
    return render_template('index.html', boyaca_temperature="no se encontro", cundinamarca_temperature="no se encontro");
   
 
   
  

@app.route('/cundinamarca')
def render_cundinamarca():
   return render_template("boyaca.html");
  
 

@app.route('/boyaca')
def render_boyaca():
   return render_template("boyaca.html");

@app.route('/a')
def render_clima():
   return render_template("clima.html");

@app.route('/clima', methods =['POST','GET'])
def get_weather():
   city =request.form['clima']
   url="https://wttr.in/"+city+"?format=3"
   answer = requests.get(url);
   if (answer.status_code == 200):
    return render_template('clima.html', temperature=answer.text) ;
   else:
    return f'La ciudad no se encuentra';

if __name__ == '__main__':
   app.run(debug=True);
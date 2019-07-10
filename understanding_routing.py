from flask import Flask 
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say_hi(name):
    return 'Hi '+ name.title() + '!'

@app.route('/repeat/<num>/<word>')
def repeatWord(num,word):
    return (word + '\n') * int(num)

if __name__=="__main__":
    app.run(debug=True)
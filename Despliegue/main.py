from flask import Flask, render_template, request
import pickle


app = Flask(__name__)


with open('modelo2.pkl', 'rb') as f:
    modelo2 = pickle.load(f)
    
@app.route('/')
def home():
    return render_template('index.html')


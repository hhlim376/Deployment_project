# import Flask and jsonify
import flask
from flask import Flask, jsonify, request
import pandas as pd
import numpy as np
import traceback 
import pickle

## First create app
app = Flask(__name__)

## Load our model from pickle file
with open('pipeline_rfc.pickle','rb') as f:
    pipeline_rfc = pickle.load(f)
    

## Create an endpoint
@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if flask.request.method == 'GET':
        return "Use POST with parameters to get predictions!"

    if flask.request.method == 'POST':
        try:
            json = request.json
            
            df_data = pd.DataFrame(json, index=[0])
            prediction = pipeline_rfc.predict(df_data)
            
            return jsonify(prediction.tolist())
           
        except:
            return jsonify({
                    "trace": traceback.format_exc()
            }) 
    
if __name__ == "__main__":
    app.run()
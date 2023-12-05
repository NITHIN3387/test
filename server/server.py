from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/hello', methods = ['GET'])
def hello():
    responce = jsonify({
        "msg": "hello world" 
    })
    
    responce.headers.add("Access-Control-Allow-Origin", "*")
    
    return responce

@app.route('/predict', methods = ['POST'])
def predict():
    print('you have called me')
    N_value = request.form['N_value']
    P_value = request.form['P_value']
    K_value = request.form['K_value']
    Season = request.form['Season']
    
    responce = jsonify({
        "prediction": util.get_prediction(N_value, P_value, K_value, Season)
    })
    
    responce.headers.add("Access-Control-Allow-Origin", "*")
    
    return responce

if __name__ == "__main__":
    print("python flask server started running")
    util.load_model()
    app.run()
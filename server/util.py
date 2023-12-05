import pickle
import numpy as np

__model = None

def load_model():
    print('loading model...')
    global __model
    
    with open('/media/nithin/DATA/jupyter codes/Real Estate Price Prediction Project/test/server/artifacts/model.pkl', 'rb') as f:
        __model = pickle.load(f)
    
    print('model loaded successfully :)')
    
def get_prediction(N_value, P_value, K_value, Season):
    print(N_value, P_value, K_value, Season)
    x = np.zeros(4)
    
    x[0] = N_value
    x[1] = P_value
    x[2] = K_value
    x[3] = Season
    
    return __model.predict([x])[0]
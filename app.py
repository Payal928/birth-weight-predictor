from flask import Flask,request,jsonify,render_template
import pandas as pd
import pickle

# make instace 
app = Flask(__name__)

def clean_data(form_data):
    gestation = float(form_data['gestation'])
    parity = int(form_data['parity'])
    age = float(form_data['age'])
    height = float(form_data['height'])
    weight = float(form_data['weight'])
    smoke = float(form_data['smoke'])

    cleaned_data = {'gestation':[gestation],
                    'parity': [parity],
                    'age':[age],
                    'height':[height],
                    'weight' :[weight],
                    'smoke':[smoke]}

    return cleaned_data




@app.route('/' , methods = ['GET'])
def home():
    return render_template('main_app.html')



@app.route('/predict' , methods = ['POST'])
def predict():

    # get json data from user
    baby_data = request.form

    #convert this data in dict 
    clean_data_babay = clean_data(baby_data)

    #convert json data to dataframe

    data_df = pd.DataFrame(clean_data_babay)

    # load ml model
    with open('model.pkl' , 'rb') as obj:
        model = pickle.load(obj)

    # predict weight 
    prediction = model.predict(data_df)# making float coz it array and cannnot make aray as json data 

    prediction = round(float(prediction[0]),2)
    ounce = 'ounce'


    return render_template('main_app.html' , prediction = prediction , ounce = ounce)
    


# trigger flask app 
if __name__ == '__main__':
    app.run(debug = True)
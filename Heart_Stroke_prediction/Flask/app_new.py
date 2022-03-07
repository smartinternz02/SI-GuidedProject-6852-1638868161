from flask import Flask, request,render_template
import joblib
import numpy as np
app = Flask(__name__)
model = joblib.load("model")

app = Flask(__name__)

@app.route('/')
def predict():
    return render_template('Manual_predict.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    g= request.form["Gender"]
    if (g == 'f'):
        g1,g2,g3=1,0,0
    if (g == 'm'):
        g1,g2,g3=0,1,0
    if (g == 'o'):
        g1,g2,g3=0,0,1
    age= request.form["Age"]
    q= request.form["Hypertension"]
    if (q == 'n'):
        q=0
    if (q == 'y'):
        q=1
    hd= request.form["heart_disease"]
    if (hd == 'n'):
        hd=0
    if (hd == 'y'):
        hd=1    
    em= request.form["ever_married"]
    if (em == 'n'):
        em=0
    if (em == 'y'):
        em=1   
    wt= request.form["work_type"]
    if (wt == 'ch'):
        wt1,wt2,wt3,wt4,wt5 = 1,0,0,0,0
    if (wt == 'gvt'):
        wt1,wt2,wt3,wt4,wt5 = 0,1,0,0,0
    if (wt == 'unemp'):
        wt1,wt2,wt3,wt4,wt5 = 0,0,1,0,0   
    if (wt == 'pvt'):
        wt1,wt2,wt3,wt4,wt5 = 0,0,0,1,0
    if (wt == 'self'):
        wt1,wt2,wt3,wt4,wt5 = 0,0,0,0,1
    rt= request.form["Residence_type"]
    if (rt == 'rural'):
        rt=0
    if (rt == 'urban'):
        rt=1  
    agl= request.form["avg_glucose_level"]
    bmi= request.form["BMI"]
    sm= request.form["smoking_status"]
    if (sm == 'for'):
        sm1,sm2,sm3=1,0,0
    if (sm == 'ns'):
        sm1,sm2,sm3=0,1,0
    if (sm == 's'):
        sm1,sm2,sm3=0,0,1    
        
    inp= np.array([g1,g2,g3,wt1,wt2,wt3,wt4,wt5,sm1,sm2,sm3,age,q,hd,em,rt,agl,bmi])
    print(inp)
            
    pred = model.predict([inp])   
    print(pred)    

    if(pred[0]==0):
        result="no chances of stroke"
    else:result="chances of stroke"
    
    return render_template('Manual_predict.html', \
                           prediction_text=('There are \
                                            ',result))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
    

from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    weight=request.form['1']
    height=request.form['2']

    weight=float(weight)
    height=float(height)

    height=height/100  #cm to m

    BMI=weight/(height*height)

    BMI=round(BMI,2)
    
    if BMI > 0:
        if BMI <= 16:
            return render_template('result.html',pred=f"Your Body Mass Index is {BMI}. You are Severely UnderWeight!!!")
        elif BMI <=18.5:
            return render_template('result.html',pred=f"Your Body Mass Index is {BMI}. You are UnderWeight!!")
        elif BMI <=25:
            return render_template('result.html',pred=f"Your Body Mass Index is {BMI}. You are Healthy.")
        elif BMI <=30:
            return render_template('result.html',pred=f"Your Body Mass Index is {BMI}. You are OverWeight!!")
        else:
            return render_template('result.html',pred=f"Your Body Mass Index is {BMI}. You are Severely OverWeight!!!")
    else:
        return render_template('result.html',pred="Enter Correct Details Of Weight and Height")

if __name__=='__main__':
    app.run(debug=True)
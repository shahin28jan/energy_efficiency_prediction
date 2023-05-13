from flask import Flask,request,render_template,jsonify
from src.pipeline.predict_pipeline import CustomData,PredictPipeline


application=Flask(__name__)

app=application



@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])

def predict_datapoint():
    if request.method=='GET':
        return render_template('form.html')
    
    else:
        data=CustomData(
            relative_compactness=float(request.form.get('relative_compactness')),
            surface_area=float(request.form.get('surface_area')),
            wall_area = float(request.form.get('wall_area')),
            roof_area = float(request.form.get('roof_area')),
            overall_height = float(request.form.get('overall_height')),
            glazing_area = float(request.form.get('glazing_area')),
            glazing_area_distribution = float(request.form.get('glazing_area_distribution'))      
        )
        final_new_data=data.get_data_as_dataframe()
        predict_pipeline=PredictPipeline()
        pred=predict_pipeline.predict(final_new_data)

        result=pred

        return render_template('result.html',final_result=result)






if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)
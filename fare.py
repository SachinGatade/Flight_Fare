from flask import Flask,request,render_template,url_for
import numpy as np
import pickle

with open ("model.pkl","rb")as f:
    model=pickle.load(f)

app=Flask(__name__)

@app.route("/")
def welcome():
    return render_template("fare.html")

@app.route("/fare",methods=["POST"])
def fare():
    Source=float(request.form["Source"])
    Destination=float(request.form["Destination"])
    Total_Stops=float(request.form["Total_Stops"])
    Air_India=float(request.form["Air_India"])
    GoAir=float(request.form["GoAir"])
    IndiGo=float(request.form["IndiGo"])
    Jet_Airways=float(request.form["Jet_Airways"])
    Jet_Airways_Business=float(request.form["Jet_Airways_Business"])
    Multiple_carriers=float(request.form["Multiple_carriers"])
    Multiple_carriers_Premium_economy=float(request.form["Multiple_carriers_Premium_economy"])
    SpiceJet=float(request.form["SpiceJet"])
    Trujet=float(request.form["Trujet"])
    Vistara=float(request.form["Vistara"])
    Vistara_Premium_economy=float(request.form["Vistara_Premium_economy"])
    Journey_Month=float(request.form["Journey_Month"])
    Journey_Day=float(request.form["Journey_Day"])
    Dep_Time_Hours=float(request.form["Dep_Time_Hours"])
    Dep_Time_Minute=float(request.form["Dep_Time_Minute"])
    Duration_hours=float(request.form["Duration_hours"])
    Duration_min=float(request.form["Duration_min"])

    data=np.array([Source,Destination,Total_Stops,Air_India,GoAir,IndiGo,
    Jet_Airways,Jet_Airways_Business,Multiple_carriers,Multiple_carriers_Premium_economy,
    SpiceJet,Trujet,Vistara,Vistara_Premium_economy,Journey_Month,Journey_Day,Dep_Time_Hours,
    Dep_Time_Minute,Duration_hours,Duration_min],ndmin=2)
    result=model.predict(data)
    return render_template("result.html",predict=result)
 					
@app.route("/fare/result")
def result():
    return render_template(url_for("result.html"))		


if __name__ =="__main__":
    app.run(host='0.0.0.0',port=8080,debug=True )
from flask import Flask, jsonify, render_template, request
from project_app.utils import LoanPre

# Creating instance here
# 'app' is standard variable
app = Flask(__name__)

# @app.route("/") --> USED TO GET HOME API
# @app.route("/furniture") --> You will get 'Furniture' Page here

@app.route("/")
def hello_flask():
    print("Welcome to Product Sales Prediction")
    return render_template("index.html")



@app.route("/predict_charges", methods=["POST", "GET"])
def get_loan_pred():
    if request.method == "GET":
        print("We are in a GET Method")
                
        credit_policy = float(request.args.get("credit_policy"))
        int_rate = float(request.args.get("int_rate"))
        installment = float(request.args.get("installment"))
        log_annual_inc = float(request.args.get("log_annual_inc"))
        dti = float(request.args.get("dti"))
        fico = float(request.args.get("fico"))
        days_with_cr_line = float(request.args.get("days_with_cr_line"))
        revol_bal = float(request.args.get("revol_bal"))
        revol_util = float(request.args.get("revol_util"))
        inq_last_6mths = float(request.args.get("inq_last_6mths"))
        delinq_2yrs = float(request.args.get("delinq_2yrs"))
        pub_rec = float(request.args.get("pub_rec"))
        purpose = request.args.get("purpose")

    else:
        print("Error in if block")
        
    lon_pri = LoanPre(credit_policy,int_rate,installment,log_annual_inc,dti,fico,days_with_cr_line,revol_bal,revol_util,inq_last_6mths,delinq_2yrs,pub_rec,purpose)
    charges = lon_pri.get_predicted_charges()
    
    if charges == 1:
        charges_text = "you have some amount left contact to branch immediately"
    else:
        charges_text = "Your Loan Is approved"
    
    return render_template("index.html", prediction=charges_text)


print("__name__-->",__name__)
if __name__=="__main__":
    #app.run(host="0.0.0.0",post=5000,debug=false)
    app.run()



